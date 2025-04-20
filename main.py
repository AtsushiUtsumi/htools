import pyautogui
import pytesseract
from PIL import ImageGrab ,ImageOps

# Tesseractのパスを設定（Windows環境の場合）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# マウスの移動を安全に行うため、フェイルセーフを有効にする
pyautogui.FAILSAFE = True
# pyautogui.moveTo(1000, 770, duration=0.5)# B級育成ボタン
# pyautogui.click()
# pyautogui.moveTo(1180, 420, duration=0.5)

def get_text_at_cursor():
    # マウス位置の周辺（100x100ピクセル）をキャプチャ
    x, y = pyautogui.position()
    screenshot = ImageGrab.grab(bbox=(x-0, y-25, x+150, y+25))

    screenshot.save('screenshot.png')  # デバッグ用にスクリーンショットを保存
    
    # 画像から文字列を抽出（日本語対応）
    text = pytesseract.image_to_string(screenshot, lang='jpn')
    return text.strip()

# 「0」は真っ黒、「255」は真っ白

def convert_to_black(image):
    # 高めの閾値を設定し、ほぼ白に近い色以外を黒に変換
    return image.point(lambda x: 255 if x >= 246 else 0)

def convert_to_white(image):
    return image.point(lambda x: 0 if x < 250 else 255)

# カーソル移動
# pyautogui.moveTo(1000, 770, duration=0.5)  # B級育成ボタン
# テキスト抽出と表示
text = get_text_at_cursor()
#print(f"抽出されたテキスト: {text}")

screenshot = ImageGrab.grab(bbox=(1000, 750, 1100, 800))# B級育成ボタン
screenshot = ImageGrab.grab(bbox=(1140, 520, 1180, 540))# 体力値
screenshot = ImageOps.invert(screenshot)# 白黒反転
screenshot.save('screenshot.png')  # デバッグ用にスクリーンショットを保存
text = pytesseract.image_to_string(screenshot, output_type=pytesseract.Output.STRING)
print('テキスト:' + text)