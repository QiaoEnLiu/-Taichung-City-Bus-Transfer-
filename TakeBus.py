# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:33:26 2023

@author: User
"""
#from FilePath_OOP import FilePath
from Bus_OOP import Bus

   
if __name__ =='__main__':        
    #從現在撘乘站，前往目的地可撘哪些公車
    
    busListDF=Bus.readOnlineFile()
    busList=busListDF.to_dict('records') 

    des="朝陽科技大學"
    take="吉峰東自強路口"
       
    # 朝陽科技大學, 吉峰東自強路口
    # 臺中車站, 高鐵臺中站, 臺中市政府, 新光三越
    # 逢甲大學(福星路)
         
    desBus=[]
    desStop=[]
    
    takeBus=[]
    takeStop=[]
    
    #pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    #busList=Bus.readFile(pathDir)
    
      
    desBus=Bus.IDsAtStop(des,busList)
    desStop=Bus.busesAtStop(des,busList)
        
    takeBus=Bus.IDsAtStop(take,busList)      
    takeStop=Bus.busesAtStop(take,busList)
    
    if Bus.sameBus(desBus,takeBus):
         #兩站有相同的公車路線，則不需要轉乘
         
         print("----------------不需要轉乘-----------------")
         
         print(f"\n從 {take} 撘乘：")
         for i in takeStop:
             for j in desStop:
                 if Bus.stopsVector(i,j):
                     print(f"{j['路線']}[{j['站序']}]，到 {j['中文站點名稱']}[{j['站序']}] 下車")
        
    else:
        #兩站若沒有相同的公車路線，則需要轉乘
        print("-----------------目的地需要轉乘---------------------")
        



        
