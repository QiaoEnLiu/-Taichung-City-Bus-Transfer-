# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:39:12 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Bus

if __name__ =='__main__':
    #該站點上所有公車路線延站（無輸出）
    
    stopName='朝陽科技大學'
    
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    busListCSV=Bus.readFile(pathDir)
    
    # 朝陽科技大學, 吉峰東自強路口

    # 臺中車站, 高鐵臺中站, 臺中市政府, 新光三越
        
    # 逢甲大學(福星路)
    
    busesID=[] #行經該站點公車
    busesID=Bus.IDsAtStop(stopName,busListCSV)
    
    busesLine=[] #行經該站點公車路線，如同該站牌上的路線
    busesLine=Bus.stopInfo(busesID,busListCSV) 
    
    

    
    
    