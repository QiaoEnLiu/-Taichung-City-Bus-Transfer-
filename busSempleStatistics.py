# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 14:22:03 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Bus


if __name__ =='__main__':
    #臺中市公車路線初步統計
    
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    busListCSV=Bus.readFile(pathDir)
    
    busIDList=Bus.allBusID(busListCSV)    
    listStepsNum=Bus.allBusStepsNum(busListCSV,busIDList)
    busNameList=Bus.allBusName(busListCSV)
    
    #print("路線編號") #臺中市所有公車路線數量及編號
    #for i in busIDList:
        #print(i)
        
    #print("路線編號,去程站數,回程站數") #每條路線去程、回程各站點數量
    #for i in listStepsNum:
        #print(f"{i[0]},{i[1]},{i[2]}")
        
    print("路線編號,中文名稱") #每條路線中文名稱
    for i in busNameList:
        print(f"{i[0]},{i[1]}")
    

        
    