from PIL import Image
import pyautogui
import os
import time

from autoPlayer import *
AvailableRegion = (44,29,1791,1009)
pyautogui.PAUSE = 3

player = autoPlayer((44,29),(1835,1038))
for i in range(1000):
    #赝作，剑本刷手稿。一面大英雄，二面黑杯小黑，三面1宝弓凛+1宝特总
    location = pyautogui.locateOnScreen('aim.png',confidence = 0.8)
    pyautogui.click(pyautogui.center(location))
    #检查是否需要苹果
    flag = player.checkAP()
    #通过过度界面，进入选人界面
    ## 检查选人界面是否正常
    while not player.checkChooseHelp():
        print("checking")
        time.sleep(1)
    
    print("Pass")
    player.findAddServant()
    time.sleep(2)
    #pyautogui.click(440,409)
    player.beginMission()
    #通过选人界面，进入第一面。第一面大英雄三技能，宝具
    while not player.checkBattleAvailable():
        time.sleep(1)
    
    time.sleep(3)
    player.chooseServentSkill(0,2)
    time.sleep(2)
    player.InBattle()
    pyautogui.PAUSE = 0.5
    player.InBattlePhantasm(0)
    player.InBattleAttack(0)
    player.InBattleAttack(1)
    pyautogui.PAUSE = 3
    
    #通过选人界面，进入第二面。孔明上场，孔明一二三技能给小黑，小黑自冲，二三技能。弓凛三技能
    while not player.checkBattleAvailable():
        time.sleep(1)
    
    pyautogui.PAUSE = 5
    time.sleep(3)
    player.chooseServentSkill(0,1)
    player.chooseServentSkill(0,2)
    player.chooseServentSkillWithSpecificAim(0,0,1)
    player.chooseServentSkill(1,1)
    player.chooseServentSkill(1,2)
    player.chooseServentSkill(2,2)
    time.sleep(1)
    pyautogui.PAUSE = 3
    player.InBattle()
    pyautogui.PAUSE = 0.5
    player.InBattlePhantasm(1)
    player.InBattleAttack(0)
    player.InBattleAttack(1)
    pyautogui.PAUSE = 3
    #通过选人界面，进入第三面。换人礼装将孔明与特总对换。
    while not player.checkBattleAvailable():
        time.sleep(1)
    
    time.sleep(3)
    pyautogui.PAUSE = 5
    player.chooseMasterSkill(2)
    player.changePeopleSkill(0,3)
    time.sleep(2)
    player.chooseServentSkill(0,2)
    player.chooseServentSkill(2,0)
    player.chooseServentSkill(2,1)
    time.sleep(2)
    player.chooseMasterSkill(0)
    pyautogui.PAUSE = 3
    
    player.InBattle()
    pyautogui.PAUSE = 0.5
    player.InBattlePhantasm(0)
    player.InBattlePhantasm(2)
    player.InBattleAttack(0)
    pyautogui.PAUSE = 3
    time.sleep(45)
    #第三面结束，进入结算界面
    # 判断是否进入结算界面，如果没有进入结算界面，循环使用一二三技能直到结束
    while player.checkBattleAvailable():
        player.InBattle()
        pyautogui.PAUSE = 0.5
        player.InBattleAttack(0)
        player.InBattleAttack(1)
        player.InBattleAttack(2)
        pyautogui.PAUSE = 3
        time.sleep(20)
    
    pyautogui.PAUSE = 1.5
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    time.sleep(3)
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    time.sleep(15)