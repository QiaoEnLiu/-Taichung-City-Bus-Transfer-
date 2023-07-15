# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:45:11 2023

@author: User
"""
class FilePath:
    
    def __init__(self,fileName,extName):
        
        self.resDir='Resource/' #檔案路徑
        self.fileName=fileName #檔名
        self.extName='.'+extName #副檔名
        
    def path(self):
            
        return self.resDir+self.fileName+self.extName