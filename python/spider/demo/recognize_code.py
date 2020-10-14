import os

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

count_failure = 0
for img in os.listdir('codes'):
    img_path = os.path.join('codes', img)
    name = pytesseract.image_to_string(Image.open(img_path))
    name = ''.join([i for i in name if i and i not in [':', '\n', ' ', '"', '\'']])
    if not name:
        count_failure += 1
        name = f'没认出{count_failure}'
    print(name)
    if not os.path.exists(f'codes\\{name}.png'):
        os.rename(img_path, f'codes\\{name}.png')
