# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:24:44 2023

@author: User
"""
import csv

class Bus:
    
    #Resource/臺中市市區公車站牌資料.CSV    
    
    def __init__(self,busID,busName,roundTrip,stationID,stationName_CN,stationName_EN,latitude,longitude): 
                
        self.busID=busID #路線編號
        self.busName=busName #路線名稱：名稱為「端點A站 - 端點B站」
        self.roundTrip=roundTrip #方向：路線名稱「端點A站 - 端點B站」為去程(outbound)，「端點A站」為發車站，站序1；而回程(inbound)以「端點B站」發車，「端點B站」站序為1，為回程發車站
        self.stationID=stationID #站序：發車站點（端點）為1，數字遞增為行車方向
        self.stationName_CN=stationName_CN #中文站點名稱
        self.stationName_EN=stationName_EN #英文站點名稱
        self.latitude=latitude #經度
        self.longitude=longitude #緯度
        
        #針對公車CSV檔欄位所呈現的物件Bus，但目前用不到


    def readFile(filePath):
        
        busList=[]             
        with open(filePath,newline='',encoding='big5') as csvFile:   #encoding='utf-8-sig'     
            rows=csv.DictReader(csvFile)
            for row in rows:
                busList.append(row)                    
        csvFile.close()
        return busList
    
        #讀檔


    def readStepBusesID(takeStep,busList):
    
        busIDList=[]
        temp=''
        for i in busList:
            if takeStep in i['中文站點名稱']:
                if temp == '' or temp != i['路線']:                        
                    busIDList.append(i['路線'])
                    temp=i['路線']
        return busIDList
    
        #查站牌路線（純路線編號）


    def readStepBuses(takeStep,busList):
    
        busIDList=[]
        for i in busList:
            if takeStep in i['中文站點名稱']:
                busIDList.append(i)
        return busIDList
    
        #查站牌路線（該站牌行）


    def sameBus(destinationBus,takeBus):
        
    
        for i in destinationBus:
            for j in takeBus:
                if i == j:
                    return i == j
        
        #轉乘程式碼中，判斷是否需要轉乘        
            
        
    def stepInfo(stepBusesID,busList):
             
        busLine=[]
        tempList=[]
        for i in stepBusesID:
            Bus.readBusSteps(i, tempList,busList)
            busLine.extend(tempList)
            tempList=[]
        return busLine
        
        #站牌資訊（途經該站所有公車路線）


    def readBusSteps(busID,tempList,busList):
        
        for i in busList:
            if busID == i['路線']:        
                tempList.append(i)
                
        #查路線延站        
                
                
    def sameSteps(bus1,bus2,busList):
        
        bus1Steps=[]
        bus2Steps=[]
        sameSteps=[]
        
        Bus.readBusSteps(bus1,bus1Steps,busList)
        Bus.readBusSteps(bus2,bus2Steps,busList)
        
        for i in bus1Steps:
            for j in bus2Steps:
                if i['中文站點名稱'] == j['中文站點名稱']:
                    sameSteps.append(i)
                    break
                
        return sameSteps
        
        #兩條硌線相同站點，以bus1站點為主
    
    
    def stepsVector(take, destination):
        
        return take['路線'] == destination['路線'] and take['方向'] == destination['方向'] and int(take['站序']) < int(destination['站序'])
        
        #撘乘站與目的地站是否在同一條路線、同個方向，且以前兩狀況下目的地站是否在撘乘站之後
    
    
    def allBusID(busList): 
        
        busIDList=[]
        tempID=''
        buses=0
        
        for i in busList:
            if tempID == '' or tempID != i['路線']:
                busIDList.append(i['路線'])
                tempID=i['路線']

        buses=len(busIDList)
        print("臺中市公車共",buses,"條路線") 
        return busIDList
        
        #臺中市所有公車路線編號
        
    
    def allBusName(busList):
        
                
        busNameList=[]
        tempBusName=''
        
        for i in busList:
            tempList=[]
            if tempBusName == '' or tempBusName != i['路線名稱']:
                tempList.append(i['路線'])
                tempList.append(i['路線名稱'])
                busNameList.append(tempList)
                tempBusName=i['路線名稱']
                
        return busNameList
    
        #臺中市所有公車路線名稱
        
    
    def allBusStepsNum(busList,busIDList):
        
        listStepsNum=[]        
        for i in range(len(busIDList)):
            listTemp=[]
            stepsOB=0
            stepsIB=0    
            
            for row in busList:
                if busIDList[i]==row['路線']:                    
                    if "去程"==row['方向']:                
                        stepsOB+=1 
                        
                    if "回程"==row['方向']:                        
                        stepsIB+=1                   
                    
            listTemp.append(busIDList[i])
            listTemp.append(stepsOB)
            listTemp.append(stepsIB)
            listStepsNum.append(listTemp)
            
        #串列[['路線'],去程站數量,回程站數量]    
        return listStepsNum
          
        #該路線去程站數量及回程站數量
        
    
    def searchStepName(lang,stepNameCN,stepNameEN,busList):
        
        stepsList=[]
        CN_Name="中文站點名稱"    
        EN_Name="英文站點名稱"
        stepName=""
        
        langField=""
        
        if lang=="CN":
            langField=CN_Name
            stepName=stepNameCN
        elif lang=="EN":
            langField=EN_Name
            stepName=stepNameEN
            
        for i in busList:
            if stepName in i[langField]:
                stepsList.append(i)
                
        return stepsList
    
        #查站點名稱（中文/英文）    