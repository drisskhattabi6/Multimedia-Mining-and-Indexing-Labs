import cv2

def placeholder(x):
    pass
    
img = cv2.imread("Lab00/images/fondvert.png")
img = cv2.resize(img, (1280, 720))
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# cv2.imshow("OG Image",img)
# cv2.imshow("HSV Image", hsvImg)

cv2.namedWindow("trackBars", cv2.WINDOW_NORMAL)
cv2.resizeWindow("trackBars", 400, 200)
cv2.createTrackbar("HLow","trackBars",0,179,placeholder)
cv2.createTrackbar("HHigh","trackBars",179,179,placeholder)
cv2.createTrackbar("SLow","trackBars",0,255,placeholder)
cv2.createTrackbar("SHigh","trackBars",255,255,placeholder)
cv2.createTrackbar("Vlow","trackBars",0,255,placeholder)
cv2.createTrackbar("VHigh","trackBars",255,255,placeholder)

while(1):
    HLow = cv2.getTrackbarPos("HLow","trackBars")
    HHigh = cv2.getTrackbarPos("HHigh","trackBars")
    SLow = cv2.getTrackbarPos("SLow","trackBars")
    SHigh = cv2.getTrackbarPos("SHigh","trackBars")
    Vlow = cv2.getTrackbarPos("Vlow","trackBars")
    VHigh = cv2.getTrackbarPos("VHigh","trackBars")

    binImage = cv2.inRange(hsvImg, (HLow, SLow, Vlow), (HHigh, SHigh, VHigh))
    cv2.imshow("Binary Image", binImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()