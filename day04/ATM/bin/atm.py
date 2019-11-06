
#不在入口写主逻辑
# print("Welcom to my atm")
#
# print(__file__)#打印相对路径

#我们需要动态的获取绝对路径并加到系统环境变量中

import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from conf import settings
from core import main

main.login()