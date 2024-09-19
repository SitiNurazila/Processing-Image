from PIL import Image

# Membuka gambar
img = Image.open("Image Processing/chelsea - rgb.jpg")

# 1. Konversi ke Grayscale
grayscale_img = img.convert("L")
grayscale_img.save("Image Processing/chelsea - gray.jpg")  # Menyimpan gambar grayscale

# 2. Konversi ke Biner (Thresholding)
threshold = 128  # Nilai threshold, bisa diubah sesuai kebutuhan
binarized_img = grayscale_img.point(lambda p: 255 if p > threshold else 0, mode="1")
binarized_img.save("Image Processing/chelsea - biner.jpg")  # Menyimpan gambar biner

# Menampilkan hasil gambar grayscale dan biner
grayscale_img.show()
binarized_img.show()
