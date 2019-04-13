import pyautogui
from PIL import Image
import time
import pyscreeze
#常量，用于参数指定的修正
originXL = 44
originXR = 1835
originYU = 29
originYD = 1038

class autoPlayer:
    def __init__(self,LeftUpPos,RightDownPos):
        '''
        负责脚本中与具体坐标相关的部分，根据初始化值缩放坐标
        初始化自动脚本，接受目标模拟器有效区域的左上点和右下点。（即FGO界面有颜色部分的最左上角和最右下角）
        具体数据：1920*1080分辨率下，夜神模拟器6.2.6.2 Android4,下任务栏不隐藏，左上角为44,29 ，右上角为1835,1038
        '''
        self.Left = LeftUpPos[0]
        self.Up = LeftUpPos[1]
        self.Right = RightDownPos[0]
        self.Down = RightDownPos[1]
        self.Width = self.Right-self.Left
        self.Height = self.Down-self.Up

    def findInImage(self,originImage,aimImage,confidence = 0.9):
        ''' 
        在aimImage中查找originImage（两者都是Image对象）
        置信度confidence表示允许的误差像素的占比
        如果找到了，则返回首个像素；不然，返回None
        不支持缩放查找        
        实现思路：
        首先进行逐像素比对，计算允许的误差像素个数，并对当前搜索环境中的误差像素个数进行累计，如果累计超过，则不可能匹配，直接跳出
        '''
        alInterval = 5
        allowCount = int(originImage.size[0] * originImage.size[1] *confidence)
        for y in range(aimImage.size[1]):
            for x in range(aimImage.size[0]):
                wrongCount = 0
                if x+originImage.width>aimImage.width or y+originImage.height>aimImage.height:
                    break

                for xx in range(originImage.size[0]):
                    for yy in range(originImage.size[1]):
                        oc = originImage.getpixel((xx,yy))
                        ac = aimImage.getpixel((x+xx,y+yy))
                        if x+xx >= aimImage.size[0] or y+yy >= aimImage.size[1]:
                            break
                        if abs(oc[0]-ac[0])>alInterval or abs(oc[1]-ac[1])>alInterval or abs(oc[2]-ac[2])>alInterval:
                            wrongCount += 1
                    if wrongCount >=allowCount:
                        break
                
                if wrongCount < allowCount:
                    return (x,y)
        
        return None

            

    def checkChooseHelp(self):
        '''
        检查是否进入选人界面
        如果是，返回true；反之，则返回false
        '''
        originXL= 663
        originYU = 30
        originXR = 1835
        originYD = 180
        compareImage = Image.open('ChooseHelper.png')
        shootImage = pyautogui.screenshot(region = (originXL,originYU,originXR-originXL,originYD-originYU))
        compareResult = self.findInImage(compareImage,shootImage)
        if not compareResult is None:
            return True
        else:
            return False
    
    def findAddServant(self):
        '''
        找带加成礼装的人，确认第一个人是否符合要求。是的话点击第一个，不然向下拖
        '''

        #截取指定区域
        out = False
        counting = 0
        while not out:
            try:
                location = pyautogui.locateOnScreen('aimServent.png',confidence = 0.8)
                pyautogui.click(pyautogui.center(location))
                out = True
            except pyscreeze.ImageNotFoundException:
                pyautogui.moveTo(115,767)
                pyautogui.drag(0,-248*2,1.5,button = 'left')
                counting += 1
                if counting > 5:
                    return False

        return True
    
    def clickFirstServent(self):
        pyautogui.click(834,423)
    
    def beginMission(self):
        pyautogui.click(1703,973)

    def checkBattleAvailable(self):
        try:
            location = pyautogui.locateOnScreen('battleAvailable.png',confidence = 0.9)
            return True
        except:
            return False

    def chooseServentSkill(self,serventNum,skillNum):
        '''
        点击第几号位的从者（0,1,2）
        第几个技能（0,1,2)
        '''
        serventDistance = 446
        skillDistance = 131
        baseX = 136 #第0号从者，第0号技能
        baseY = 833

        realX = baseX + serventDistance * serventNum + skillDistance * skillNum
        pyautogui.click(realX,baseY)

    def chooseServentSkillWithSpecificAim(self,serventNum,skillNum,aimNum):
        '''
        点击第几号位的从者（0,1,2）
        第几个技能（0,1,2)
        对象编号（0,1,2）
        '''
        serventDistance = 446
        skillDistance = 131
        baseX = 136 #第0号从者，第0号技能
        baseY = 833

        realX = baseX + serventDistance * serventNum + skillDistance * skillNum
        pyautogui.click(realX,baseY)

        baseX = 518 #第0号从者，第0号技能
        baseY = 673
        aimDistance = 420

        realX = baseX + aimDistance * aimNum
        pyautogui.click(realX,baseY)

    def chooseEnemy(self,enemyNum):
        '''
        点击第几号位的敌人，从0开始计数
        '''
        enemyDistance = 342
        baseX = 107
        baseY = 89
        realX = baseX = enemyDistance*enemyNum
        pyautogui.click(realX,baseY)

    def InBattle(self):
        pyautogui.click(1637,866)

    def InBattleAttack(self,attackNum):
        '''
        普通攻击，从0开始，attackNum表示攻击卡的位置
        '''
        attackDistance = 359
        baseX = 205
        baseY = 741
        realX = baseX + attackNum*attackDistance
        pyautogui.click(realX,baseY)

    def InBattlePhantasm(self,phantasmNum):
        '''
        宝具，从0开始
        '''
        phantasmDistance = 324
        baseX = 623
        baseY = 315
        realX = baseX + phantasmNum * phantasmDistance
        pyautogui.click(realX,baseY)
    
    def chooseMasterSkill(self,skillNum):
        '''
        发动御主礼装技能，从0开始
        '''
        pyautogui.click(1715,476)
        baseX = 1313
        baseY = 464
        skillDistance = 125
        realX = baseX + skillNum * skillDistance
        pyautogui.click(realX,baseY)#选择技能
        #pyautogui.click(1175,623)#确认

    def changePeopleSkill(self,start,sub):
        '''
        换人礼装
        '''
        baseX = 234
        baseY = 525
        peopleDistance = 276
        realX = baseX + start * peopleDistance
        pyautogui.click(realX,baseY)

        realX = baseX + sub * peopleDistance
        pyautogui.click(realX,baseY)

        pyautogui.click(970,901)

    def checkEndFirst(self):
        try:
            ans = pyautogui.locateOnScreen('resultPage1.png')
            return True
        except:
            return False