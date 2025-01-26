import numpy as np
import cv2

def histogram_specification(img, ref):
    # Get the histogram of the input image
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()

    # Get the histogram of the reference image
    hist_ref, bins_ref = np.histogram(ref.flatten(), 256, [0, 256])
    cdf_ref = hist_ref.cumsum()
    cdf_normalized_ref = cdf_ref * float(hist_ref.max()) / cdf_ref.max()

    # Create the mapping function
    mapping = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        j = 255
        while j >= 0 and cdf_normalized_ref[j] > cdf_normalized[i]:
            j -= 1
        mapping[i] = j

    # Apply the mapping function to the input image
    img_spec = mapping[img]

    return img_spec

def main():
    img = cv2.imread('images/sunset1.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (1080, 720))
    ref = cv2.imread('images/sunset2.jpg', cv2.IMREAD_GRAYSCALE)
    ref = cv2.resize(ref, (1080, 720))

    img_spec = histogram_specification(img, ref)

    cv2.imshow('Original Image', img)
    cv2.imshow('Reference Image', ref)
    cv2.imshow('Specified Image', img_spec)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()