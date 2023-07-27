# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:39:12 2023

@author: User
"""
from FilePath_OOP import FilePath
from Bus_OOP import Bus



if __name__ =='__main__':
    #站牌資訊，該站點上所有公車路線
    
    stopName='朝陽科技大學'
    
    pathDir=FilePath("臺中市市區公車站牌資料", "CSV").path()
    busListCSV=Bus.readFile(pathDir)
    
    # 朝陽科技大學, 吉峰東自強路口

    # 臺中車站, 高鐵臺中站, 臺中市政府, 新光三越
        
    # 逢甲大學(福星路)
    
    busIDList=[]
    stopsSort=[]
    stopsName=[]
    
    for i in busListCSV:
        if stopName in i['中文站點名稱']:
            busIDList.append(i)
            
    stopsSort=sorted(busIDList,key=lambda x: x['中文站點名稱'])

    tempName=''
    for i in stopsSort:
        if tempName=='' or tempName!=i['中文站點名稱']:
            tempName=i['中文站點名稱']
            print("---------")
            print(f"\n{i['中文站點名稱']}",f"{i['英文站點名稱']},",f"({i['經度']},{i['緯度']})\n---------")
        if tempName == i['中文站點名稱']:
            print(i['路線'],i['方向'],f"[{i['站序']}]")
    print("---------")

     
    
    

    
    
    