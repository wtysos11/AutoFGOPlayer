from PIL import Image
import pyautogui
import os
import time

from autoPlayer import *
AvailableRegion = (44,29,1791,1009)
pyautogui.PAUSE = 3

player = autoPlayer((44,29),(1835,1038))
for i in range(5):
    #赝作，剑本刷手稿。一面大英雄，二面黑杯小黑，三面1宝弓凛+1宝特总
    pyautogui.click('aim.png')
    #通过过度界面，进入选人界面
    ## 检查选人界面是否正常
    while not player.checkChooseHelp():
        print("checking")
        time.sleep(1)
    
    print("Pass")
    player.findAddServant()
    #pyautogui.click(440,409)
    player.beginMission()
    #通过选人界面，进入第一面。第一面弓凛一技能，二技能，弓凛宝具
    while not player.checkBattleAvailable():
        time.sleep(1)
    
    time.sleep(3)
    player.chooseServentSkill(2,0)
    time.sleep(2)
    player.chooseServentSkill(2,1)
    time.sleep(1)
    player.InBattle()
    player.InBattlePhantasm(2)
    player.InBattleAttack(0)
    player.InBattleAttack(1)
    
    #通过选人界面，进入第二面。换下弓凛，阿福上场，一技能，三技能。梅林一技能。阿福宝具
    while not player.checkBattleAvailable():
        time.sleep(1)
    
    time.sleep(3)
    player.chooseMasterSkill(2)
    player.changePeopleSkill(2,3)
    time.sleep(3)
    player.chooseServentSkill(2,0)
    time.sleep(2)
    player.chooseServentSkill(2,2)
    time.sleep(2)
    player.chooseServentSkill(1,0)
    time.sleep(1)
    player.InBattle()
    player.InBattlePhantasm(2)
    player.InBattleAttack(0)
    player.InBattleAttack(1)
    #通过选人界面，进入第三面。梅林三技能给船长。船长一技能，三技能。船长宝具。
    while not player.checkBattleAvailable():
        time.sleep(1)
    
    time.sleep(3)
    player.chooseServentSkill(0,0)
    time.sleep(2)
    player.chooseServentSkill(0,2)
    time.sleep(2)
    player.chooseServentSkillWithSpecificAim(1,2,0)
    time.sleep(2)
    player.chooseMasterSkill(0)
    time.sleep(1)
    player.InBattle()
    player.InBattlePhantasm(0)
    player.InBattleAttack(0)
    player.InBattleAttack(1)
    time.sleep(25)
    #第三面结束，进入结算界面
    pyautogui.PAUSE = 1.5
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    time.sleep(3)
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    pyautogui.click(1538,958)
    time.sleep(15)