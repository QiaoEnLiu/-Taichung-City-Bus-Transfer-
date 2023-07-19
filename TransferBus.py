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

    destination="逢甲大學"
    take="朝陽科技大學"
    
    # 朝陽科技大學, 吉峰東自強路口

    # 臺中車站, 高鐵臺中站, 臺中市政府, 新光三越
        
    # 逢甲大學(福星路)
            
    destinationBus=[]
    desBusLine=[]
    destinationStep=[]
    
    transferStep=[]
    toTransfer=[]
    transferTo=[]
       
    takeBus=[]
    takeBusLine=[]
    takeStep=[]

    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    
    busListCSV=Bus.readFile(pathDir)
    
    destinationBus=Bus.readStepBusesID(destination,busListCSV)
    destinationStep=Bus.readStepBuses(destination,busListCSV)
        
    takeBus=Bus.readStepBusesID(take,busListCSV)        
    takeStep=Bus.readStepBuses(take,busListCSV)
    
    if Bus.sameBus(destinationBus,takeBus):
        #不需要轉乘
        
        print("----------------不需要轉乘-----------------")
        
        print(f"\n從 {take} 撘乘：")
        for i in takeStep:
            for j in destinationStep:
                if Bus.stepsVector(i,j):
                    print(f"{i['路線']}[{i['站序']}]，",end='')
                    print(f"到 {j['中文站點名稱']}[{j['站序']}] 下車")
             
    else:
        #需要轉乘
        print("---------------需要轉乘------------------")  
 
        desBusLine=Bus.stepInfo(destinationBus,busListCSV)
        takeBusLine=Bus.stepInfo(takeBus,busListCSV)   
               
        for i in takeBusLine:
            for j in desBusLine:
                if i['中文站點名稱'] == j['中文站點名稱']:
                    transferStep.append(i)
                    transferStep.append(j)
                    break
                
        for i in takeStep:
            for j in transferStep:
                if Bus.stepsVector(i,j):
                    toTransfer.append(j)
                    
        for i in transferStep:
            for j in destinationStep:
                if Bus.stepsVector(i,j):
                    transferTo.append(i)
                                             
        tempBus=""
        print(f"\n從 {take}")
        for i in toTransfer:
            if tempBus == '' or tempBus != i['路線']:
                tempBus=i['路線']
                print("-------------------------\n")
                print(f"--撘乘{i['路線']}[{i['方向']}]公車")
                        
            for j in transferTo:                
                if i['中文站點名稱'] == j['中文站點名稱'] :
                    for k in destinationStep:
                        if Bus.stepsVector(j,k):
                            print(f"----到[{i['站序']}] {i['中文站點名稱']}",end='')
                            print(f"[{j['站序']}] ，轉乘{j['路線']}[{j['方向']}]公車，",end='')
                            print(f"抵達 {k['中文站點名稱']}[{k['站序']}]")
                    
                    break
                
        print("-------------------------")
        
    
