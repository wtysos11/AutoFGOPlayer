import pyautogui
from PIL import Image
import time
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
        print("Find servent")
        re = pyautogui.screenshot(region = (110,427,336-110,552-427))
        aim = Image.open('aimServent.png')
        result = self.findInImage(aim,re)
        count = 0
        while result is None:
            #单次移动
            print("Move once")
            pyautogui.moveTo(115,767)
            pyautogui.drag(0,-248,1.5,button = 'left')
            re = pyautogui.screenshot(region = (110,427,336-110,552-427))
            result = self.findInImage(aim,re)
            count += 1
            if count>4:
                return False
        
        self.clickFirstServent()
        return True
    
    def clickFirstServent(self):
        pyautogui.click(834,423)
    
    def beginMission(self):
        pyautogui.click(1703,973)