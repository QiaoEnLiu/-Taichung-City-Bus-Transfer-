# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 11:42:18 2023

@author: User
"""

# Bus CSV read once

from FilePath_OOP import FilePath
from Bus_OOP import Bus
    
                         
if __name__ =='__main__':
    #臺中市公車轉乘組合主程式
	#從現在撘乘站前往目的地是否需要轉乘

    #目的地名稱（地標）
    desName=input('請輸入目的地（輸入中文，可模糊名稱、地標或站名，如「臺中車站」、「逢甲大學」或「逢甲大學(福星路)」、「逢甲大學(逢甲路)」）：\n')
        #逢甲大學, 臺中車站, 高鐵臺中站, 臺中市政府, 新光三越
    
    #撘乘站名稱
    takeName=input('請輸入撘乘站站名（輸入中文，須精準站名，如「逢甲大學(福星路)」、「逢甲大學(逢甲路)」、「朝陽科技大學」、「吉峰東自強路口」）：\n')
        #逢甲大學(福星路), 逢甲大學(逢甲路), 朝陽科技大學, 吉峰東自強路口
         
        
    #目的地站站點相關串列
    des=Bus()
    

    #撘乘站站點相關串列
    take=Bus()

    
    #目的地站點相關串列
    TF_Step=[] #在每條路線上的轉乘站站點
    to_TF=[]   #可從撘乘站到轉乘站的公車
    TF_To=[]   #可從轉乘站到目的地站的公車


    #讀取CSV檔
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()    
    busListCSV=Bus.readFile(pathDir)
        
    
    
    des.busesID=Bus.IDsAtStep(desName,busListCSV)
    des.lineSteps=Bus.busesAtStep(desName,busListCSV)
        
    take.busesID=Bus.IDsAtStep(takeName,busListCSV)        
    take.lineSteps=Bus.busesAtStep(takeName,busListCSV)
    
    
    #判斷可直達或需要轉乘
    if Bus.sameBus(des.busesID,take.busesID):
        #可直達，不需要轉乘
        
        print("\n----------------不需要轉乘-----------------")
        
        print(f"\n從 {takeName} 撘乘：")
        for i in take.lineSteps:
            for j in des.lineSteps:
                if Bus.stepsVector(i,j):
                    print(f"{i['路線']}[{i['站序']}]，",end='')
                    print(f"到 {j['中文站點名稱']}[{j['站序']}] 下車")
             
    else:
        #需要轉乘
        print("\n---------------需要轉乘------------------")  
 
        des.lines=Bus.stepInfo(des.busesID,busListCSV)
        take.lines=Bus.stepInfo(take.busesID,busListCSV)   
        
        
        for i in take.lines:
            for j in des.lines:
                if i['中文站點名稱'] == j['中文站點名稱']: #找出行經撘乘站路線上與行經目的地站路線上相同的站點名稱，為轉乘站
                    TF_Step.append(i)
                    TF_Step.append(j)
                    break
                
        for i in take.lineSteps:
            for j in TF_Step:
                if Bus.stepsVector(i,j): #找出從撘乘站前往轉乘站的公車
                    to_TF.append(j)
                    
        for i in TF_Step:
            for j in des.lineSteps:
                if Bus.stepsVector(i,j): #找出從轉乘站前往目的地站的公車
                    TF_To.append(i)
                                              
        tempBus=""
        print(f"\n從 {takeName}")
        for i in to_TF:
            if tempBus == '' or tempBus != i['路線']:
                tempBus=i['路線']
                print("-------------------------\n")
                print(f"--撘乘{i['路線']}[{i['方向']}]公車")
                        
            for j in TF_To:
                if i['中文站點名稱'] == j['中文站點名稱'] :
                    for k in des.lineSteps:
                        if Bus.stepsVector(j,k):
                            print(f"----到[{i['站序']}] {i['中文站點名稱']}",end='')
                            print(f"[{j['站序']}] ，轉乘{j['路線']}[{j['方向']}]公車，",end='')
                            print(f"抵達 {k['中文站點名稱']}[{k['站序']}]")
                    
                    break
                
        print("-------------------------")
        
    
