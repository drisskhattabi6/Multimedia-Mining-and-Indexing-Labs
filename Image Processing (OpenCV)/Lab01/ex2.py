import numpy as np
import cv2

def f(x):
    pass

def main():
    a = cv2.imread("images/sunset1.jpg",0)
    a = cv2.resize(a,(1080,720))
    cv2.imshow('Originale', a)
    # Binarisation
    seuil = 128
    b = np.uint8((a>=seuil)*255)
    # Ou encore
    # ret,b=cv2.threshold(a,seuil,255,cv2.THRESH_BINARY);
    # Calcul de l'histogramme
    histSize = 256
    hist = cv2.calcHist([a],[0],None,[histSize],[0,histSize-1])
    # calculer le graphe de l'histogramme et déssiner dans une image
    imHistW = 512
    imHistH = 400
    bord = 10
    binHistW = (imHistW-2*bord)/histSize
    histImage = np.ones((imHistH, imHistW, 1), dtype=np.uint8)*255
    # Histogramme normalisé
    cv2.normalize(hist, hist)
    hist=hist*imHistH
    for i in range(1, histSize):
        cv2.line(histImage, ( int(bord+binHistW*(i-1)), int(imHistH-bord- hist[i-1]) ),
                 ( int(bord+binHistW*i), int(imHistH-bord - hist[i])), 0)
    cv2.rectangle(histImage, ( bord,bord),(imHistW-bord, imHistH-bord ), 0)
    # Créer une autre image pour y ajouter la ligne correspondant au seuil
    histImagePlusLigne = histImage.copy()
    cv2.line(histImagePlusLigne, (int(bord+binHistW*seuil), imHistH-bord),
             ( int(bord+binHistW*seuil), bord), 128)
    cv2.imshow('Binarisation', b)
    cv2.imshow('Histogramme', histImagePlusLigne)
    cv2.createTrackbar('Seuil : ', 'Histogramme', 0, 255, f)
    cv2.setTrackbarPos('Seuil : ', 'Histogramme',seuil)
    while True:
        seuil = cv2.getTrackbarPos('Seuil : ', 'Histogramme')
        # Binarisation
        b = np.uint8((a>=seuil)*255)
        cv2.imshow('Binarisation', b)
        histImagePlusLigne = histImage.copy()
        cv2.line(histImagePlusLigne, (int(bord+binHistW*seuil), imHistH-bord),
                 ( int(bord+binHistW*seuil), bord), 128)
        cv2.imshow('Histogramme', histImagePlusLigne)
        if cv2.waitKey(100) & 0xFF == 27 :
            break
    cv2.destroyAllWindows()
        
if __name__ == "__main__":
    main()
