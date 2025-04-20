from sub import get_param_list
from time import sleep
import pyautogui

def press_button_b():
    pyautogui.moveTo(1000, 770, duration=0.2)# B級育成ボタン
    pyautogui.click()
def press_button_c():
    pyautogui.moveTo(1000 - 100, 770, duration=0.2)# C級育成ボタン
    pyautogui.click()
def press_button_not_save():
    pyautogui.moveTo(1000 - 100, 770, duration=0.1)# やめる
    pyautogui.click()
def press_button_save():
    pyautogui.moveTo(1000, 770, duration=0.1)# 保存
    pyautogui.click()

for i in range(5):# 100個使っても0.32%しか上昇しないので注意
    print("======================")
    press_button_c()
    print("C級育成")
    sleep(0.1)
    param_list = None
    while param_list == None:
        try:
            param_list = get_param_list()
        except:
            print("パラメータ取得エラー")
    print(param_list)
    if param_list[0] + param_list[3] == 0 and param_list[0] > param_list[3]:# 合計がでもメインステータスがプラスなら保存
        print("保存(メインステータス優先)")
        press_button_save()
    elif param_list[0] + param_list[3] > 0:# 合計が正なら保存
        print("保存")
        press_button_save()
    else:
        print("やめる")
        press_button_not_save()
