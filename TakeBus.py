# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:33:26 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Bus


if __name__ =='__main__':        
    #從現在撘乘站，前往目的地可撘哪些公車

    destination="朝陽科技大學"
    take="吉峰東自強路口"
       
    # 朝陽科技大學, 吉峰東自強路口

    # 臺中車站, 高鐵臺中站, 臺中市政府, 新光三越
        
    # 逢甲大學(福星路)
    
    busListCSV=[]
     
    destinationBus=[]
    destinationStep=[]
    
    takeBus=[]
    takeStep=[]
    
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    
    busListCSV=Bus.readFile(pathDir)
      
    destinationBus=Bus.readStepBusesID(destination,busListCSV)
    destinationStep=Bus.readStepBuses(destination,busListCSV)
        
    takeBus=Bus.readStepBusesID(take,busListCSV)      
    takeStep=Bus.readStepBuses(take,busListCSV)
    
    if Bus.sameBus(destinationBus,takeBus):
         #兩站有相同的公車路線，則不需要轉乘
         
         print("----------------不需要轉乘-----------------")
         
         for i in takeStep:
             for j in destinationStep:
                 if i['路線'] == j['路線'] and i['方向'] == j['方向'] and int(i['站序']) < int(j['站序']):
                     print(f"從{i['中文站點名稱']}({take})(站序{i['站序']})撘{i['路線']}({j['路線']})，到{j['中文站點名稱']}({destination})(站序{j['站序']})下車")
        
    else:
        #兩站若沒有相同的公車路線，則需要轉乘
        print("-----------------目的地需要轉乘---------------------")
        



        
