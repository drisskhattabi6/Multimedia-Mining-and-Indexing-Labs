import cv2
import json
import numpy as np


def main():
    img = cv2.imread("Image Processing (OpenCV)/Lab02/images/coins.jpg", 1)
    gris1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # pré-traitement
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
    j = 0
    pieces = {0: 0.05, 1: 0.1, 2: 0.5, 3: 1, 4: 2}
    dic = {}
    for i in circles[0, :]:
        print(j, ":", "(", i[0], i[1], ")", i[2])
        j = j + 1
        # Tracer
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
        cv2.imshow("Cercles", img)
        print("0:0.05, 1:0.1, 2:0.5, 3:1, 4:2 ( Euros ) : ")
        val = cv2.waitKey(0) - 48
        dic[str(i[2])] = float(pieces[val])
    # Afficher et sauvegarde
    print(dic)
    with open("data.json", "w") as fp:
        json.dump(dic, fp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
