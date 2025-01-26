import cv2

# L'image est dans le sous-dossier "images" du dossier parent
# prendre une image de votre choix
nomimage = "../images/a.jpg"

# Lecture
img = cv2.imread(nomimage)

# La méthode retourne un objet de type numpy.ndarray
print("type",type(img))
print("shape", img.shape)
print("size",img.size)

# Afficher la taille de l'image
(h, w) = img.shape[:2] 
print("height= {}, width= {}".format(h,w)) 
    
# Nombre de canaux
c = img.shape[2]
print("Nombre de canaux= {}".format(c))

# Affichage de l'image originale
cv2.imshow('Lab10-a', img)

# Modifier une partie de l'image
# OpenCV organize le raster en tant que des triplets (Bleu, Vert, Rouge)
# img[50:200,50:200] = (0,255,0)

# Faire un crop
# imgCrop = img[50:200,50:200]

# Traitement dans RGB : Garder le canal 0 (Bleu)
img[:, :, 0] = 0
img[:, :, 1] = 0

# Affichage de l'image originale
cv2.imshow('Lab10-abis', img)

# Inverser l'image
#img = 255 -img
 
# Affichage de l'image résultat
#cv2.imshow('Lab10-b', img)

# Attendre une touche
cv2.waitKey(0)

# Sauvegarde du résultat
# cv2.imwrite("lab10(resultat).jpg", imgCrop)

# Libérer les fenêtres 
cv2.destroyAllWindows()
