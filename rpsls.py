#coding:gbk
"""
Ŀ�ģ����RPSLS��Ϸ
���ߣ���ܰ
"""
print("���������ѡ��")
name=input()# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
print("------------")
def name_to_number(name):
    if name=='ʯͷ':
       return (0)
    elif name=='ʷ����':
       return (1)
    elif name=='��':
       return (2)
    elif name=='����':
       return (3)
    elif name=='����':
       return (4)
    else:
	    return (5)
player_choice=name_to_number(name)
print("����ѡ��Ϊ��%s"%name)
    
import random
number=random.randrange(0,4) # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number    
def number_to_name(number):# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    if number==0:
       return "ʯͷ"
    elif number==1:
       return "ʷ����"
    elif number==2:
       return "��"
    elif number==3:
       return "����"
    elif number==4:
       return "����"
comp_number=number_to_name(number)
print("�������ѡ��Ϊ:%s"%comp_number)
def rpsls(player_choice):
    if player_choice==number:
       print("���ͼ��������һ����")

    elif player_choice==0 and number==(2 or 1):
       print("����Ӯ��")
    elif player_choice==0 and number==(3 or 4):
	    print("��Ӯ��") 
          
    elif player_choice==1 and number==(2 or 3):
         print("����Ӯ��")
    elif player_choice==1 and number==(0 or 4):
		   print("��Ӯ��")
    elif player_choice==2 and number==(4 or 3):
          print("����Ӯ��")
    elif player_choice==2 and number==(1 or 2):
		   print("��Ӯ�ˣ�")
    elif player_choice==3 and number==(0 or 4):
          print("����Ӯ��")
    elif player_choice==3 and number==(1 or 2):
		   print("��Ӯ�ˣ�")  
    elif player_choice==4 and number==(2 or 3):
          print("��Ӯ�ˣ�")
    elif player_choice==4 and number==(0 or 1):
		   print("����Ӯ��") 
    
    elif player_choice==5:
       print("Error: No Correct Name")
    return rpsls
rosls=rpsls(player_choice)
    
    
    
    
    
    
    
    
    
    
