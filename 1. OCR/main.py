import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Jooney Han\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def recognize_numbers(image_path):
    with Image.open(image_path) as img:
        result = pytesseract.image_to_string(img, config='--psm 6 outputbase digits')
        return result.strip()

image_path = r'C:\Users\Jooney Han\Desktop\KMCAP\images'

for i in range(100):
    recognized_numbers = recognize_numbers(os.path.join(image_path, f'{i}.png'))
    print("Recognized Numbers for", i, ":", recognized_numbers)
