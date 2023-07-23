# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 11:42:18 2023

@author: User
"""

# Bus CSV read once

from FilePath_OOP import FilePath
from Bus_OOP import Bus
    
                         
if __name__ =='__main__':
    #轉乘主程式
	#從現在撘乘站前往目的地是否需要轉乘

    destinationName=input('請輸入目的地站名（輸入中文）：')
    takeName=input('請輸入撘乘站站名（輸入中文）：')
    
    # 逢甲大學, 逢甲大學(福星路), 逢甲大學(逢甲路)

    # 臺中車站, 高鐵臺中站, 臺中市政府, 新光三越
        
    # 朝陽科技大學, 吉峰東自強路口
         
    
    #目的地站站點相關串列
    destination=Bus()
    

    #撘乘站站點相關串列
    take=Bus()

    
    #目的地站點相關串列
    transferStep=[] #在每條路線上的轉乘站站點
    toTransfer=[]   #可從撘乘站到轉乘站的公車
    transferTo=[]   #可從轉乘站到目的地站的公車


    #讀取CSV檔
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()    
    busListCSV=Bus.readFile(pathDir)
        
    
    
    destination.buses=Bus.readStepBusesID(destinationName,busListCSV)
    destination.steps=Bus.readStepBuses(destinationName,busListCSV)
        
    take.buses=Bus.readStepBusesID(takeName,busListCSV)        
    take.steps=Bus.readStepBuses(takeName,busListCSV)
    
    
    #判斷可直達或需要轉乘
    if Bus.sameBus(destination.buses,take.buses):
        #可直達，不需要轉乘
        
        print("----------------不需要轉乘-----------------")
        
        print(f"\n從 {takeName} 撘乘：")
        for i in take.steps:
            for j in destination.steps:
                if Bus.stepsVector(i,j):
                    print(f"{i['路線']}[{i['站序']}]，",end='')
                    print(f"到 {j['中文站點名稱']}[{j['站序']}] 下車")
             
    else:
        #需要轉乘
        print("---------------需要轉乘------------------")  
 
        destination.lines=Bus.stepInfo(destination.buses,busListCSV)
        take.lines=Bus.stepInfo(take.buses,busListCSV)   
               
        for i in take.lines:
            for j in destination.lines:
                if i['中文站點名稱'] == j['中文站點名稱']:
                    transferStep.append(i)
                    transferStep.append(j)
                    break
                
        for i in take.steps:
            for j in transferStep:
                if Bus.stepsVector(i,j):
                    toTransfer.append(j)
                    
        for i in transferStep:
            for j in destination.steps:
                if Bus.stepsVector(i,j):
                    transferTo.append(i)
                                             
        tempBus=""
        print(f"\n從 {takeName}")
        for i in toTransfer:
            if tempBus == '' or tempBus != i['路線']:
                tempBus=i['路線']
                print("-------------------------\n")
                print(f"--撘乘{i['路線']}[{i['方向']}]公車")
                        
            for j in transferTo:
                if i['中文站點名稱'] == j['中文站點名稱'] :
                    for k in destination.steps:
                        if Bus.stepsVector(j,k):
                            print(f"----到[{i['站序']}] {i['中文站點名稱']}",end='')
                            print(f"[{j['站序']}] ，轉乘{j['路線']}[{j['方向']}]公車，",end='')
                            print(f"抵達 {k['中文站點名稱']}[{k['站序']}]")
                    
                    break
                
        print("-------------------------")
        
    
