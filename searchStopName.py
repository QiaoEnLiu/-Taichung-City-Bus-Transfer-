# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:53:44 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Bus


if __name__ =='__main__':
    #中文站點名稱比對
    
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
    
    '''
    print('路線,方向,站序,中文站點名稱,英文站點名稱,經度,緯度')
    for i in stopsList:
        print(i['路線'],i['方向'],i['站序'],i['中文站點名稱'],i['英文站點名稱'],i['經度'],i['緯度'])
    '''
        
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
            
    for i in stopsName:
        print(f"{i[0]},{i[1]}")
        '''
        for j in stepsSort:
            print(f"{j['路線']}[{j['方向']},{j['站序']}]",end=',')
        print()
        '''
        
            
            
        
            
            