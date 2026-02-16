# 🧪 Cellular Automata Simulation  
## Conway's Game of Life (Implementasi ADT Array)

---

## 📌 Deskripsi Proyek

Proyek ini merupakan simulasi **Conway's Game of Life**, sebuah model *cellular automata* klasik yang dikembangkan oleh John Conway.

Berbeda dari implementasi umum yang menggunakan list Python secara langsung, proyek ini membangun dan memanfaatkan **Abstract Data Type (ADT) Array** sebagai struktur utama penyimpanan grid.

Tujuan utamanya adalah memahami bagaimana array bekerja secara konseptual dan bagaimana struktur data sederhana dapat menghasilkan pola kompleks.

---

## 🧠 Konsep yang Digunakan

- Abstract Data Type (ADT) Array
- Struktur Data Linear
- Grid 2 Dimensi
- Cellular Automata
- Algoritma berbasis aturan

---

## ⚙️ Aturan Game of Life

Setiap sel memiliki dua kemungkinan keadaan:

- 🔲 Mati (0)
- 🟩 Hidup (1)

Aturan evolusi setiap generasi:

1. Sel hidup dengan kurang dari 2 tetangga → mati (underpopulation)
2. Sel hidup dengan 2 atau 3 tetangga → tetap hidup
3. Sel hidup dengan lebih dari 3 tetangga → mati (overpopulation)
4. Sel mati dengan tepat 3 tetangga → hidup (reproduction)

---

## 🏗️ Struktur Program

Program terdiri dari:

- Inisialisasi grid menggunakan ADT Array
- Fungsi untuk menghitung jumlah tetangga
- Proses pembentukan generasi berikutnya
- Tampilan grid setiap iterasi

Simulasi berjalan dalam beberapa generasi dengan jeda waktu antar frame.

---

## ▶️ Cara Menjalankan

### 1️⃣ Clone Repository

```bash
git clone https://github.com/username/nama-repository.git
cd nama-repository
