import pytesseract
from PIL import Image
import pyocr
import pyocr.builders

class charRec:
    def __init__(self):
        self.img = Image.open("screenshot.png").convert("RGB")

    def Convert(self):
        width,height = self.img.size
        for x in range(width):
            for y in range(height):
                r, g, b = self.img.getpixel((x,y))

                if r >= 59 and g >= 59 and b >= 59:
                    self.img.putpixel((x,y),(255,255,255))

        self.img.save("screenshot2.png")

    def imgText(self):
        return pytesseract.image_to_string(self.img, lang="eng")

image = charRec()
image.Convert()
result = image.imgText()
print("結果:" + result)


from PIL import Image
import pyocr
import pyocr.builders
import sys

file_path = 'screenshot2.png'
# ツール読み込み
tools = pyocr.get_available_tools()
# ツールが見付からない場合
if len(tools) == 0:
    print('pyocrが見付かりません。pyocrをインストールして下さい。')
    sys.exit(1)
tool = tools[0]
# 画像読み込み
img_org = Image.open(file_path)
# 枚数表記部分を切り取り
#max_medals_img = img_org.crop((0, 0, 45, 15))
# OCR
max_medals = tool.image_to_string(img_org , lang='eng', builder=pyocr.builders.DigitBuilder(tesseract_layout=6))
print(f'max_medals：{max_medals}')