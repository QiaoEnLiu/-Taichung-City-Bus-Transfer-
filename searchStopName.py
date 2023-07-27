# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:53:44 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Bus


if __name__ =='__main__':
    #查站點名稱，中文站名比對
    
    #lang=input('輸入站名語言 Input language for step name(CN/EN):')
    
    stopNameEN="Taichung Station"
    stopNameCN="臺中車站"
    
    # 臺中車站, 高鐵臺中站
    # Taichung Station, HSR Taichung Station
    
    CN_Name="中文站點名稱"    
    EN_Name="英文站點名稱"
        
    stopsList=[]
    stopsSort=[]
    stopsName=[]
    busListCSV=[]
    
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    busListCSV=Bus.readFile(pathDir)

    stopsList=Bus.searchStopName('CN', stopNameCN,stopNameEN, busListCSV)
    #stopsList=Bus.searchStopName(lang, stopNameCN,stopNameEN, busListCSV)

        
    stopsSort=sorted(stopsList,key=lambda x: x['中文站點名稱'])
    tempStopName=''
    for i in stopsSort:
        tempList=[]
        if tempStopName == '' or tempStopName != i['中文站點名稱']:
            tempList.append(i['中文站點名稱'])
            tempList.append(i['英文站點名稱'])
            tempList.append(i['經度'])
            tempList.append(i['緯度'])
            stopsName.append(tempList)
            tempStopName=i['中文站點名稱']
            print(i['中文站點名稱'],i['英文站點名稱'])
    
        
            
        
            
            