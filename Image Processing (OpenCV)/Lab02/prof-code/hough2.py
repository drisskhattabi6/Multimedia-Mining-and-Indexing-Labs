# Calcul de la somme de monnaie (application sur une nouvelle image : im2.jpg)
import cv2
import json

import numpy as np


def valeur(x, d):
    kmin = 1000
    for k, v in d.items():
        if np.abs(int(k) - x) < kmin:
            kmin = np.abs(int(k) - x)
            vmin = v
    return float(vmin)


def main():
    img = cv2.imread("Image Processing (OpenCV)/Lab02/images/coins.jpg", 1)
    gris1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Pré-traitement
    kernel = np.ones((11, 11), np.uint8)
    gris2 = cv2.morphologyEx(gris1, cv2.MORPH_OPEN, kernel)
    gris2 = cv2.GaussianBlur(gris2, (11, 11), 5)
    # Hough

    circles = cv2.HoughCircles(
        gris2,
        cv2.HOUGH_GRADIENT,
        1,
        120,
        param1=120,
        param2=25,
        minRadius=50,
        maxRadius=100,
    )
    circles = np.uint16(np.around(circles))
    # Lecture des paramètres
    with open("data.json", "r") as fp:
        dic = json.load(fp)
    somme = 0.0
    for i in circles[0, :]:
        somme = somme + valeur(i[2], dic)
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    somme = np.around(somme, 2)
    # Affichage
    img = cv2.putText(
        img,
        "Somme : " + str(somme) + " Euros.",
        (10, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        1,
        cv2.LINE_AA,
    )
    cv2.imshow("Somme en Euros", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
