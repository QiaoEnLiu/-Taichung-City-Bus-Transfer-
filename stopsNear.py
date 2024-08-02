# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:14:07 2024

@author: User
"""
from Bus_OOP import Stop
from FilePath_OOP import FilePath

theStop = Stop()

pathDir = FilePath("臺中市市區公車站牌資料", "CSV").path()    
busList = theStop.readFile(pathDir)

if __name__ =='__main__':
    
    # la, lo=input('').split(',')
    # print(la, lo)
    
    
    stopNameList=[]
    for i in busList:
        tempLocat = {
            theStop.stopName_CN:i[theStop.stopName_CN],
            theStop.stopName_EN:i[theStop.stopName_EN],
            theStop.latitude:i[theStop.latitude],
            theStop.longitude:i[theStop.longitude]
            }
        
        theStop.unduplicateList(stopNameList, tempLocat)
        
    print(stopNameList)