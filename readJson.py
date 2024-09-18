import pandas as pd
import json

def betweenStr(string):
    start = string.find('起點')
    end = string.find('沿途')

    if start != -1 and end != -1 and start < end:
        return string[start + 1:end]
        return None
    

filePath = r'Resource/臺中市區公車路線圖.JSON'

with open(filePath,'r') as file:
    jsonFile = json.load(file)

bus = '132路'

stop = '國立臺中科技大學'


for row in jsonFile:

    # if row['路線'] == bus:
    #     print(row)

    # if row['路線'] == bus:
    #     print(row['去程'].split(':')[1].split('、'))
    #     print(stop in row['去程'].split(':')[1].split('、'))
    #     print(stop in row['回程'].split(':')[1].split('、'))

    if stop in row['去程'].split(':')[1].split('、'):
        print(row)

