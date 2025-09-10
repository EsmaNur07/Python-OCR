import cv2
import pytesseract
from PIL import Image, ImageEnhance

img_file = 'data/biruni.jpg'
img = cv2.imread(img_file)

cv2.imshow('image', img)
cv2.waitKey(0)