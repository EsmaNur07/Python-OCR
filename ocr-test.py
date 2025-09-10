import cv2
import pytesseract
from PIL import Image, ImageEnhance

img_file = 'data/bozuk_belge.png'
img = cv2.imread(img_file)

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = grayscale(img)
cv2.imwrite("temp/gray_image.png", gray_image)

img = Image.open("temp/gray_image.png")
img.show()