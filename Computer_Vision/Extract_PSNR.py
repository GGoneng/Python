"""
03.
Student ID : 21920141
Name       : 이민하
Subject    : Computer Vision
Function   : Extract PSNR by Original RGB Image and Recovery RGB Image
"""

# Import Modules
import numpy as np
import cv2 as cv
import time
import math

# Create a function that sets the Image
def set_path(file_name):
    # Set a File Path
    FILE_PATH = "./Data/"
    imgfile = FILE_PATH + file_name

    # Read a Image File
    img = cv.imread(imgfile, cv.IMREAD_COLOR)

    return img


# Create a function that shows the image
def show_image(img_file):
    # Resize the Image Window
    img = cv.resize(img_file, dsize = (500, 300))

    # Show the Image Window
    cv.imshow("img_file", img_file)

    # To maintain the window opened
    cv.waitKey(0)


# Create a function that transform RGB to YCbCr (SDTV Version)
def transform_rgb_to_ycbcr_sdtv(rgb_img_file):
    # Make a empty numpy array
    ycbcr = np.zeros(rgb_img_file.shape, dtype = np.uint8)

    # Transform the Image RGB to YCbCr
    for i, y in enumerate(rgb_img_file):
        for j, x in enumerate(y):
            red, green, blue = x

            # (SDTV Version Formula)
            y601 = 0.299 * red + 0.587 * green + 0.114 * blue 
            cb = -0.172 * red + -0.339 * green + 0.511 * blue + 128
            cr = 0.511 * red + -0.428 * green + -0.083 * blue + 128

            # Input YCbCr to empty array
            ycbcr[i][j] = [y601, cb, cr]

    return ycbcr

# Create a function that transform YCbCr to RGB (SDTV Version)
def transform_ycbcr_to_rgb_sdtv(ycbcr_img_file):
    # Make a empty numpy array
    rgb = np.zeros(ycbcr_img_file.shape, dtype = np.uint8)

    # Transform the Image YCbCr to RGB
    for i, y in enumerate(ycbcr_img_file):
        for j, x in enumerate(y):
            y601, cb, cr = x

            # (SDTV Version Formula)
            red = y601 + 1.371 * (cr - 128)
            green = y601 - 0.698 * (cr - 128) - 0.336 * (cb - 128)
            blue = y601 + 1.732 * (cb - 128)

            # Input RGB to empty array
            rgb[i][j] = [red, green, blue]

    return rgb

# Create a function that transform RGB to YCbCr (HDTV Version)
def transform_rgb_to_ycbcr_hdtv(rgb_img_file):
    # Make a empty numpy array
    ycbcr = np.zeros(rgb_img_file.shape, dtype = np.uint8)

    # Transform the Image RGB to YCbCr
    for i, y in enumerate(rgb_img_file):
        for j, x in enumerate(y):
            red, green, blue = x

            # (HDTV Version Formula)
            y709 = 0.213 * red + 0.715 * green + 0.072 * blue 
            cb = -0.117 * red + -0.394 * green + 0.511 * blue + 128
            cr = 0.511 * red + -0.464 * green + -0.047 * blue + 128

            # Input YCbCr to empty array
            ycbcr[i][j] = [y709, cb, cr]

    return ycbcr


# Create a function that transform YCbCr to RGB (HDTV Version)
def transform_ycbcr_to_rgb_hdtv(ycbcr_img_file):
    # Make a empty numpy array
    rgb = np.zeros(ycbcr_img_file.shape, dtype = np.uint8)

    # Transform the Image YCbCr to RGB
    for i, y in enumerate(ycbcr_img_file):
        for j, x in enumerate(y):
            y709, cb, cr = x

            # (HDTV Version Formula)
            red = y709 + 1.54 * (cr - 128)
            green = y709 - 0.459 * (cr - 128) - 0.183 * (cb - 128)
            blue = y709 + 1.816 * (cb - 128)

            # Input RGB to empty array
            rgb[i][j] = [red, green, blue]

    return rgb


# Create a function that transform RGB to YCbCr (OpenCV Version)
def transform_rgb_to_ycbcr_cv(rgb_img_file):
    ycbcr = cv.cvtColor(rgb_img_file, cv.COLOR_RGB2YCrCb)

    return ycbcr

# Create a function that transform YCbCr to RGB (OpenCV Version)
def transform_ycbcr_to_rgb_cv(ycbcr_img_file):
    rgb = cv.cvtColor(ycbcr_img_file, cv.COLOR_YCrCb2RGB)

    return rgb

# Create a function that extract Y Channel (= Gray Scale)
def extract_y_channel(ycbcr_img):
    # Make a empty numpy array
    y_channel = np.zeros(ycbcr_img.shape[:-1], dtype = np.uint8)

    # Extract Y Channel and Input Y to empty array
    for i, y in enumerate(ycbcr_img):
        for j, x in enumerate(y):   
            y601, cb, cr = x
            y_channel[i][j] = y601

    return y_channel

# Create a function that extract Mean Squared Error
def getMSE(rgb_img_file1, rgb_img_file2):
    # Make a MSE variable
    redMSE = 0
    greenMSE = 0
    blueMSE = 0

    # Get MSE by each pixel
    for i, y in enumerate(rgb_img_file1):
        for j, x in enumerate(y):
            red_1, green_1, blue_1 = x

            red_2 = rgb_img_file2[i][j][0]
            green_2 = rgb_img_file2[i][j][1]
            blue_2 = rgb_img_file2[i][j][2]

            redMSE += (np.float64(red_1) - np.float64(red_2)) ** 2
            greenMSE += (np.float64(green_1) - np.float64(green_2)) ** 2
            blueMSE += (np.float64(blue_1) - np.float64(blue_2)) ** 2
    
    N = rgb_img_file1.shape[0] * rgb_img_file1.shape[1]
    
    totalMSE = (redMSE + greenMSE + blueMSE) / (3 * N)

    return totalMSE

# Create a function that extract PSNR
def getPSNR(totalMSE):
    # Define a MAX (RGB = 255 * 3)
    MAX = 255

    # Get PSNR
    PSNR = 10 * math.log10(MAX ** 2 / totalMSE)

    return PSNR


# Main Funciton
if __name__ == "__main__":

    # Set a File Path
    rgb_img = set_path("test.jpg")   

    # Transform the Image file (SDTV Version)
    sdtv_ycbcr_img = transform_rgb_to_ycbcr_sdtv(rgb_img)
    sdtv_y_img = extract_y_channel(sdtv_ycbcr_img)
    sdtv_rgb_img = transform_ycbcr_to_rgb_sdtv(sdtv_ycbcr_img)

    # Transform the Image file (HDTV Version)
    hdtv_ycbcr_img = transform_rgb_to_ycbcr_hdtv(rgb_img)
    hdtv_y_img = extract_y_channel(hdtv_ycbcr_img)
    hdtv_rgb_img = transform_ycbcr_to_rgb_hdtv(hdtv_ycbcr_img)

    # Transform the Image file (OpenCV Version)
    cv_ycbcr_img = transform_rgb_to_ycbcr_cv(rgb_img)
    cv_y_img = extract_y_channel(cv_ycbcr_img)
    cv_rgb_img = transform_ycbcr_to_rgb_cv(cv_ycbcr_img)

    # Measure the Start Time
    t1 = time.time()

    # Print PSNR implemented by custom function (SDTV)
    print(f"PSNR implemented by function (sdtv_rgb_img) : {getPSNR(getMSE(rgb_img, sdtv_rgb_img)):.4f}")

    # Measure the Finish Time
    t2 = time.time()
    
    # Print PSNR implemented by custom function (HDTV)
    print(f"PSNR implemented by function (hdtv_rgb_img) : {getPSNR(getMSE(rgb_img, hdtv_rgb_img)):.4f}")

    # Print PSNR implemented by custom function (OpenCV)
    print(f"PSNR implemented by function (cv_rgb_img) : {getPSNR(getMSE(rgb_img, cv_rgb_img)):.4f}")

    # Print Custom function's operation time
    print(f"manual_time : {t2 - t1:.4f}")


    # Measure the Start Time
    t1 = time.time()

    # Print PSNR implemented by formula function (SDTV)
    print(f"PSNR implemented by formula (sdtv_rgb_img) : {cv.PSNR(rgb_img, sdtv_rgb_img):.4f}")

    # Measure the Finish Time
    t2 = time.time()
    
    # Print PSNR implemented by formula function (HDTV)
    print(f"PSNR implemented by formula (hdtv_rgb_img) : {cv.PSNR(rgb_img, hdtv_rgb_img):.4f}")

    # Print PSNR implemented by formula function (OpenCV)
    print(f"PSNR implemented by formula (cv_rgb_img) : {cv.PSNR(rgb_img, cv_rgb_img):.4f}")

    # Print formula function's operation time
    print(f"opencv_time : {t2 - t1:.4f}")
