# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 11:42:18 2023

@author: User
"""

# Bus CSV read once

from FilePath_OOP import FilePath
from Bus_OOP import Stop, BusLine
    
                         
if __name__ == '__main__':
    #臺中市公車轉乘組合主程式
	#從現在撘乘站前往目的地是否需要轉乘
    
    #region 讀取臺中市市區公車站牌資料
    
    #讀取CSV檔
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()    
    busList=Stop.readFile(pathDir)
        
    # busListDF=Stop.readOnlineFile()
    # busList=busListDF.to_dict('records')    
    
    #endregion
    

    #region 目的地與撘乘站
    #目的地名稱（地標）
    # desName=input('請輸入目的地（輸入中文，可模糊名稱、地標或站名，如「臺中車站」、「逢甲大學」或「逢甲大學(福星路)」、「逢甲大學(逢甲路)」）：\n')
    desName="逢甲大學(福星路)"
        #逢甲大學, 臺中車站, 高鐵臺中站, 臺中市政府, 新光三越
    
    
    #撘乘站名稱
    # takeName=input('請輸入撘乘站站名（輸入中文，須精準站名，如「逢甲大學(福星路)」、「逢甲大學(逢甲路)」、「朝陽科技大學」、「吉峰東自強路口」）：\n')
    takeName="朝陽科技大學"
        #逢甲大學(福星路), 逢甲大學(逢甲路), 朝陽科技大學, 吉峰東自強路口
         
    des=BusLine() #目的地站站點相關串列
    take=BusLine() #撘乘站站點相關串列
    #endregion


    #region 轉乘站
    #轉乘站站點相關串列
    
    TF_Stops=[] #在每條路線上的轉乘站站點
    To_TF=[]   #可從撘乘站到轉乘站的公車
    TF_To=[]   #可從轉乘站到目的地站的公車
    
    #endregion
    
    
    #region 目的地站點及撘乘站點的所有公車及其延線
    
    des.busesID=Stop.IDsAtStop(desName,busList)
    des.lineStops=Stop.busesAtStop(desName,busList)
        
    take.busesID=Stop.IDsAtStop(takeName,busList)        
    take.lineStops=Stop.busesAtStop(takeName,busList)
    
    #endregion
    
    
    #region 開始找公車撘
    
    #判斷可直達或需要轉乘
    #region 可直達（兩站在同一條路線上）
    if Stop.sameBus(des.busesID,take.busesID):
        #可直達，不需要轉乘
        
        print("\n----------------不需要轉乘-----------------")
        
        print(f"\n從 {takeName} 撘乘：")
        for i in take.lineStops:
            for j in des.lineStops:
                if Stop.stopsVector(i,j):
                    print(f"{i[Stop.busID]}[{i[Stop.stopID]}]，",end='')
                    print(f"到 {j[Stop.stopName_CN]}[{j[Stop.stopID]}] 下車")
    #endregion
    
    #region 要轉乘（兩站的所有公車路線並沒有相同的公車路線）
             
    else:
        #轉乘
        print("\n---------------需要轉乘------------------")  
        
        #region 目的地站及撘乘站所有的公車路線及延站 
        des.lines=Stop.stopInfo(des.busesID,busList)
        take.lines=Stop.stopInfo(take.busesID,busList)   
        #endregion
        
        #region 找出行經撘乘站路線上與行經目的地站路線上相同的站點名稱
        for i in take.lines:
            for j in des.lines:
                if i[Stop.stopName_CN] == j[Stop.stopName_CN]: #為轉乘站
                
                    #region 找出從撘乘站前往轉乘站的公車
                    Stop.unduplicateList(To_TF, i)
                    #endregion
                    
                    #region 找出從轉乘站前往目的地站的公車
                    Stop.unduplicateList(TF_To, j)
                    #endregion
                    
                    # TF_Stops.append(i)
                    # TF_Stops.append(j)
                    # break
        
        # TF_Stops = Stop.autoUnduplicateList(TF_Stops)
        #endregion
        
        '''
        #region 找出從撘乘站前往轉乘站的公車
        for i in take.lineStops:
            for j in TF_Stops:
                if Stop.stopsVector(i,j):
                    To_TF.append(j)
        To_TF = Stop.autoUnduplicateList(To_TF)
        #endregion
        
        #region 找出從轉乘站前往目的地站的公車
        for i in TF_Stops:
            for j in des.lineStops:
                if Stop.stopsVector(i,j):
                    TF_To.append(i)
        TF_To = Stop.autoUnduplicateList(TF_To)
        #endregion
        
        '''
                                              
        tempBus=""
        print(f"\n從 {takeName}")
        
        #des.lineStops=sorted(des.lineStops,key=lambda x: x[Stop.stopName_CN])
        
        #region 從撘乘站到轉乘站
        for i in To_TF:
            if tempBus == '' or tempBus != i[Stop.busID]:
                tempBus=i[Stop.busID]
                print("-------------------------\n")
                print(f"--撘乘{i[Stop.busID]}[{i[Stop.roundTrip]}]公車")
        #endregion
        
        #region 從轉乘站到目的地站
                        
            for j in TF_To:
                if i[Stop.stopName_CN] == j[Stop.stopName_CN] :
                    for k in des.lineStops:
                        if Stop.stopsVector(j,k):
                            print(f"----到[{i[Stop.stopID]}] {i[Stop.stopName_CN]}",end='')
                            print(f"[{j[Stop.stopID]}] ，轉乘{j[Stop.busID]}[{j[Stop.roundTrip]}]公車，",end='')
                            print(f"抵達 {k[Stop.stopName_CN]}[{k[Stop.stopID]}]")
                    
                    # break
        #endregion
                
        print("-------------------------")
    #endregion
    
    #endregion
        