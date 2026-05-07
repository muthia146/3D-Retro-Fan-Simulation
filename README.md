# 3D Retro Fan Simulation (OpenGL)

Proyek Visualisasi 3D Kipas Angin Meja dengan fitur animasi osilasi dan kontrol kecepatan interaktif menggunakan Python dan PyOpenGL. Dibuat untuk memenuhi tugas UAS mata kuliah Grafika Komputer.

## Fitur Utama
- **Animasi:** Rotasi baling-baling dan osilasi (geleng) kepala kipas.
- **Interaksi:** Kontrol kecepatan (Level 0-3) dan toggle osilasi.
- **Simulasi:** Efek kertas terbang dinamis berdasarkan kekuatan angin.
- **Environment:** Ruangan retro dengan sistem pencahayaan dan kamera orbit.

## Teknologi
- Python 3.12+
- Pygame (Window Management)
- PyOpenGL (Graphic Rendering)

## Kontrol Keyboard & Mouse
| Input | Fungsi |
| :--- | :--- |
| **Angka 1, 2, 3** | Menyalakan kipas & pilih tingkat kecepatan |
| **Angka 0** | Power Off (Mematikan kipas) |
| **Tombol O** | Toggle Osilasi (Menyalakan/Mematikan gerak geleng) |
| **Klik Kiri + Drag** | Rotasi Kamera (Orbit) |
| **Scroll Mouse** | Zoom In / Out |
| **WASD / Panah** | Navigasi Kamera Manual |

## Cara Instalasi & Menjalankan
1. Clone repositori ini atau download source code.
2. Instal dependensi:
   ```bash
   pip install pygame PyOpenGL
3. Jalankan aplikasi:
    ```bash
   python main.py
