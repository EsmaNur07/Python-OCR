import cv2
import pytesseract
from PIL import Image, ImageEnhance

img_file = 'data/bozuk_belge.png'
img = cv2.imread(img_file)

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = grayscale(img)
cv2.imwrite("temp/gray_image.png", gray_image)

thresh, im_blackNwhite = cv2.threshold(gray_image, 200, 230, cv2.THRESH_BINARY)
cv2.imwrite("temp/blackNwhite.png", im_blackNwhite)

img = Image.open("temp/blackNwhite.png")
img.show() 