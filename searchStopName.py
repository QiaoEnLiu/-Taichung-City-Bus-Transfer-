# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:53:44 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Stop

theStop = Stop()


if __name__ =='__main__':
    #查站點名稱，中文站名比對（輸出只有站名）
    
    pathDir = FilePath("臺中市市區公車站牌資料", "CSV").path()    
    busList = theStop.readFile(pathDir)
  
    # busListDF = theStop.readOnlineFile()
    # busList = busListDF.to_dict('records') 
    
    #lang = input('查詢站點「臺中車站」 Seach Stop Name(Taichung Station)\n輸入語言 Input language for step name(CN/EN):')
    
    stopNameCN = "臺中車站"
    stopNameEN = "Taichung Station"
    
    # 臺中車站, 高鐵臺中站
    # Taichung Station, HSR Taichung Station
    
    CN_Name = theStop.stopName_CN    
    EN_Name = theStop.stopName_EN
        
    stopsList = []
    stopsSort = []
    stopsNameList = []
    stopsInfo = []
  
    #stopsList=theStop.searchStopName(lang, stopNameCN, stopNameEN, busList)
    stopsList=theStop.searchStopName('CN', stopNameCN, stopNameEN, busList)


    stopsSort=sorted(stopsList,key=lambda x: (x[theStop.stopName_CN], x[theStop.latitude]))
    tempStopNameLaLo=''
    print()
    for i in stopsSort:
        if tempStopNameLaLo == '' or \
        tempStopNameLaLo != (i[theStop.stopName_CN]+','+str(i[theStop.latitude])+','+str(i[theStop.longitude])):
                
            stopsNameList.append(i)
            tempStopNameLaLo=i[theStop.stopName_CN]+','+str(i[theStop.latitude])+','+str(i[theStop.longitude])
            # stopsInfo.append({theStop.stopName_CN:i[theStop.stopName_CN],
            #                   theStop.latitude:str(i[theStop.latitude]),
            #                   theStop.longitude:str(i[theStop.longitude])})
            print(i[theStop.stopName_CN],i[theStop.stopName_EN],i[theStop.latitude],i[theStop.longitude])
    
    # for i in stopsInfo:
    #     print(i)
    #     for j in stopsSort:
                        
    #         if i[theStop.stopName_CN] == j[theStop.stopName_CN] and \
    #         str(i[theStop.latitude]) == j[theStop.latitude] and \
    #         str(i[theStop.longitude]) == j[theStop.longitude]:
                
    #             print("--",j[theStop.busID], j[theStop.busName], j[theStop.roundTrip], j[theStop.stopID])
                
    #     print()
                
                    
                                                                                       