# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:53:44 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Stop


if __name__ =='__main__':
    #查站點名稱，中文站名比對（輸出只有站名）
    
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()    
    busList=Stop.readFile(pathDir)
  
    # busListDF=Bus.readOnlineFile()
    # busList=busListDF.to_dict('records') 
    
    #lang=input('查詢站點「臺中車站」 Seach Stop Name(Taichung Station)\n輸入語言 Input language for step name(CN/EN):')
    
    stopNameCN="臺中車站"
    stopNameEN="Taichung Station"
    
    # 臺中車站, 高鐵臺中站
    # Taichung Station, HSR Taichung Station
    
    CN_Name=Stop.stopName_CN    
    EN_Name=Stop.stopName_EN
        
    stopsList=[]
    stopsSort=[]
    stopsNameList=[]
    stopsInfo=[]
  
    #stopsList=Stop.searchStopName(lang, stopNameCN,stopNameEN, busList)
    stopsList=Stop.searchStopName('CN', stopNameCN,stopNameEN, busList)


    stopsSort=sorted(stopsList,key=lambda x: (x[Stop.stopName_CN],x[Stop.latitude]))
    tempStopNameLaLo=''
    print()
    for i in stopsSort:
        if tempStopNameLaLo == '' or \
        tempStopNameLaLo != (i[Stop.stopName_CN]+','+str(i[Stop.latitude])+','+str(i[Stop.longitude])):
                
            stopsNameList.append(i)
            tempStopNameLaLo=i[Stop.stopName_CN]+','+str(i[Stop.latitude])+','+str(i[Stop.longitude])
            # stopsInfo.append({Stop.stopName_CN:i[Stop.stopName_CN],
            #                   Stop.latitude:str(i[Stop.latitude]),
            #                   Stop.longitude:str(i[Stop.longitude])})
            print(i[Stop.stopName_CN],i[Stop.stopName_EN],i[Stop.latitude],i[Stop.longitude])
    
    # for i in stopsInfo:
    #     print(i)
    #     for j in stopsSort:
                        
    #         if i[Stop.stopName_CN]== j[Stop.stopName_CN] and \
    #         str(i[Stop.latitude]) == j[Stop.latitude] and \
    #         str(i[Stop.longitude]) ==j[Stop.longitude]:
                
    #             print("--",j[Stop.busID],j[Stop.busName],j[Stop.roundTrip],j[Stop.stopID])
                
    #     print()
                
                    
                                                                                       