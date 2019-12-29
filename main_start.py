# -*- coding: utf-8 -*-


# import system module
import sys
import os
application_path = os.path.abspath('.')
# #把模块的路径加到当前的主程序中
sys.path.append(application_path+'/core')
sys.path.append(application_path+'/common_module')
# #把模块的路径加到当前的主程序中
# sys.path.append(application_path+'/showapi')
# sys.path.append(application_path+'/model')


import constant
import g_var
g_var._init()#在主模块初始化全局变量的dic
# #定义当前的程序名称
g_var.set_value("ApplicationTag", "tool_excel")
# #定义文件的根路径
g_var.set_value('ApplicationPath', application_path)
# #定义文件的根路径
g_var.set_value('DataPath', application_path+'/data')


#import custom module
from common_module import common_main


#import custom code
import Logger
import FileHelper



# #>>>>-----初始化-----<<<<<
#注意：Logger的初始化必须比其他类早
Logger._init()
FileHelper._init()



#region app入口
from core import core_main

print("AppStart: root_path = "+application_path)
core_main.start()
#endregion 


