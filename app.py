import os
import numpy as np
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import io

app = Flask(__name__)

# Load Model (Hanya sekali saat start)
MODEL_PATH = 'model_pneumonia_final.h5'
model = load_model(MODEL_PATH)

def preprocess_image(img):
    # Resize gambar ke 150x150 sesuai training
    img = img.resize((150, 150))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # Normalisasi
    img_array = np.expand_dims(img_array, axis=0) # Batch dimension
    return img_array

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Tidak ada file yang diunggah'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Tidak ada file yang dipilih'})

    try:
        # Proses gambar dari memory (tanpa simpan ke disk)
        img = Image.open(io.BytesIO(file.read())).convert('RGB')
        processed_img = preprocess_image(img)
        
        # Prediksi
        prediction = model.predict(processed_img)
        score = float(prediction[0][0])
        
        # Logika Diagnosa (Sama seperti sebelumnya)
        threshold_high = 0.85
        threshold_low = 0.50
        
        confidence_percent = score * 100
        normal_percent = (1 - score) * 100
        
        if score > threshold_high:
            result = "PNEUMONIA"
            status = "danger" # Untuk warna merah
            confidence = f"{confidence_percent:.2f}%"
            message = "Sistem mendeteksi pola pneumonia dengan keyakinan sangat tinggi."
        elif score > threshold_low:
            result = "SUSPECT"
            status = "warning" # Untuk warna kuning
            confidence = f"{confidence_percent:.2f}%"
            message = "AI mendeteksi anomali namun belum cukup kuat. Disarankan cek ulang."
        else:
            result = "NORMAL"
            status = "success" # Untuk warna hijau
            confidence = f"{normal_percent:.2f}%"
            message = "Paru-paru terlihat bersih. Tidak ditemukan pola infeksi signifikan."

        return jsonify({
            'result': result,
            'confidence': confidence,
            'status': status,
            'message': message
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)