from PIL import Image
import pyautogui
import os
import time

#os.chdir('E:\\code\\myRepository\\AutoFGOPlayer')
from autoPlayer import *
AvailableRegion = (44,29,1791,1009)
pyautogui.PAUSE = 1

player = autoPlayer((44,29),(1835,1038))
#点击外层关卡
pyautogui.click('aim.png')
#通过过度界面，进入选人界面
## 检查选人界面是否正常
while not player.checkChooseHelp():
    print("checking")
    time.sleep(1)

print("Pass")
player.findAddServant()
player.beginMission()
#通过选人界面，进入第一面

#通过选人界面，进入第二面

#通过选人界面，进入第三面

#第三面结束，进入结算界面