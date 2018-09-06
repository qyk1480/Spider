from pytesseract import image_to_string
from PIL import Image

image = Image.open('captcha.jpg')
text = image_to_string(image)
print(text)
