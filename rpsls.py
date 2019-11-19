#coding:gbk
"""
目的：完成RPSLS游戏
作者：贺馨
"""
print("请输入你的选择：")
name=input()# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
print("------------")
def name_to_number(name):
    if name=='石头':
       return (0)
    elif name=='史波克':
       return (1)
    elif name=='布':
       return (2)
    elif name=='蜥蜴':
       return (3)
    elif name=='剪刀':
       return (4)
    else:
	    return (5)
player_choice=name_to_number(name)
print("您的选择为：%s"%name)
    
import random
number=random.randrange(0,4) # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number    
def number_to_name(number):# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
    if number==0:
       return "石头"
    elif number==1:
       return "史波克"
    elif number==2:
       return "布"
    elif number==3:
       return "蜥蜴"
    elif number==4:
       return "剪刀"
comp_number=number_to_name(number)
print("计算机的选择为:%s"%comp_number)
def rpsls(player_choice):
    if player_choice==number:
       print("您和计算机出的一样呢")

    elif player_choice==0 and number==(2 or 1):
       print("机器赢了")
    elif player_choice==0 and number==(3 or 4):
	    print("您赢了") 
          
    elif player_choice==1 and number==(2 or 3):
         print("机器赢了")
    elif player_choice==1 and number==(0 or 4):
		   print("您赢了")
    elif player_choice==2 and number==(4 or 3):
          print("机器赢了")
    elif player_choice==2 and number==(1 or 2):
		   print("您赢了！")
    elif player_choice==3 and number==(0 or 4):
          print("机器赢了")
    elif player_choice==3 and number==(1 or 2):
		   print("您赢了！")  
    elif player_choice==4 and number==(2 or 3):
          print("您赢了！")
    elif player_choice==4 and number==(0 or 1):
		   print("机器赢了") 
    
    elif player_choice==5:
       print("Error: No Correct Name")
    return rpsls
rosls=rpsls(player_choice)
    
    
    
    
    
    
    
    
    
    
