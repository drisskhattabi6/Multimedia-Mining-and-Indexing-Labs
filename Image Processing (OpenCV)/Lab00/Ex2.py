import cv2

img = cv2.imread("Lab00/images/fondvert.png")
bg = cv2.imread("Lab00/images/test.jpg")
bg = cv2.resize(bg, (img.shape[1], img.shape[0]))

hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsvImg, (35, 100, 100), (85, 255, 255))

invMask = 255 - mask
finalFG = cv2.bitwise_and(img, img, mask=invMask)
finalBG = cv2.bitwise_and(bg, bg, mask=mask)


final_img = finalFG + bg
# final_img = finalFG + finalBG

cv2.imshow("mask",mask)
cv2.imshow("inverted mask",invMask)
cv2.imshow("final foreground",finalFG)
cv2.imshow("final background",finalBG)
cv2.imshow("final",final_img)

cv2.imwrite("Lab00/images/fondvert-changed-background.png", final_img)

cv2.waitKey(0)
cv2.destroyAllWindows()