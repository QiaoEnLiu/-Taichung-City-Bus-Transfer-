# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:24:44 2023

@author: User
"""
import csv
import pandas as pd

class Stop:
    
    def __init__(self):
        
        self.busesID=[] #行經該站點的公車
        self.lines=[] #行經該站點公車路線
        self.lineStops=[] #在每條路線上的該站點

class Bus:
    
    #Resource/臺中市市區公車站牌資料.CSV    
    
    '''
    def __init__(self,busID,busName,roundTrip,stopID,stopName_CN,stopName_EN,latitude,longitude): #針對公車CSV檔欄位所呈現的物件Bus，但目前用不到
                
        self.busID=busID #路線：路線編號
        self.busName=busName #路線名稱：名稱為「端點A站 - 端點B站」
        self.roundTrip=roundTrip #方向：路線名稱「端點A站 - 端點B站」為去程(outbound)，「端點A站」為發車站，站序1；而回程(inbound)以「端點B站」發車，「端點B站」站序為1，為回程發車站
        self.stop=stopID #站序：發車站點（端點）為1，數字遞增為行車方向
        self.stopName_CN=stopName_CN #中文站點名稱
        self.stopName_EN=stopName_EN #English Stop Name
        self.latitude=latitude #經度
        self.longitude=longitude #緯度
        
        '''
    
        
    busID='路線' #路線：路線編號 / Bus.busID
    busName='路線名稱' #路線名稱：名稱為「端點A站 - 端點B站」 / Bus.busName
    roundTrip='方向' #方向 / Bus.roundTrip
    stopID='站序' #站序：發車站點（端點）為1，數字遞增為行車方向 / Bus.stopID
    stopName_CN='中文站點名稱' #中文站點名稱 / Bus.stopName_CN
    stopName_EN='英文站點名稱' #English Stop Name / Bus.stopName_EN
    latitude='經度' #經度 / Bus.latitude
    longitude='緯度' #緯度 / Bus.longitude
    
    #路線方向分為兩種
    roundTrip_ob='去程' #路線名稱「端點A站 - 端點B站」為去程(outbound)，「端點A站」為發車站 / Bus.roundTrip_ob
    roundTrip_ib='回程' #回程(inbound)以「端點B站」發車 / Bus.roundTrip_ib
    

    def readOnlineFile(): #讀取「臺中市市區公車站牌資料」url
        
        url='https://datacenter.taichung.gov.tw/swagger/OpenData/2dd516a9-510f-424e-91d8-17dae9cedf99'
        df=pd.read_csv(url,encoding='big5')
        return df
        #return df.to_dict('records')

    def readFile(filePath): #讀檔
        
        busList=[]             
        with open(filePath,newline='',encoding='big5') as csvFile:   #encoding='utf-8-sig'     
            rows=csv.DictReader(csvFile)
            for row in rows:
                busList.append(row)                       
        csvFile.close()
        return busList
    


    def IDsAtStop(stop,busList): #查行經該站點的路線編號
       
        busIDList=[]
        temp=''
        for i in busList:
            if stop in i[Bus.stopName_CN]:
                if temp == '' or temp != i[Bus.busID]:  
                    busIDList.append(i[Bus.busID])
                    temp=i[Bus.busID]
        return busIDList

    

    def busesAtStop(takeStop,busList): #查行經該站點的路線（該站點行）
    
        busIDList=[]
        for i in busList:
            if takeStop in i[Bus.stopName_CN]:
                busIDList.append(i)
        return busIDList
    
        

    def sameBus(desBus,takeBus): #轉乘程式碼中，判斷是否需要轉乘
            
        for i in desBus:
            for j in takeBus:
                if i == j:
                    return i == j
        
                                   
    def stopInfo(busesID,busList): #站牌路線資訊（列出行經該站的公車路線，要先由IDsAtStop函式前找出行經該站的路線編號，再透過路線編號從已讀取的資料集串列，找出每條路線上的每個站點）
             
        busLine=[]
        for i in busesID:
            tempList=[] 
            for j in busList:
                if i == j[Bus.busID]:        
                    tempList.append(j)
            busLine.extend(tempList)
            
        return busLine
                

    def linesAtStop(busID,tempList,busList): #路線延站
        
        for i in busList:
            if busID == i[Bus.busID]:        
                tempList.append(i)
                                            
              
    def sameStops(bus1,bus2,busList): #兩條硌線相同站點
        
        bus1Stops=[]
        bus2Stops=[]
        sameStops=[]        
        Bus.linesAtStop(bus1,bus1Stops,busList)
        Bus.linesAtStop(bus2,bus2Stops,busList)        
        for i in bus1Stops:
            for j in bus2Stops:
                if i[Bus.stopName_CN] == j[Bus.stopName_CN]:
                    sameStops.append(i)
                    sameStops.append(j)
                    break
                
        return sameStops
        
    
    def stopsVector(take, des): #撘乘站與目的地站是否在同一條路線、同個方向，且以前兩狀況下目的地站是否在撘乘站之後
        
        return take[Bus.busID] == des[Bus.busID] and take[Bus.roundTrip] == des[Bus.roundTrip] and int(take[Bus.stopID]) < int(des[Bus.stopID])
        
                
    def allBusID(busList): #臺中市所有公車路線編號
        
        busIDList=[]
        tempID=''
        #buses=0        
        for i in busList:
            if tempID == '' or tempID != i[Bus.busID]:
                busIDList.append(i[Bus.busID])
                tempID=i[Bus.busID]
        #buses=len(busIDList)
        #print("臺中市公車共",buses,"條路線") 
        return busIDList
        
        
    def allBusName(busList): #臺中市所有公車路線名稱
        
                
        busNameList=[]
        tempBusName=''        
        for i in busList:
            tempList=[]
            if tempBusName == '' or tempBusName != i[Bus.busName]:
                tempList.append(i[Bus.busID])
                tempList.append(i[Bus.busName])
                busNameList.append(tempList)
                tempBusName=i[Bus.busName]                
        return busNameList      
        
    
    def allBusStopsNum(busList,busIDList): #該路線去程站數量及回程站數量
        
        listStopsNum=[]        
        for i in range(len(busIDList)):
            listTemp=[]
            stopsOB=0
            stopsIB=0              
            for row in busList:
                if busIDList[i]==row[Bus.busID]:                    
                    if Bus.roundTrip_ob==row[Bus.roundTrip]:                
                        stopsOB+=1                         
                    if Bus.roundTrip_ib==row[Bus.roundTrip]:                        
                        stopsIB+=1                                      
            listTemp.append(busIDList[i])
            listTemp.append(stopsOB)
            listTemp.append(stopsIB)
            listStopsNum.append(listTemp)         
            
        #串列[['路線'],去程站數量,回程站數量]    
        return listStopsNum
          
    
    def searchStopName(lang,stopNameCN,stopNameEN,busList): #查站點名稱（中文/英文），暫時只有中文
        
        stopsList=[]
        CN_Name=Bus.stopName_CN    
        EN_Name=Bus.stopName_EN
        stopName=""        
        langField=""        
        if lang=="CN":
            langField=CN_Name
            stopName=stopNameCN
        elif lang=="EN":
            langField=EN_Name
            stopName=stopNameEN            
        for i in busList:
            if stopName in i[langField]:
                stopsList.append(i)                
        return stopsList