from PIL import Image, ImageGrab
import pyocr
import pyocr.builders
from time import sleep
import sys

# パラメータを取得する関数
def _get_param_list():
    range_x_min = 1150
    range_x_max = 1175
    screenshot = ImageGrab.grab(bbox=(range_x_min, 420, range_x_max, 440))# 筋力値
    screenshot.save('筋力.png')
    screenshot = ImageGrab.grab(bbox=(range_x_min, 455, range_x_max, 475))# 敏捷値
    screenshot.save('敏捷.png')
    screenshot = ImageGrab.grab(bbox=(range_x_min, 488, range_x_max, 508))# 知力値
    screenshot.save('知力.png')
    screenshot = ImageGrab.grab(bbox=(range_x_min, 520, range_x_max, 540))# 体力値
    screenshot.save('体力.png')
    return [
        get_param_from_file('筋力.png'),
        get_param_from_file('敏捷.png'),
        get_param_from_file('知力.png'),
        get_param_from_file('体力.png')
            ]

def get_param_list():
    ERROR_COUNT = 5
    count = 0
    sleep(0.2)
    param_list = None
    while param_list == None:
        try:
           param_list = _get_param_list()
        except:
            count += 1
            print(f"パラメータ取得エラー({count}回目)")
            if count >= ERROR_COUNT:
                print(f"パラメータ取得{ERROR_COUNT}回失敗したので終了します")
                exit(0)
            sleep(1)
    return param_list

def get_param_from_file(file_path):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print('pyocrが見付かりません。pyocrをインストールして下さい。')
        sys.exit(1)
    tool = tools[0]
    # 画像読み込み
    img_org = Image.open(file_path)
    rgb = img_org.getpixel((1, 1))

    plus = 1# 符号
    if rgb[0] > rgb[1]:# 赤が強い場合はマイナス
        plus = -1
    value = tool.image_to_string(img_org , lang='eng', builder=pyocr.builders.DigitBuilder(tesseract_layout=6))
    if value[0] == '4' and plus > 0:# プラスの符号を「4」と誤認する場合があるので、「4」始まりかつ緑色の場合は先頭の「4」を削除する
        ret = abs(int(value[1:])) * plus
        print(file_path + " : " + str(ret))
        return ret
    else:
        ret = abs(int(value)) * plus
        print(file_path + " : " + str(ret))
        return ret
