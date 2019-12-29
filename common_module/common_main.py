# -*- coding: utf-8 -*-



# from utils import FileUtil



# fileNameList = FileUtil.GetFileListFromFolderWithExtension("/Users/SeekMac/Code_Projects/study_python/python3_projects/stock_analyse/data", 
# 	False, [".csv"])
# for fileName in fileNameList.values():
# 	print(fileName)







import sys
import os
current_folder_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_folder_path+'/utils')
