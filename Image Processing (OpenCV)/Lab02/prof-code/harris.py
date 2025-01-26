# Détection des points d’intérêt par l’opérateur de Harris
import numpy as np
import cv2 as cv

img = cv.imread("Image Processing (OpenCV)/Lab02/images/coins.jpg")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgFloat = np.float32(imgGray)
# Deuxième et troisième paramètre : taille du voisinage et taille de masque de Sobel
# Quatrième paramètre : paramètre libre qui apparait dans la formule prévue par Harris
dst = cv.cornerHarris(imgFloat, 7, 5, 0.1)
# Choix du seuil optimal, il dépend de l'image
seuil = 0.1 * dst.max()
dim = dst.shape
for i in range(dim[0]):
    for j in range(dim[1]):
        if dst[i, j] > seuil:
            cv.circle(img, (j, i), 1, (0, 0, 255), 1)
cv.imshow("dst", img)
cv.waitKey(0)
cv.destroyAllWindows()
