from random import randint,sample
import string

from PIL import Image
from PIL import ImageFont
from PIL import  ImageDraw

class VerifyCode(object):
    #定义成员属性
    def __init__(self, width=10, height=40, size=4):
        self.width = width
        self.height = height
        self.size = size
        self.__code = None
        self.pen = None
    #
    def output(self):
        #　定义画布和画笔
        im = Image.new('RGB', (self.width, self.height), )













    def __rand_color(self):
        return randint(0, 255), randint(0, 255), randint(0, 255)