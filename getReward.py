# 无限池奖池抽取
from PIL import Image
import pyautogui
import os
import time

from autoPlayer import *
AvailableRegion = (44,29,1791,1009)
pyautogui.PAUSE = 1

#抽取奖池的数量，默认奖池没有抽取
for i in range(6):
    #点击奖池兑换按钮
    pyautogui.click(609,687)
    for j in range(29):
        for k in range(4):
            pyautogui.click(600,610)
        
        try:
            location = pyautogui.locateOnScreen('over.png',confidence = 0.8)
            break
        except:
            continue
    pyautogui.click(1590,373)
    pyautogui.click(1242,815)
    time.sleep(2)
    pyautogui.click(1001,832)