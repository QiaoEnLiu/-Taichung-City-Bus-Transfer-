# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:24:44 2023

@author: User
"""
import csv

class Bus:
    
    #Resource/臺中市市區公車站牌資料.CSV    
    
    def __init__(self):
        
        self.busesID=[] #行經該站點的公車
        self.lines=[] #行經該站點公車路線
        self.lineSteps=[] #在每條路線上的該站點
    
    '''
    def __init__(self,busID,busName,roundTrip,stepID,stepName_CN,stepName_EN,latitude,longitude): #針對公車CSV檔欄位所呈現的物件Bus，但目前用不到
                
        self.busID=busID #路線：路線編號
        self.busName=busName #路線名稱：名稱為「端點A站 - 端點B站」
        self.roundTrip=roundTrip #方向：路線名稱「端點A站 - 端點B站」為去程(outbound)，「端點A站」為發車站，站序1；而回程(inbound)以「端點B站」發車，「端點B站」站序為1，為回程發車站
        self.stepID=stepID #站序：發車站點（端點）為1，數字遞增為行車方向
        self.stepName_CN=stepName_CN #中文站點名稱
        self.stepName_EN=stepName_EN #English Step Name
        self.latitude=latitude #經度
        self.longitude=longitude #緯度
        
        '''


    def readFile(filePath): #讀檔
        
        busList=[]             
        with open(filePath,newline='',encoding='big5') as csvFile:   #encoding='utf-8-sig'     
            rows=csv.DictReader(csvFile)
            for row in rows:
                busList.append(row)                    
        csvFile.close()
        return busList
    


    def IDsAtStep(takeStep,busList): #查行經該站點的路線編號
       
        busIDList=[]
        temp=''
        for i in busList:
            if takeStep in i['中文站點名稱']:
                if temp == '' or temp != i['路線']:  
                    busIDList.append(i['路線'])
                    temp=i['路線']
        return busIDList

    

    def busesAtStep(takeStep,busList): #查行經該站點的路線（該站點行）
    
        busIDList=[]
        for i in busList:
            if takeStep in i['中文站點名稱']:
                busIDList.append(i)
        return busIDList
    
        

    def sameBus(desBus,takeBus): #轉乘程式碼中，判斷是否需要轉乘
            
        for i in desBus:
            for j in takeBus:
                if i == j:
                    return i == j
        
                                   
    def stepInfo(stepBusesID,busList): #站牌資訊（行經該站所有公車路線，如同該站上列出行經該站的路線）
             
        busLine=[]
        tempList=[]
        for i in stepBusesID:
            Bus.linesAtStep(i, tempList,busList)
            busLine.extend(tempList)
            tempList=[]
        return busLine
                

    def linesAtStep(busID,tempList,busList): #路線延站
        
        for i in busList:
            if busID == i['路線']:        
                tempList.append(i)
                                            
              
    def sameSteps(bus1,bus2,busList): #兩條硌線相同站點
        
        bus1Steps=[]
        bus2Steps=[]
        sameSteps=[]
        
        Bus.linesAtStep(bus1,bus1Steps,busList)
        Bus.linesAtStep(bus2,bus2Steps,busList)
        
        for i in bus1Steps:
            for j in bus2Steps:
                if i['中文站點名稱'] == j['中文站點名稱']:
                    sameSteps.append(i)
                    sameSteps.append(j)
                    break
                
        return sameSteps
        
    
    def stepsVector(take, des): #撘乘站與目的地站是否在同一條路線、同個方向，且以前兩狀況下目的地站是否在撘乘站之後
        
        return take['路線'] == des['路線'] and take['方向'] == des['方向'] and int(take['站序']) < int(des['站序'])
        
                
    def allBusID(busList): #臺中市所有公車路線編號
        
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
        
        
    def allBusName(busList): #臺中市所有公車路線名稱
        
                
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
        
    
    def allBusStepsNum(busList,busIDList): #該路線去程站數量及回程站數量
        
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
          
    
    def searchStepName(lang,stepNameCN,stepNameEN,busList): #查站點名稱（中文/英文），暫時只有中文
        
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