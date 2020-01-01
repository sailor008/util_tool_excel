# -*- coding: utf-8 -*-


import os
import xlrd

def GetTableItemTitles(excelFilePath):
	excelFilePath = excelFilePath.replace("/", os.sep)
	excel = xlrd.open_workbook(excelFilePath, formatting_info = True)
	# sheetNames = data.sheet_names()    #返回book中所有工作表的名字
	# for tempStr in sheetNames:
	# 	table = data.sheet_by_name(tempStr)
	table = excel.sheet_by_index(0)
	row_len = table.nrows  #获取该sheet中的有效行数
	col_len = table.ncols  #获取列表的有效列数
	print("rows = {0}, cols = {1}".format(row_len, col_len))
	if row_len <= 0 or col_len <= 0 :
		return None
	#todo 从表头开始遍历，找到第一个 背景填充的格子，认定其为表格标题 开始
	targetRow = None
	targetCol = None
	for rowIdx in range(row_len):
		for colIdx in range(col_len):
			xfx = table.cell_xf_index(rowIdx, colIdx)
			xf = excel.xf_list[xfx]
			isCellBgFill = xf.background.fill_pattern
			if isCellBgFill == 1:
				targetRow = rowIdx
				targetCol = colIdx
				break
	if targetRow == None or targetCol == None:
		return None
	print("表格标题开始的格子：(%s, %s)"%(targetRow, targetCol))
	for cell in table.row_slice(targetRow):
		print("_____"+str(cell))

