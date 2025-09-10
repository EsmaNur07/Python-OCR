import cv2
import pytesseract
from PIL import Image, ImageEnhance

img_file = 'data/Turkish_Technic.png'
img = cv2.imread(img_file)

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_turkishT = grayscale(img)
cv2.imwrite("temp/gray_turkishT.png", gray_turkishT)

thresh, im_blackNwhite3 = cv2.threshold(gray_turkishT, 128, 255, cv2.THRESH_BINARY)
cv2.imwrite("temp/blackNwhite3.jpg", im_blackNwhite3)

img = Image.open("temp/blackNwhite3.jpg")
img.show() 