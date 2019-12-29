# -*- coding: utf-8 -*-



import xlrd


import g_var
application_path = g_var.get_value("ApplicationPath")


filename = application_path+"/res/ISCN_海盐爱建.xls"
data = xlrd.open_workbook(filename)#文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。
names = data.sheet_names()    #返回book中所有工作表的名字
for tempStr in names:
	print("打印名字："+tempStr)

# table = data.sheets()[0]  
# nrows = table.nrows  #获取该sheet中的有效行数
# print("表格有效长度："+str(nrows))

def start():
	print("----core.start-----------------")
	# ImageHandle.AddTextInImage()
	pass





