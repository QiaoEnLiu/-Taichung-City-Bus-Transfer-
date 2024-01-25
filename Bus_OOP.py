# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:24:44 2023

@author: User
"""
import csv
import pandas as pd

class BusLine:
    
    def __init__(self):
        
        self.busesID=[] #行經該站點的公車編號
        self.lines=[] #行經該站點公車路線
        self.lineStops=[] #在每條路線上的該站點

class Stop:
    
    #Resource/臺中市市區公車站牌資料.CSV    
    
    '''
    def __init__(self,busID,busName,roundTrip,stopID,stopName_CN,stopName_EN,latitude,longitude): #針對公車CSV檔欄位所呈現的物件Bus，但目前用不到
                
        self.busID=busID #路線：路線編號
        self.busName=busName #路線名稱：名稱為「端點A站 - 端點B站」
        self.roundTrip=roundTrip #方向：路線名稱「端點A站 - 端點B站」為去程(outbound)，「端點A站」為發車站，站序1；而回程(inbound)以「端點B站」發車，「端點B站」站序為1，為回程發車站
        self.stop=stopID #站序：發車站點（端點）為1，數字遞增為行車方向，也可稱「向量」
        self.stopName_CN=stopName_CN #中文站點名稱
        self.stopName_EN=stopName_EN #English Stop Name
        self.latitude=latitude #經度
        self.longitude=longitude #緯度
        
        '''
    
        
    busID='路線' #路線：路線編號 / Stop.busID
    busName='路線名稱' #路線名稱：名稱為「端點A站 - 端點B站」 / Stop.busName
    roundTrip='方向' #方向 / Stop.roundTrip
    stopID='站序' #站序：發車站點（端點）為1，數字遞增為行車方向，也可稱「向量」 / Stop.stopID
    stopName_CN='中文站點名稱' #中文站點名稱 / Stop.stopName_CN
    stopName_EN='英文站點名稱' #English Stop Name / Stop.stopName_EN
    latitude='經度' #經度 / Stop.latitude
    longitude='緯度' #緯度 / Stop.longitude
    
    #路線方向分為兩種
    roundTrip_ob='去程' #路線名稱「端點A站 - 端點B站」為去程(outbound)，「端點A站」為發車站 / Stop.roundTrip_ob
    roundTrip_ib='回程' #回程(inbound)以「端點B站」發車 / Stop.roundTrip_ib
    

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
            if stop in i[Stop.stopName_CN]:
                if temp == '' or temp != i[Stop.busID]:  
                    busIDList.append(i[Stop.busID])
                    temp=i[Stop.busID]
        return busIDList

    

    def busesAtStop(takeStop,busList): #查行經該站點的路線編號（包括該站點行）
    
        busIDList=[]
        for i in busList:
            if takeStop in i[Stop.stopName_CN]:
                busIDList.append(i)
        return busIDList
    
        

    def sameBus(desBus,takeBus): #轉乘程式碼中，判斷是否需要轉乘
            
        for i in desBus:
            for j in takeBus:
                if i == j:
                    return i == j
        
                                   
    def stopInfo(busesID,busList): #站牌路線資訊
        #列出行經該站的公車路線，要先由IDsAtStop函式前找出行經該站的路線編號，再透過路線編號從已讀取的資料集串列，找出每條路線上的每個站點
        
        busLine=[]
        for i in busesID:
            tempList=[] 
            for j in busList:
                if i == j[Stop.busID]:        
                    tempList.append(j)
            busLine.extend(tempList)
            
        return busLine
                

    def linesAtStop(busID,tempList,busList): #路線延站
        
        for i in busList:
            if busID == i[Stop.busID]:        
                tempList.append(i)
                                            
              
    def sameStops(bus1,bus2,busList): #兩條硌線相同站點
        
        bus1Stops=[]
        bus2Stops=[]
        sameStops=[]        
        Stop.linesAtStop(bus1,bus1Stops,busList)
        Stop.linesAtStop(bus2,bus2Stops,busList)        
        for i in bus1Stops:
            for j in bus2Stops:
                if i[Stop.stopName_CN] == j[Stop.stopName_CN]:
                    sameStops.append(i)
                    sameStops.append(j)
                    break
                
        return sameStops
        
    
    def stopsVector(take, des): #撘乘站與目的地站是否在同一條路線、同個方向、目的地站是否在撘乘站之後
        
        sameBus = take[Stop.busID] == des[Stop.busID]
        sameDirection = take[Stop.roundTrip] == des[Stop.roundTrip]
        takeToDes = int(take[Stop.stopID]) < int(des[Stop.stopID])
    
        return sameBus and sameDirection and takeToDes
        
                
    def allBusID(busList): #臺中市所有公車路線編號
        
        busIDList=[]
        tempID=''
        #buses=0        
        for i in busList:
            if tempID == '' or tempID != i[Stop.busID]:
                busIDList.append(i[Stop.busID])
                tempID=i[Stop.busID]
        #buses=len(busIDList)
        #print("臺中市公車共",buses,"條路線") 
        return busIDList
        
        
    def allBusName(busList): #臺中市所有公車路線名稱
        
                
        busNameList=[]
        tempBusName=''        
        for i in busList:
            tempList=[]
            if tempBusName == '' or tempBusName != i[Stop.busName]:
                tempList.append(i[Stop.busID])
                tempList.append(i[Stop.busName])
                busNameList.append(tempList)
                tempBusName=i[Stop.busName]                
        return busNameList      
        
    
    def allBusStopsNum(busList,busIDList): #該路線去程站數量及回程站數量
        
        listStopsNum=[]        
        for i in range(len(busIDList)):
            listTemp=[]
            stopsOB=0
            stopsIB=0              
            for row in busList:
                if busIDList[i]==row[Stop.busID]:                    
                    if Stop.roundTrip_ob==row[Stop.roundTrip]:                
                        stopsOB+=1                         
                    if Stop.roundTrip_ib==row[Stop.roundTrip]:                        
                        stopsIB+=1                                      
            listTemp.append(busIDList[i])
            listTemp.append(stopsOB)
            listTemp.append(stopsIB)
            listStopsNum.append(listTemp)         
            
        #串列[['路線'],去程站數量,回程站數量]    
        return listStopsNum
          
    
    def searchStopName(lang,stopNameCN,stopNameEN,busList): #查站點名稱（中文/英文），暫時只有中文
        
        stopsList=[]
        CN_Name=Stop.stopName_CN    
        EN_Name=Stop.stopName_EN
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