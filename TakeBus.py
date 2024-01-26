# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:33:26 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Stop

   
if __name__ =='__main__':        
    #從現在撘乘站，前往目的地可撘哪些公車
    
    #region 讀取CSV檔
    
    # busListDF=Stop.readOnlineFile()
    # busList=busListDF.to_dict('records') 
    
    
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()    
    busList=Stop.readFile(pathDir)
    #endregion

    #region 目的地站與撘乘站測試
    des="朝陽科技大學"
    take="吉峰東自強路口"
       
    # 朝陽科技大學, 吉峰東自強路口
    # 臺中車站, 高鐵臺中站, 臺中市政府, 新光三越
    # 逢甲大學(福星路)    
    #endregion


    #region 目的地站點及撘乘站點各公車及其路線延站      
    desBus=Stop.IDsAtStop(des,busList)
    desStop=Stop.busesAtStop(des,busList)
        
    takeBus=Stop.IDsAtStop(take,busList)      
    takeStop=Stop.busesAtStop(take,busList)
    
    #endregion
    
    #region 開始找公車撘
    #region 可直達（兩站在同一條路線上）
    if Stop.sameBus(desBus,takeBus):
         #兩站有相同的公車路線，則不需要轉乘
         
         print("----------------不需要轉乘-----------------")
         
         print(f"\n從 {take} 撘乘：")
         for i in takeStop:
             for j in desStop:
                 if Stop.stopsVector(i,j):
                     print(f"{j[Stop.busID]}[{j[Stop.stopID]}]，到 {j[Stop.stopName_CN]}[{j[Stop.stopID]}] 下車")
    #endregion
    
    #region 要轉乘（兩站的所有公車路線並沒有相同的公車路線）
    else:
        #兩站若沒有相同的公車路線，則需要轉乘
        print("-----------------目的地需要轉乘---------------------")
    #endregion
    #endregion
        
        
