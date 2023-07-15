# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:19:49 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Bus

if __name__ =='__main__':
    #bus1上哪些站點可以撘bus2（無輸出）
    
    bus1='131'
    bus2='25'
    
    busListCSV=[]
    sameSteps=[]
        
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    busListCSV=Bus.readFile(pathDir)
    
    sameSteps=Bus.sameSteps(bus1,bus2,busListCSV) 
                
    