# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:53:44 2023

@author: User
"""
#from FilePath_OOP import FilePath
from Bus_OOP import Bus


if __name__ =='__main__':
    #查站點名稱，中文站名比對（輸出只有站名）
    
    #pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()    
    #busList=Bus.readFile(pathDir)
  
    busListDF=Bus.readOnlineFile()
    busList=busListDF.to_dict('records') 
    
    #lang=input('查詢站點「臺中車站」 Seach Stop Name(Taichung Station)\n輸入語言 Input language for step name(CN/EN):')
    
    stopNameCN="臺中車站"
    stopNameEN="Taichung Station"
    
    # 臺中車站, 高鐵臺中站
    # Taichung Station, HSR Taichung Station
    
    CN_Name=Bus.stopName_CN    
    EN_Name=Bus.stopName_EN
        
    stopsList=[]
    stopsSort=[]
    stopsNameList=[]
  
    #stopsList=Bus.searchStopName(lang, stopNameCN,stopNameEN, busList)
    stopsList=Bus.searchStopName('CN', stopNameCN,stopNameEN, busList)


    stopsSort=sorted(stopsList,key=lambda x: (x[Bus.stopName_CN],x[Bus.latitude]))
    tempStopNameLaLo=''
    print()
    for i in stopsSort:
        if tempStopNameLaLo == '' or tempStopNameLaLo != (i[Bus.stopName_CN]+','+str(i[Bus.latitude])+','+str(i[Bus.longitude])):
            stopsNameList.append(i)
            tempStopNameLaLo=i[Bus.stopName_CN]+','+str(i[Bus.latitude])+','+str(i[Bus.longitude])
            print(i[Bus.stopName_CN],i[Bus.stopName_EN],i[Bus.latitude],i[Bus.longitude])