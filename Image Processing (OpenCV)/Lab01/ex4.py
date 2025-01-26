import cv2
import numpy as np

# Function to draw the polygon
def draw_polygon(event, x, y, flags, param):
    global points, drawing, img_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        img_copy = img.copy()
        cv2.polylines(img_copy, [np.array(points)], False, (0, 255, 0), 2)
        cv2.imshow('image', img_copy)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.polylines(img_copy, [np.array(points)], False, (0, 255, 0), 2)
        cv2.imshow('image', img_copy)

# Load the image
img = cv2.imread('images/winxp.webp')
img = cv2.resize(img, (1080, 720))
img_copy = img.copy()
points = []
drawing = False

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_polygon)

while True:
    cv2.imshow('image', img_copy)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        mask = np.zeros((1080, 720), dtype=np.uint8)
        cv2.fillPoly(mask, [np.array(points)], 255)
        cv2.imshow('mask', mask)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        img[mask == 0] = gray_bgr[mask == 0]
        cv2.imshow('result', img)
        cv2.waitKey(0)
        break

cv2.destroyAllWindows()