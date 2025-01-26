import numpy as np
import cv2

cv2.namedWindow('Ex1:', 1)

img = cv2.imread('images/fondvert.png',1)
img = cv2.resize(img, (1080,720))

def getColor(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            x1, y1 = max(0, x-7), max(0, y-7)
            x2, y2 = min(img.shape[1], x+7), min(img.shape[0], y+7)
            
            lower = np.array([img_hsv[y1, x1, 0], img_hsv[y1, x1, 1], img_hsv[y1, x1, 2]])
            upper = np.array([img_hsv[y2, x2, 0], img_hsv[y2, x2, 1], img_hsv[y2, x2, 2]])

            mask = cv2.inRange(img_hsv, lower, upper)
            cv2.imshow("Ex1:",mask)
        
def main():
    cv2.imshow('Ex1:', img)
    cv2.setMouseCallback('Ex1:', getColor)
    
    while True:
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
        
    
if __name__ == "__main__":
    main()
    