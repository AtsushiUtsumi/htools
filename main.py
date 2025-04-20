from sub import get_param_list
from time import sleep
import pyautogui

def press_button_b():
    pyautogui.moveTo(1000, 770, duration=0.5)# B級育成ボタン
    pyautogui.click()
def press_button_not_save():
    pyautogui.moveTo(1000, 770, duration=0.5)# やめる
    #pyautogui.click()
def press_button_save():
    pyautogui.moveTo(1000, 770, duration=0.5)# 保存
    #pyautogui.click()

for i in range(1):
    press_button_b()
    print("B級育成")
    sleep(1)
    param_list = get_param_list()
    print(param_list)
    sleep(1)
    if param_list[0] + param_list[3] > 0:
        print("保存")
        press_button_save()
    else:
        print("やめる")
        press_button_not_save()
