# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:33:26 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Bus

   
if __name__ =='__main__':        
    #從現在撘乘站，前往目的地可撘哪些公車

    des="朝陽科技大學"
    take="吉峰東自強路口"
       
    # 朝陽科技大學, 吉峰東自強路口

    # 臺中車站, 高鐵臺中站, 臺中市政府, 新光三越
        
    # 逢甲大學(福星路)
    
    busListCSV=[]
     
    desBus=[]
    desStep=[]
    
    takeBus=[]
    takeStep=[]
    
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    
    busListCSV=Bus.readFile(pathDir)
      
    desBus=Bus.IDsAtStep(des,busListCSV)
    desStep=Bus.busesAtStep(des,busListCSV)
        
    takeBus=Bus.IDsAtStep(take,busListCSV)      
    takeStep=Bus.busesAtStep(take,busListCSV)
    
    if Bus.sameBus(desBus,takeBus):
         #兩站有相同的公車路線，則不需要轉乘
         
         print("----------------不需要轉乘-----------------")
         
         print(f"\n從 {take} 撘乘：")
         for i in takeStep:
             for j in desStep:
                 if Bus.stepsVector(i,j):
                     print(f"{i['路線']}[{i['站序']}]，到 {j['中文站點名稱']}[{j['站序']}] 下車")
        
    else:
        #兩站若沒有相同的公車路線，則需要轉乘
        print("-----------------目的地需要轉乘---------------------")
        



        
