# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:53:44 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Bus


if __name__ =='__main__':
    #站點名稱比對
    
    lang=input('輸入站名語言 Input language for step name(CN/EN):')
    
    stepNameEN="Taichung Station"
    stepNameCN="臺中車站"
    
    # 臺中車站, 高鐵臺中站
    # Taichung Station, HSR Taichung Station
    
    CN_Name="中文站點名稱"    
    EN_Name="英文站點名稱"
        
    stepsList=[]
    busListCSV=[]
    
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    busListCSV=Bus.readFile(pathDir)

    stepsList=Bus.searchStepName(lang, stepNameCN,stepNameEN, busListCSV)
    
    print('路線,方向,站序,中文站點名稱,英文站點名稱,經度,緯度')
    for i in stepsList:
        print(i['路線'],i['方向'],i['站序'],i['中文站點名稱'],i['英文站點名稱'],i['經度'],i['緯度'])