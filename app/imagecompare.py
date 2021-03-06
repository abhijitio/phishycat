#import ImageChops
#import Image
#im1 = Image.open("image1.jpg")
#im2 = Image.open("image2.jpg")
#diff= ImageChops.difference(im1, im2)

#def equal(im1, im2):
 #return ImageChops.difference(im1, im2).getbbox()

import sys

from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average

def main(file1, file2):
    #file1, file2 = sys.argv[1:1+2]
    # read images as 2D arrays (convert to grayscale for simplicity)
    img1 = to_grayscale(imread(file1).astype(float))
    #print img1
    img2 = to_grayscale(imread(file2).astype(float))
    # compare
    n_m, n_0 = compare_images(img1, img2)
    if n_m/img1.size==0:
        if n_0*1.0/img1.size==0:
            return n_m/img1.size
    return "Not Norm Return" # Need to change
    #return n_m/img1.size
    #print "Manhattan norm:", n_m, "/ per pixel:", n_m/img1.size
    #print "Zero norm:", n_0, "/ per pixel:", n_0*1.0/img1.size

def compare_images(img1, img2):
    # normalize to compensate for exposure difference
    img1 = normalize(img1)
    img2 = normalize(img2)
    # calculate the difference and its norms
    diff = img1 - img2  # elementwise for scipy arrays
    m_norm = sum(abs(diff))  # Manhattan norm
    z_norm = norm(diff.ravel(), 0)  # Zero norm
    return (m_norm, z_norm)

def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

if __name__ == "__main__":
    main()
