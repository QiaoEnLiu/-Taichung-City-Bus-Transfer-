# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:14:07 2024

@author: User
"""
from Bus_OOP import Stop
from FilePath_OOP import FilePath

pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()    
busList=Stop.readFile(pathDir)

if __name__ =='__main__':
    
    # la, lo=input('').split(',')
    # print(la, lo)
    
    
    stopNameList=[]
    for i in busList:
        tempLocat={Stop.stopName_CN:i[Stop.stopName_CN],
                   Stop.stopName_EN:i[Stop.stopName_EN],
                   Stop.latitude:i[Stop.latitude],
                   Stop.longitude:i[Stop.longitude]}
        Stop.unduplicateList(stopNameList, tempLocat)
        
    print(stopNameList)