import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

LOG_IMAGE_PATH = '../images/expt_2/log_image.tif'
POWER_LAW_IMAGE1_PATH = '../images/expt_2/power_law_gamma_low.tif'
POWER_LAW_IMAGE2_PATH = '../images/expt_2/power_law_gamma_high.tif'

def readImage(imagePath):
    # read the image
    image_original = mpimg.imread(imagePath)
    image = image_original.copy() # else it is read only

    if len(image.shape) == 3:
        # is a color image
        # converting to grayscale: avg method
        R = image[:,:, 0]
        G = image[:,:, 1]
        B = image[:,:, 2]
        grayscale = (R/3 + G/3 + B/3)
    else:
        # is a grayscale image
        grayscale = np.array(image_original.copy())

    plt.imshow(grayscale, cmap='gray')
    plt.title('original gray image')
    
    return grayscale

# log s = c * log(1+r)
def logTransform(grayImage ,c):
    # needed to avoid log(1) = 0 error
    log_image = c * np.log10(grayImage + 1.0000000000001) 
    plt.imshow(log_image, cmap='gray')
    plt.title('log transform with c = ' + str(c))

# power law s = c * r^(gamma)
def powerLawTransform(grayImage, c, gamma):
    power_image = c * np.power(grayImage, gamma)
    plt.imshow(power_image, cmap='gray')
    plt.title('log transform with c = '+ str(c) + ' & gamma = ' + str(gamma))

