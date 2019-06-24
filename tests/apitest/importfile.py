# 打开文件
import os

#__file__,当前文件路径
# print(__file__)

#父级目录
# os.path.dirname(__file__)
#父级的父级
# os.path.dirname(os.path.dirname(__file__))
#项目的绝对路径
basedir = os.path.abspath(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
file_path = os.path.join(basedir,'data','1.txt')
print(file_path)

f = open("D:/install/pycharm/interwar/tests/data/1.txt")
print(f)
#逐行读取，去除换行strip（）
data = [item.strip() for item in f.readlines()]