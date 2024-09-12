# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:59:39 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Stop

theStop = Stop()


if __name__ =='__main__':
    #該公車路線
    
    pathDir = FilePath("臺中市市區公車站牌資料", "CSV").path()    
    busList = theStop.readFile(pathDir)
  
    # busListDF = theStop.readOnlineFile()
    # busList = busListDF.to_dict('records') 
    
    busID = input('請輸入路線：')
           
    stopsList = []
    
    #theStop.linesAtStop(busID,stopsList,busList)
    for i in busList:
        if busID == i[theStop.busID]:        
            stopsList.append(i)
           

    if len(stopsList) == 0:
        print('目前臺中市內尚未有此公車')
    
    else:
        
        tempBound=''
        for i in stopsList:
            if tempBound == '' or tempBound != i[theStop.roundTrip]:
                tempBound=i[theStop.roundTrip]
                print("-------------------------\n")
                print(f"{busID}路線：[{i[theStop.busName]}]")
                print(f"--{i[theStop.roundTrip]}")
                print("--------------")
                
            print(i[theStop.stopID], i[theStop.stopName_CN], i[theStop.stopName_EN], i[theStop.latitude], i[theStop.longitude], sep=", ")
    