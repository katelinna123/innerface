import xlrd
import json

file = xlrd.open_workbook('D:\install\pycharm\interwar\data\data.xls')
sh = file.sheet_by_name("添加加油卡")
print(sh.cell_value(1,3))
