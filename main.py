from PIL import Image
import pyautogui
import os
import time

from autoPlayer import *
AvailableRegion = (44,29,1791,1009)
pyautogui.PAUSE = 3

player = autoPlayer((44,29),(1835,1038))
for i in range(9):
    #点击外层关卡。凶骨关卡：第一章冬木x-g，15ap一把
    location = pyautogui.locateOnScreen('aim.png',confidence = 0.95)
    pyautogui.click(pyautogui.center(location))
    #通过过度界面，进入选人界面
    ## 检查选人界面是否正常
    while not player.checkChooseHelp():
        print("checking")
        time.sleep(1)
    
    print("Pass")
    #player.findAddServant()
    pyautogui.click(440,409)
    player.beginMission()
    #通过选人界面，进入第一面
    while not player.checkBattleAvailable():
        time.sleep(1)
    
    time.sleep(3)
    player.chooseServentSkill(2,0)
    player.chooseServentSkill(2,1)
    time.sleep(1)
    player.InBattle()
    player.InBattlePhantasm(2)
    player.InBattleAttack(0)
    player.InBattleAttack(1)
    
    #通过选人界面，进入第二面
    while not player.checkBattleAvailable():
        time.sleep(1)
    
    time.sleep(3)
    player.chooseServentSkill(1,0)
    player.chooseServentSkill(1,1)
    time.sleep(1)
    player.InBattle()
    player.InBattlePhantasm(1)
    player.InBattleAttack(0)
    player.InBattleAttack(1)
    #通过选人界面，进入第三面
    while not player.checkBattleAvailable():
        time.sleep(1)
    
    time.sleep(3)
    player.chooseServentSkill(0,1)
    time.sleep(1)
    player.InBattle()
    player.InBattlePhantasm(0)
    player.InBattleAttack(0)
    player.InBattleAttack(1)
    time.sleep(35)
    #第三面结束，进入结算界面
    pyautogui.PAUSE = 1.5
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    time.sleep(3)
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    time.sleep(10)