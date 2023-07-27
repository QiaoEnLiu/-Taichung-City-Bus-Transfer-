# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:19:49 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Bus

if __name__ =='__main__':
    #bus1路線上哪些站點與bus2路線有著一模一樣的站點名稱（無輸出）
    
    bus1='131'
    bus2='25'
    
    busListCSV=[]
    sameStops=[]
        
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    busListCSV=Bus.readFile(pathDir)
    
    sameStops=Bus.sameStops(bus1,bus2,busListCSV) 
                
    