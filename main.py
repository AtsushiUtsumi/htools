from sub import get_param_list
from time import sleep
import pyautogui
# 画面のボタンの座標は「.env」に移すこと
# ボタンの押下はメソッド化してテストしやすくすること

mode = 'C'
count = 10# 何回育成するか
primary_param_index = 0# メインステータスのインデックス
secondary_param_index = 3# サブステータスのインデックス

import sys
args = sys.argv

if len(args) != 4:
    print("引数の数が違います")
    print("引数1: B or C")
    print("引数2: 育成回数")
    print("引数3: メインステータスのインデックス")
    exit(0)
mode = args[1]
count = int(args[2])
primary_param_index = int(args[3])

def press_button_b():
    print("B級育成")
    pyautogui.moveTo(1000, 770, duration=0.2)# B級育成ボタン
    sleep(0.1)
    pyautogui.click()
def press_button_c():
    print("C級育成")
    pyautogui.moveTo(1000 - 100, 770, duration=0.2)# C級育成ボタン
    sleep(0.1)
    pyautogui.click()

def press_button_not_save():
    pyautogui.moveTo(820, 770, duration=0.2)# やめる
    pyautogui.click()
def press_button_save():
    pyautogui.moveTo(1060, 770, duration=0.2)# 保存
    pyautogui.click()

save_count = 0
not_save_count = 0
change_list = [0, 0, 0, 0]# ステータスの変化量を記録するリスト

for i in range(count):# 100個使っても0.32%しか上昇しないので注意
    print("\n======================< " + str(i + 1) + "/" + str(count) + " >======================")
    if mode == "B":
        press_button_b()
    elif mode == "C":
        press_button_c()
    param_list = get_param_list()
    print(param_list)
    if param_list[primary_param_index] + param_list[secondary_param_index] == 0 and param_list[primary_param_index] > param_list[secondary_param_index]:# 合計がでもメインステータスがプラスなら保存
        print("保存(メインステータス優先)")
        save_count += 1
        for i in range(len(param_list)):change_list[i] += param_list[i]
        press_button_save()
    elif param_list[primary_param_index] + param_list[secondary_param_index] > 0:# 合計が正なら保存
        print("保存")
        save_count += 1
        for i in range(len(param_list)):change_list[i] += param_list[i]
        press_button_save()
    else:
        print("やめる")
        not_save_count += 1
        press_button_not_save()
    print("保存回数: " + str(save_count) + " / やめた回数: " + str(not_save_count) + " / 合計: " + str(save_count + not_save_count))
    print("ステータスの変化量: " + str(change_list))
