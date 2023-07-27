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
        if busID == i['路線']:        
            stopsList.append(i)
           

    if len(stopsList)==0:
        print('目前臺中市內尚未有此公車')
    
    else:
    
        tempBound=''
        for i in stopsList:
            if tempBound == '' or tempBound != i['方向']:
                tempBound=i['方向']
                print("-------------------------\n")
                print(f"{busID}路線：[{i['路線名稱']}]")
                print(f"--{i['方向']}")
                print("--------------")
                
            print(i['站序'],i['中文站點名稱'],i['英文站點名稱'],i['經度'],i['緯度'],sep=", ")
    