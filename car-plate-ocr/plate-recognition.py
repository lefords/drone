import cv2
import pytesseract
import os
import sys

# === НАСТРОЙКА TESSERACT ===
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'D:\Tesseract\tessdata'

# Получаем путь к изображению из аргумента командной строки
if len(sys.argv) < 2:
    print("❌ Использование: python script.py <путь_к_изображению>")
    exit()

img_path = sys.argv[1]

if not os.path.isfile(img_path):
    print(f"❌ Файл '{img_path}' не найден.")
    exit()

img = cv2.imread(img_path)
if img is None:
    print("❌ Не удалось загрузить изображение.")
    exit()

# Простая предобработка
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Распознавание текста
config = '--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?@#$%&*()[]{}<>+-='
text = pytesseract.image_to_string(thresh, config=config, lang='eng')

print("✅ Распознано:")
print(text.strip())

# Показываем результат
cv2.imshow("Изображение", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()