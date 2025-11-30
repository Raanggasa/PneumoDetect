# 🫁 PneumoDetect AI: Deteksi Pneumonia Berbasis Deep Learning

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**PneumoDetect AI** adalah aplikasi web cerdas yang dirancang untuk membantu tenaga medis dalam mendeteksi tanda-tanda Pneumonia pada citra X-Ray dada (*Chest X-Ray*) secara otomatis menggunakan teknologi *Deep Learning* (CNN).

Proyek ini dikembangkan sebagai bagian dari penelitian **Analisis Big Data** untuk meningkatkan efisiensi dan akurasi diagnosis awal penyakit paru-paru.

---

## 🚀 Demo Aplikasi (Live)

Aplikasi ini telah di-deploy dan dapat diakses secara publik melalui link berikut:

### [🔗 Coba Live Demo di Hugging Face](https://huggingface.co/spaces/raanggasa/deteksi-pneumonia)

---

## ✨ Fitur Utama

* **⚡ Deteksi Instan:** Menggunakan model CNN yang telah dilatih untuk memberikan hasil prediksi (Normal / Pneumonia) dalam hitungan detik.
* **📊 Confidence Score:** Menampilkan tingkat keyakinan (probabilitas) AI terhadap hasil prediksinya dalam persentase.
* **📈 Visualisasi Data:** Dashboard interaktif yang menampilkan performa model (Kurva Loss/Akurasi, Confusion Matrix, ROC Curve) menggunakan *Chart.js*.
* **📱 Desain Responsif:** Antarmuka pengguna (UI) berbasis Bootstrap 5 yang modern, bersih, dan dapat diakses melalui Desktop maupun Mobile.
* **🔒 Privasi:** Tidak menyimpan data pasien secara permanen (*stateless processing*).

---

## 🛠️ Teknologi yang Digunakan

### Backend & AI
* **Python 3.9**: Bahasa pemrograman utama.
* **TensorFlow & Keras**: Framework untuk membangun, melatih, dan menjalankan model CNN.
* **Flask**: Micro-framework web untuk melayani API prediksi dan rendering template.
* **NumPy & Pillow**: Library untuk pemrosesan array dan citra digital.

### Frontend
* **HTML5 & CSS3**: Struktur halaman.
* **Bootstrap 5**: Framework CSS untuk styling yang responsif.
* **JavaScript (Chart.js)**: Library untuk visualisasi grafik performa model secara interaktif.

### Deployment
* **Docker**: Kontainerisasi aplikasi untuk konsistensi lingkungan.
* **Gunicorn**: Production WSGI Server untuk performa tinggi.
* **Hugging Face Spaces**: Platform hosting berbasis cloud.

---

## 🧠 Arsitektur Model & Performa

Model yang digunakan adalah **Custom Convolutional Neural Network (CNN)** yang dilatih pada dataset Chest X-Ray (Kaggle/Mendeley) berisi 5,800+ gambar.

* **Input Shape:** 150x150 pixels (Rescaled 1./255).
* **Layers:** 4 Blok Konvolusi (Conv2D + MaxPooling) untuk ekstraksi fitur, diikuti oleh Flatten dan Dense Layers.
* **Regularization:** Menggunakan Dropout (0.5) dan L2 Regularization untuk mencegah *overfitting*.
* **Output:** Sigmoid Activation (Binary Classification).

### Metrik Evaluasi (Pada Data Uji)
| Metrik | Nilai | Deskripsi |
| :--- | :--- | :--- |
| **Akurasi** | **89%** | Ketepatan prediksi keseluruhan. |
| **Recall (Sensitivitas)** | **98%** | Kemampuan model mengenali kasus positif (Pneumonia), meminimalisir False Negative. |
| **AUC Score** | **0.96** | Area Under Curve, menunjukkan performa klasifikasi yang sangat baik. |

---

## 💻 Instalasi dan Menjalankan Lokal

Jika Anda ingin menjalankan proyek ini di komputer Anda sendiri, ikuti langkah-langkah berikut:

### Prasyarat
Pastikan **Python 3.8+** dan **Git** sudah terinstall di komputer Anda.

### 1. Clone Repository
```bash
git clone [https://github.com/Raanggasa/PneumoDetect.git](https://github.com/Raanggasa/PneumoDetect.git)
cd PneumoDetect
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
python app.py
```

Buka browser Anda dan akses alamat: ```bash http://127.0.0.1:5000 ```

### 📸 Antarmuka Aplikasi
![Beranda](https://uploads.onecompiler.io/42bwrvdku/4467dr656/127.0.0.1_5000_.png)
![Diagnosa](https://uploads.onecompiler.io/4467dvrwg/4467dvwsh/127.0.0.1_5000_%20(1).png)
![Tentang Sistem](https://uploads.onecompiler.io/4467dvrwg/4467dvwsh/127.0.0.1_5000_%20(2).png)
![Tim](https://uploads.onecompiler.io/4467dvrwg/4467dvwsh/127.0.0.1_5000_%20(3).png)

### ⚠️ Disclaimer Medis
**PENTING:**
* Aplikasi ini dikembangkan semata-mata untuk tujuan Edukasi dan Penelitian.
* Hasil prediksi yang diberikan oleh sistem AI ini BUKAN merupakan diagnosis medis final.
* Sistem ini tidak menggantikan peran dokter atau ahli radiologi.
* Selalu konsultasikan hasil pemeriksaan dengan tenaga medis profesional.
* Pengembang tidak bertanggung jawab atas keputusan medis yang diambil berdasarkan hasil aplikasi ini.

### 👥 Tim Pengembang
* **Putri Yuli Utami.,S.Kom.,M.Kom** - Dosen Pembimbing
* **Rangga Aditya Saputra** - Mahasiswa
* **Ferdian Putra Wijaksono** - Mahasiswa


