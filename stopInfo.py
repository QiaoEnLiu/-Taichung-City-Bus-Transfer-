# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:39:12 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Stop



if __name__ =='__main__':
    #站牌資訊，該站點上所有公車路線

    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()    
    busList=Stop.readFile(pathDir)
  
    # busListDF=Stop.readOnlineFile()
    # busList=busListDF.to_dict('records') 
    
    
    stopName=input('請輸入站點名稱（朝陽科技大學、臺中車站、逢甲大學）：')

    # 朝陽科技大學, 吉峰東自強路口
    # 臺中車站, 高鐵臺中站, 臺中市政府, 新光三越     
    # 逢甲大學(福星路)
    
    busIDList=[]
    stopsSort=[]
    stopsName=[]
    
    for i in busList:
        if stopName in i[Stop.stopName_CN]:
            busIDList.append(i)
            
    stopsSort=sorted(busIDList,key=lambda x: (x[Stop.stopName_CN],x[Stop.latitude]))

    print()
    tempNameLaLo=''
    for i in stopsSort:
        if tempNameLaLo=='' or tempNameLaLo!=(i[Stop.stopName_CN]+','+str(i[Stop.latitude])+','+str(i[Stop.longitude])):
            tempNameLaLo=i[Stop.stopName_CN]+','+str(i[Stop.latitude])+','+str(i[Stop.longitude])
            print("---------")
            print(f"\n{i[Stop.stopName_CN]}",f"{i[Stop.stopName_EN]},",f"({i[Stop.latitude]},{i[Stop.longitude]})\n---------")
        if tempNameLaLo == (i[Stop.stopName_CN]+','+str(i[Stop.latitude])+','+str(i[Stop.longitude])):
            print(i[Stop.busID],i[Stop.roundTrip],f"[{i[Stop.stopID]}]")
    print("---------")
