from FilePath_OOP import FilePath
from Bus_OOP import Stop

theStop = Stop()

pathDir = FilePath("臺中市市區公車站細部資訊", "JSON").path()    
busList = theStop.readJson_File(pathDir)

for stop in busList:
    if stop[theStop.stopName_CN] == "三民林森路口":
        print(stop)