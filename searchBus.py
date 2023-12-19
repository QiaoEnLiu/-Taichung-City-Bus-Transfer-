158# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:59:39 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Stop

if __name__ =='__main__':
    #該公車路線
    
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()    
    busList=Stop.readFile(pathDir)
  
    # busListDF=Stop.readOnlineFile()
    # busList=busListDF.to_dict('records') 
    
    busID=input('請輸入路線：')
           
    stopsList=[]
    
    #Stop.linesAtStop(busID,stopsList,busList)
    for i in busList:
        if busID == i[Stop.busID]:        
            stopsList.append(i)
           

    if len(stopsList)==0:
        print('目前臺中市內尚未有此公車')
    
    else:  
        tempBound=''
        for i in stopsList:
            if tempBound == '' or tempBound != i[Stop.roundTrip]:
                tempBound=i[Stop.roundTrip]
                print("-------------------------\n")
                print(f"{busID}路線：[{i[Stop.busName]}]")
                print(f"--{i[Stop.roundTrip]}")
                print("--------------")
                
            print(i[Stop.stopID],i[Stop.stopName_CN],i[Stop.stopName_EN],i[Stop.latitude],i[Stop.longitude],sep=", ")
    