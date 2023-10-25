158# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:59:39 2023

@author: User
"""
#from FilePath_OOP import FilePath
from Bus_OOP import Bus

if __name__ =='__main__':
    #該公車路線
    
    #pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()    
    #busList=Bus.readFile(pathDir)
  
    busListDF=Bus.readOnlineFile()
    busList=busListDF.to_dict('records') 
    
    busID=input('請輸入路線：')
           
    stopsList=[]
    
    #Bus.linesAtStop(busID,stopsList,busList)
    for i in busList:
        if busID == i[Bus.busID]:        
            stopsList.append(i)
           

    if len(stopsList)==0:
        print('目前臺中市內尚未有此公車')
    
    else:
    
        tempBound=''
        for i in stopsList:
            if tempBound == '' or tempBound != i[Bus.roundTrip]:
                tempBound=i[Bus.roundTrip]
                print("-------------------------\n")
                print(f"{busID}路線：[{i[Bus.busName]}]")
                print(f"--{i[Bus.roundTrip]}")
                print("--------------")
                
            print(i[Bus.stopID],i[Bus.stopName_CN],i[Bus.stopName_EN],i[Bus.latitude],i[Bus.longitude],sep=", ")
    