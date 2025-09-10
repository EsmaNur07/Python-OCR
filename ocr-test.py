import cv2
import pytesseract
from PIL import Image, ImageEnhance

img_file = 'data/biruni.jpg'
img = cv2.imread(img_file)

inverted_img = cv2.bitwise_not(img)
cv2.imwrite("temp/inverted_img.png", inverted_img)

img = Image.open("temp/inverted_img.png")
img.show()