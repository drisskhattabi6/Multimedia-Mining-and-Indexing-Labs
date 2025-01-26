import numpy as np
from random import randrange
import cv2 as cv

# Lecture
img = cv.imread("Image Processing (OpenCV)/Lab02/images/coins.jpg")
cv.imshow("Originale", img)
# Seuillage
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 80, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# Erosion pour définir les marqueurs (points à 255 appartienent aux objets)
kernel = np.ones((3, 3), np.uint8)
objets = cv.erode(thresh, kernel, iterations=5)
cv.imshow("Marqueurs", objets)
# dilatation : pointsà 0 appartiennet au fond
fond = cv.dilate(thresh, kernel, iterations=5)
# Étiquettage de l'image binaire
ret, markers = cv.connectedComponents(objets)
markers[markers > 0] += 1
# Marquer les points fonds avec l'étiquette 1
markers[fond == 0] = 1
cv.imshow("Étiquetage", np.uint8(markers * 20))
# Application de l'algorithme ( -1 : Pour les bordures )
markersw = cv.watershed(img, markers)
# Affichage en couleur
imgr1 = np.zeros(img.shape, np.uint8)
# Affichage des lignes de partage des eaux en blanc
imgr1[markersw == -1] = [255, 255, 255]
# Couleur aléatoire par composante (Pour ne pas colorier le fond, on commence par l’étiquette 2)
for label in range(2, markers.max() + 1):
    imgr1[markersw == label] = [randrange(256), randrange(256), randrange(256)]
cv.imshow("Segmentation", imgr1)
cv.waitKey(0)
cv.destroyAllWindows()
