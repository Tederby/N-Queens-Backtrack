# N-Queens Problem: Backtracking Visualization

Repository ini berisi implementasi penyelesaian N-Queens Problem menggunakan algoritma Backtracking dalam bahasa pemrograman Python. Program ini dilengkapi dengan visualisasi sederhana berbasis Command Line Interface (CLI) untuk memperlihatkan langkah-langkah evaluasi algoritma secara real-time.

## Deskripsi Algoritma

Algoritma backtracking digunakan untuk mencari solusi dengan cara mencoba berbagai kemungkinan penempatan secara bertahap. Pada kasus N-Queens (di sini menggunakan papan 4x4):

1. Algoritma akan mencoba menempatkan Ratu di kolom pertama.

2. Jika aman (tidak saling serang dengan Ratu lain di baris, kolom, atau diagonal), algoritma lanjut ke kolom berikutnya.

3. Jika penempatan berujung pada jalan buntu di langkah selanjutnya, algoritma akan melakukan backtrack (mundur), mencabut Ratu dari posisi tersebut, dan mencoba posisi lain.

### Indikator Visual (CLI)

- . : Sel kosong.

- ? : Sedang dievaluasi oleh algoritma.

- Q : Ratu ditempatkan (sementara/permanen jika aman).

- x : Jalan buntu, algoritma akan melakukan backtrack dari posisi ini.

## Persyaratan Sistem

- Python 3.x

- Tidak memerlukan library eksternal (hanya menggunakan built-in module time dan os).

## Cara Menjalankan Program

1. Clone atau unduh repository ini.

2. Buka terminal atau command prompt.

3. Arahkan direktori ke tempat file disimpan.

4. Jalankan perintah berikut:

    python main.py
