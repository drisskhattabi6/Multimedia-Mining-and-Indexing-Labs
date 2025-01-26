import cv2
import numpy as np
import sys

def apply_gabor_filters(img, filters):
    feat = []
    for kernel in filters:
        filtered = cv2.filter2D(img, cv2.CV_8UC3, kernel)
        feat.append(filtered)
    return feat

def main():
    img = cv2.imread(f"Lab02/images/{sys.argv[1]}.jpg", cv2.IMREAD_GRAYSCALE)
    # img = cv2.resize(img, (500,500))
    roi = cv2.selectROI(f"Image {sys.argv[1]}.jpg", img)
    sample = img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
    
    ksize = 11
    lambd = np.pi/4
    gamma = 0.15
    psi = 0
    
    filters = []
    for theta in (0, np.pi/4, np.pi/2, 3*np.pi/4):
        for sigma in (3, 4, 5):
            kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, psi, ktype=cv2.CV_32F)
            filters.append(kernel)
    
    sampleFeats = apply_gabor_filters(sample, filters)
    print(sampleFeats)
    imgFeats = apply_gabor_filters(img, filters)
    
    res = np.zeros_like(img)
    sample_stats = [np.mean(f) for f in sampleFeats]
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pixelFeats = [f[i,j] for f in imgFeats]
            diff = np.mean(np.abs(np.array(pixelFeats) - np.array(sample_stats)))
            res[i,j] = 255 if diff < 45 else 0

    cv2.imshow("result", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return res

if __name__ == "__main__":
    main()