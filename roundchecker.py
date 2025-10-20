import pytesseract
from pytesseract import Output
from PIL import Image
import cv2

img = Image.open("screenshot.png")
w, h = img.size

region = img.crop((int(w * 0.7), int(h * 0.0), int(w * 0.95), int(h * 0.15)))
region.save("round_region.png")


img = cv2.imread("round_region.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.bitwise_not(gray)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

config = "--psm 7 -c tessedit_char_whitelist=0123456789/"

text = pytesseract.image_to_string(gray, config=config)
text = text.strip()

print("text:", repr(text))