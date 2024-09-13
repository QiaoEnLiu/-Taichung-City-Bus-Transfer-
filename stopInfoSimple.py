# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:54:46 2024

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Stop

import json

theStop = Stop()


pathDir = FilePath("臺中市市區公車站牌資料", "CSV").path()    
busList = theStop.readFile(pathDir)
    
    
stopInfo = []    
for bus in busList:
        
        
    if not any(theStop.stopExist(bus, stop) for stop in stopInfo):
            
        tempDict = theStop.stopInfoDict(bus)                
        stopInfo.append(tempDict)
                        
            
    for stop in stopInfo:
            
        if theStop.stopExist(bus, stop):
                
            if bus[theStop.busID] not in stop[bus[theStop.roundTrip]]:
                    
                # stop[bus[theStop.roundTrip]].append(bus[theStop.busID] + "_" + bus[theStop.stopID])
                stop[bus[theStop.roundTrip]].update({bus[theStop.busID] : [bus[theStop.busID], bus[theStop.stopID]]})
                       

with open(FilePath("臺中市市區公車站細部資訊", "JSON").path(), "w", encoding="utf-8") as jsonfile:
    json.dump(stopInfo, jsonfile, ensure_ascii=False, indent=4)
                
        
            