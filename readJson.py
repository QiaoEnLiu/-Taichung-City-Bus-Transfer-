from FilePath_OOP import FilePath
from Bus_OOP import Stop

theStop = Stop()

pathDir = FilePath("臺中市市區公車站細部資訊", "JSON").path()    
busList = theStop.readJson_File(pathDir)

#region Find Stop
'''
for stop in busList:
    if stop[theStop.stopName_CN] == "吉峰東自強路口":
        print(stop)
'''
#endregion

#region Find BusInfo

'''
for stop in busList:
    if "132" in stop[theStop.roundTrip_ob] or "132" in stop[theStop.roundTrip_ib]:
        print(stop)
'''

#endregion

#region Take Bus(Direct)


takeStop = "國立臺中科技大學"
desStop = "朝陽科技大學" #國立臺中科技大學 吉峰東自強路口 朝陽科技大學

takeInfo = []
for stop in busList:
    if stop[theStop.stopName_CN] == takeStop:
        takeInfo.append(stop)

desInfo = []
for stop in busList:
    if stop[theStop.stopName_CN] == desStop:
        desInfo.append(stop)



for takeBus in takeInfo:
    for desStop in desInfo:
        
        sameBusesOB = set(takeBus[theStop.roundTrip_ob].keys()) & set(desStop[theStop.roundTrip_ob].keys())
        if sameBusesOB:
            for bus in sameBusesOB:
                if int(takeBus[theStop.roundTrip_ob][bus][1]) < int(desStop[theStop.roundTrip_ob][bus][1]):
                    print(takeBus[theStop.roundTrip_ob][bus], desStop[theStop.roundTrip_ob][bus])

        sameBusesIB = set(takeBus[theStop.roundTrip_ib].keys()) & set(desStop[theStop.roundTrip_ib].keys())
        if sameBusesIB:
            for bus in sameBusesIB:
                if int(takeBus[theStop.roundTrip_ib][bus][1]) < int(desStop[theStop.roundTrip_ib][bus][1]):
                    print(takeBus[theStop.roundTrip_ib][bus], desStop[theStop.roundTrip_ib][bus])
    
        '''
        print(takeBus, desStop, sep = '\n')
        print("-------")
        print("RT_OB: ", set(takeBus[theStop.roundTrip_ob].keys()) & set(desStop[theStop.roundTrip_ob].keys()))
        print("RT_IB: ", set(takeBus[theStop.roundTrip_ib].keys()) & set(desStop[theStop.roundTrip_ib].keys()))
        print("--------------")
        input("Press Enter")
        '''
        

#endregion

