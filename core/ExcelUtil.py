# -*- coding: utf-8 -*-


import os
import xlrd

def GetTableItemTitles(excelFilePath):
	excelFilePath = excelFilePath.replace("/", os.sep)
	excel = xlrd.open_workbook(excelFilePath, formatting_info = True)
	# sheetNames = data.sheet_names()    #返回book中所有工作表的名字
	# for tempStr in sheetNames:
	# 	table = data.sheet_by_name(tempStr)
	# 	nrows = table.nrows  #获取该sheet中的有效行数
	# 	ncols = table.ncols  #获取列表的有效列数
	# 	print("tableName = {0}, rows = {1}, cols = {2}".format(tempStr, nrows, ncols))
	table = excel.sheet_by_index(0)
	row_len = table.nrows  #获取该sheet中的有效行数
	col_len = table.ncols  #获取列表的有效列数
	print("rows = {0}, cols = {1}".format(row_len, col_len))
	# for item in table.row_slice(8):
	# 	print("_____"+str(item))
	if row_len <= 0 or col_len <= 0 :
		return None
	startRowIdx = 0
	startColIdx = 0
	for rowIdx in range(row_len):
		for colIdx in range(col_len):
			if rowIdx >= 5:
				break
			xfx = table.cell_xf_index(rowIdx, colIdx)
			xf = excel.xf_list[xfx]
			bgx = xf.background
			print(bgx.__dict__)

