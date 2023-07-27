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
    
    CN_Name="中文站點名稱"    
    EN_Name="英文站點名稱"
        
    stopsList=[]
    stopsSort=[]
    stopsNameList=[]
  
    #stopsList=Bus.searchStopName(lang, stopNameCN,stopNameEN, busList)
    stopsList=Bus.searchStopName('CN', stopNameCN,stopNameEN, busList)


    stopsSort=sorted(stopsList,key=lambda x: x['中文站點名稱'])
    tempStopName=''
    print()
    for i in stopsSort:
        if tempStopName == '' or tempStopName != i['中文站點名稱']:
            stopsNameList.append(i)
            tempStopName=i['中文站點名稱']
            print(i['中文站點名稱'],i['英文站點名稱'])
    