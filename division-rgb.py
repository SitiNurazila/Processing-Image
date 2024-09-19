import cv2
import numpy as np

#membaca citra digital dari komputer
citra1 = cv2.imread("E:/Kuliah/Sem 3/PCD  Prak/kode program/image/chelsea - rgb.jpg")

#membaca channel warna BGR dan menyimpannya ke dalam variabel terpisah
b = citra1[:,:,0]
g = citra1[:,:,1]
r = citra1[:,:,2]


#menyimpan jumlah baris dan jumlah kolom dari citra
jum_baris = len(citra1)
jum_kolom = len(citra1[0])

#menyiapkan citra baru dengan nilai 0
citra_division = np.zeros((jum_baris, jum_kolom, 3))
divider = 3

#menghitung nilai pixel grayscale
for i in range(jum_baris):
    for j in range(jum_kolom):
        citra_division[i, j, 0] = int(b[i, j]) / divider
        citra_division[i, j, 1] = int(g[i, j]) /divider
        citra_division[i, j, 2] = int(r[i, j]) / divider

        # revisi nilai pixel jika > 255
        if (citra_division[i, j, 0] > 255): 
            citra_division[i, j, 0] = 255
        
        if (citra_division[i, j, 1] > 255): 
            citra_division[i, j, 1] = 255

        if (citra_division[i, j, 2] > 255): 
            citra_division[i, j, 2] = 255

citra_addition = citra_division.astype(np.uint8)

cv2.imshow("chelsea-rgb", citra1)
cv2.imshow("division", citra_addition)

cv2.waitKey()