# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 14:22:03 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Bus


if __name__ =='__main__':
    #臺中市公車路線初步統計
    
    search=input('1：顯示臺中市公車路線數量\n2：顯示臺中市公車各路線站點數量（去程、回程）\n3：顯示臺中市公車路線編號與中文名稱\n')
    
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    busListCSV=Bus.readFile(pathDir)
    
    busIDList=Bus.allBusID(busListCSV)    
    listStopsNum=Bus.allBusStopsNum(busListCSV,busIDList)
    busNameList=Bus.allBusName(busListCSV)
    
    if search =='1':
        print("路線編號") #臺中市所有公車路線數量及編號
        for i in busIDList:
            print(i)
            
    elif search =='2':
        sortBus=input('1：去程站數由大到小排序\n2：回程站數由大到小排序\n預設：以編號排序\n')
        print("路線編號,去程站數,回程站數") #每條路線去程、回程各站點數量
        
                        
        if sortBus=='1': #去程站數由大到小排序
            listStopsNum.sort(key=lambda x: x[1], reverse=True)
            for i in listStopsNum:
                print(f"{i[0]},{i[1]},{i[2]}")
                       
        elif sortBus=='2': #回程站數由大到小排序
            listStopsNum.sort(key=lambda x: x[2], reverse=True)
            for i in listStopsNum:
                print(f"{i[0]},{i[1]},{i[2]}")
                
        else: #編號排序
            for i in listStopsNum:
                print(f"{i[0]},{i[1]},{i[2]}")
        
            
    elif search =='3':
        print("路線編號,中文名稱") #每條路線中文名稱
        for i in busNameList:
            print(f"{i[0]},[{i[1]}]")
    

        
    