from sub import get_param_list
from time import sleep
import pyautogui
# 画面のボタンの座標は「.env」に移すこと
# ボタンの押下はメソッド化してテストしやすくすること
def press_button_b():
    print("B級育成")
    pyautogui.moveTo(1000, 770, duration=0.2)# B級育成ボタン
    pyautogui.click()
    sleep(0.2)
def press_button_c():
    print("C級育成")
    pyautogui.moveTo(1000 - 100, 770, duration=0.2)# C級育成ボタン
    pyautogui.click()
    sleep(0.17)
def press_button_not_save():
    pyautogui.moveTo(1000 - 100, 770, duration=0.1)# やめる
    pyautogui.click()
def press_button_save():
    pyautogui.moveTo(1000, 770, duration=0.1)# 保存
    pyautogui.click()
    sleep(0.2)

count = 100
save_count = 0
not_save_count = 0

for i in range(count):# 100個使っても0.32%しか上昇しないので注意
    print("======================< " + str(i + 1) + "/" + str(count) + " >======================")
    press_button_c()
    param_list = None
    while param_list == None:
        try:
            param_list = get_param_list()
        except:
            print("パラメータ取得エラー")
    print(param_list)
    primary_param_index = 0# メインステータスのインデックス
    secondary_param_index = 3# サブステータスのインデックス
    if param_list[primary_param_index] + param_list[secondary_param_index] == 0 and param_list[primary_param_index] > param_list[secondary_param_index]:# 合計がでもメインステータスがプラスなら保存
        print("保存(メインステータス優先)")
        save_count += 1
        press_button_save()
    elif param_list[primary_param_index] + param_list[secondary_param_index] > 0:# 合計が正なら保存
        print("保存")
        save_count += 1
        press_button_save()
    else:
        print("やめる")
        not_save_count += 1
        press_button_not_save()
    print("保存回数: " + str(save_count) + " / やめた回数: " + str(not_save_count) + " / 合計: " + str(save_count + not_save_count))
