# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 14:22:03 2023

@author: User
"""
#from FilePath_OOP import FilePath
from Bus_OOP import Bus


if __name__ =='__main__':
    #臺中市公車路線初步統計
    
    #pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()    
    #busList=Bus.readFile(pathDir)
  
    busListDF=Bus.readOnlineFile()
    busList=busListDF.to_dict('records') 
    
    search=input('1：顯示臺中市公車路線數量\n2：顯示臺中市公車各路線站點數量（去程、回程）\n3：顯示臺中市公車路線編號與中文名稱\n4：站點名稱數量（中文）\n')
    
    busIDList=Bus.allBusID(busList)    
    listStopsNum=Bus.allBusStopsNum(busList,busIDList)
    busNameList=Bus.allBusName(busList)
    
    if search =='1':
        print("路線編號") #臺中市所有公車路線數量及編號
        for i in busIDList:
            print(i)
        buses=len(busIDList)
        print(f'\n臺中市公車共{buses}條路線') 
            
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
        buses=len(busNameList)
        print(f'\n臺中市公車共{buses}條路線')
            
    elif search =='4':
        sortStops=input('1：以名稱總計\n2：以站點位置（經緯度）總計\n')
        
        if sortStops=="1":
            stopsSort=sorted(busList,key=lambda x: x[Bus.busName])
            stopNameList=[]
            tempName=''
            for i in stopsSort:
                tempList=[]
                if tempName=='' or tempName!=i[Bus.busName]:
                    tempList.append(i[Bus.busName])
                    tempList.append(i[Bus.stopName_EN])
                    stopNameList.append(tempList)
                    tempName=i[Bus.busName]
                if tempName == i[Bus.busName]:
                    continue
            nums=len(stopNameList)
            print(f'行經臺中市內所有路線上的站點共{len(stopNameList)}站')
        
        elif sortStops=="2":
            stopsSort=sorted(busList,key=lambda x: (x[Bus.busName],x[Bus.latitude]))
            stopNameList=[]
            tempNameLaLo=''
            for i in stopsSort:
                tempList=[]
                if tempNameLaLo=='' or tempNameLaLo!=(i[Bus.busName]+","+str(i[Bus.latitude])+","+str(i[Bus.longitude])):
                    tempList.append(i[Bus.busName])
                    tempList.append(i[Bus.stopName_EN])
                    tempList.append(i[Bus.latitude])
                    tempList.append(i[Bus.longitude])
                    stopNameList.append(tempList)
                    tempNameLaLo=(i[Bus.busName]+","+str(i[Bus.latitude])+","+str(i[Bus.longitude]))
                if tempNameLaLo ==(i[Bus.busName]+","+str(i[Bus.latitude])+","+str(i[Bus.longitude])):
                    continue
            nums=len(stopNameList)
            print(f'行經臺中市內所有路線上的站點共{len(stopNameList)}站')
        
 
        
    