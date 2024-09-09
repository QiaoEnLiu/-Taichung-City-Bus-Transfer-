# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:54:46 2024

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Stop

theStop = Stop()


if __name__ =='__main__':
    pathDir = FilePath("臺中市市區公車站牌資料", "CSV").path()    
    busList = theStop.readFile(pathDir)
    
    
    stopInfo = []    
    for bus in busList:
        
        
        
        if not any(theStop.stopExist(bus, stop) for stop in stopInfo):
            
            tempDict = theStop.stopInfoDict(bus)
            '''
            
            if bus[theStop.roundTrip] == theStop.roundTrip_ob:
                
                tempDict[theStop.roundTrip_ob + theStop.busID].append(bus[theStop.busID])
                
            elif  bus[theStop.roundTrip] == theStop.roundTrip_ib:
                
                tempDict[theStop.roundTrip_ib + theStop.busID].append(bus[theStop.busID])
            '''
                
            stopInfo.append(tempDict)
                        
            
        for stop in stopInfo:
            
            if theStop.stopExist(bus, stop):
                
                if bus[theStop.busID] not in stop[bus[theStop.roundTrip] + theStop.busID]:
                    
                    stop[bus[theStop.roundTrip] + theStop.busID].append(bus[theStop.busID])
                       
                '''
                if (bus[theStop.roundTrip] == theStop.roundTrip_ob and 
                bus[theStop.busID] not in stop[bus[theStop.roundTrip] + theStop.busID]):
                    
                    stop[bus[theStop.roundTrip] + theStop.busID].append(bus[theStop.busID])
                    
                elif (bus[theStop.roundTrip] == theStop.roundTrip_ib and
                bus[theStop.busID] not in stop[bus[theStop.roundTrip] + theStop.busID]):
                    
                    stop[bus[theStop.roundTrip] + theStop.busID].append(bus[theStop.busID])
                '''
        

            
            
    # for stop in stopInfo:
    #     print(stop)
                
        
            