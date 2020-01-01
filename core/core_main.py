# -*- coding: utf-8 -*-


import os
import xlrd


import g_var
application_path = g_var.get_value("ApplicationPath")

import ExcelUtil

filePath = application_path+"/res/XX爱建.xls"



# table = data.sheets()[0]  
# nrows = table.nrows  #获取该sheet中的有效行数
# print("表格有效长度："+str(nrows))

def start():
	print("----core.start-----------------")
	ExcelUtil.GetTableItemTitles(filePath)

	pass





