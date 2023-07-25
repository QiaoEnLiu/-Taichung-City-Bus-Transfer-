158# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:59:39 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Bus

if __name__ =='__main__':
    #該公車路線
    
    busID=input('請輸入路線：')
       
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    busListCSV=Bus.readFile(pathDir)
    
    stepsList=[]
    Bus.linesAtStep(busID,stepsList,busListCSV)
    
    tempBound=''
    for i in stepsList:
        if tempBound == '' or tempBound != i['方向']:
            tempBound=i['方向']
            print("-------------------------\n")
            print(f"{busID}路線：[{i['路線名稱']}]")
            print(f"--{i['方向']}")
            print("--------------")
            
        print(i['站序'],i['中文站點名稱'],i['英文站點名稱'],i['經度'],i['緯度'],sep=", ")