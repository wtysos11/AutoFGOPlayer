from PIL import Image
import pyautogui
import os
import time

from autoPlayer import *
AvailableRegion = (44,29,1791,1009)
pyautogui.PAUSE = 3

player = autoPlayer((44,29),(1835,1038))
for i in range(1000):
    #赝作，终本刷伪手稿
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
    #通过选人界面，进入第一面。第一面大英雄三技能，CEO二技能，宝具。
    while not player.checkBattleAvailable():
        time.sleep(1)
    
    pyautogui.PAUSE = 5
    time.sleep(3)
    player.chooseServentSkill(0,2)
    player.chooseServentSkill(2,1)
    player.chooseServentSkill(2,0)
    time.sleep(2)
    player.InBattle()
    pyautogui.PAUSE = 0.5
    player.InBattlePhantasm(0)
    player.InBattleAttack(0)
    player.InBattleAttack(1)
    pyautogui.PAUSE = 3
    
    time.sleep(5)
    pyautogui.click(196,491)
    pyautogui.click(196,491)


    #通过选人界面，进入第二面。孔明上场，孔明一二三技能给茶茶，换人礼装换上船长，CEO开一三技能
    while not player.checkBattleAvailable():
        time.sleep(1)
    
    pyautogui.PAUSE = 5
    time.sleep(3)

    player.chooseServentSkill(0,1)
    player.chooseServentSkill(0,2)
    player.chooseServentSkillWithSpecificAim(0,0,1)

    player.chooseMasterSkill(2)
    pyautogui.PAUSE = 1
    player.changePeopleSkill(0,3)
    pyautogui.PUASE = 5
    time.sleep(2)

    player.chooseServentSkill(2,2)
    time.sleep(1)
    pyautogui.PAUSE = 3

    player.InBattle()
    pyautogui.PAUSE = 0.5
    player.InBattlePhantasm(1)
    player.InBattleAttack(0)
    player.InBattleAttack(1)
    pyautogui.PAUSE = 3

    inBattle3 = False
    #检查是否进入第三面
    #通过选人界面，进入第三面。船长一三技能，茶茶三技能，御主礼装一技能。
    while not inBattle3:
        while not player.checkBattleAvailable():
            time.sleep(1)
        
        time.sleep(2)
        try:
            location = pyautogui.locateOnScreen('battle_check.png',confidence = 0.94)
            player.InBattle()
            pyautogui.PAUSE = 0.5
            player.InBattleAttack(0)
            player.InBattleAttack(1)
            player.InBattleAttack(2)
            pyautogui.PAUSE = 3
            continue
        except:
            inBattle3 = True
    
    time.sleep(3)
    pyautogui.PAUSE = 5
    player.chooseEnemy(1)
    player.chooseServentSkill(0,0)
    player.chooseServentSkill(0,2)
    player.chooseServentSkill(1,2)
    player.chooseMasterSkill(0)
    pyautogui.PAUSE = 3
    
    player.InBattle()
    pyautogui.PAUSE = 0.5
    player.InBattlePhantasm(0)
    player.InBattlePhantasm(2)
    player.InBattleAttack(0)
    pyautogui.PAUSE = 3
    time.sleep(45)
    pyautogui.click(196,491)
    pyautogui.click(196,491)
    #第三面结束，进入结算界面
    # 判断是否进入结算界面，如果没有进入结算界面，循环使用一二三技能直到结束
    print('Check battle available')
    while player.checkBattleAvailable():
        print('not available')
        time.sleep(2)
        player.InBattle()
        pyautogui.PAUSE = 1
        player.InBattleAttack(0)
        player.InBattleAttack(1)
        player.InBattleAttack(2)
        time.sleep(8)
        pyautogui.click(196,491)
        pyautogui.click(196,491)
        time.sleep(2)
        pyautogui.click(196,491)
        time.sleep(5)
    
    print('available or over')
    pyautogui.PAUSE = 1.5
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    time.sleep(3)
    pyautogui.click(1538,958)
    time.sleep(15)