from FilePath_OOP import FilePath
from Bus_OOP import Stop

#region Read Json File
theStop = Stop()
pathDir = FilePath("臺中市市區公車站細部資訊", "JSON").path()    
# pathDir = FilePath("測試資料集1", "JSON").path()   

busList = theStop.readJson_File(pathDir)
#endregion

CYUT = "朝陽科技大學"
FCU_FSR = "逢甲大學(福星路)"
NTUT = "國立臺中科技大學"
testStop = "吉峰東自強路口"

defaultBusID = "132"


#region Find Stop
def findStop():

    findStopName = input("尋找站點（{}）：".format(NTUT)) or NTUT
    findStopList = []
    for stop in busList:
        if stop[theStop.stopName_CN] == findStopName:
            findStopList.append(stop)
            print(stop[theStop.roundTrip_ob].keys(),stop[theStop.roundTrip_ib].keys(), sep = '\n')

#endregion

#region Find BusInfo

def findBusInfo():
    findBusID = input("尋找公車（{}）：".format(defaultBusID)) or defaultBusID 
    for stop in busList:
        if findBusID in stop[theStop.roundTrip_ob] or findBusID in stop[theStop.roundTrip_ib]:
            print(stop)


#endregion




#region Take Bus
def takeBus():

    #region Take Bus

    takeStopName = input("撘乘站({})：".format(CYUT)) or CYUT
    # takeStopName = "K"
    print("---------------", f"你的撘乘站：{takeStopName}", "---------------", sep = '\n')
    desStopName = input("目的地({})：".format(FCU_FSR)) or FCU_FSR
    # desStopName = "B"
    print("---------------", f"你的目的地：{desStopName}", "---------------", sep = '\n')
    #endregion



    #region Find Stop Before Taking Bus
    takeInfo = []
    desInfo = []
    for stop in busList:
        if stop[theStop.stopName_CN] == takeStopName:
            # print(stop)
            takeInfo.append(stop)
        
        if stop[theStop.stopName_CN] == desStopName:
            # print(stop)
            desInfo.append(stop)
    #endregion



    #region Take Bus Check Direct

    print("可直達的公車：", "------", sep = '\n')    
    sameBusesOB = []
    sameBusesIB = []
    for takeBus in takeInfo:
        for desStop in desInfo:
            
            obList = list(set(takeBus[theStop.roundTrip_ob].keys()) & set(desStop[theStop.roundTrip_ob].keys()))
            if obList:
                for bus in obList:
                    if int(takeBus[theStop.roundTrip_ob][bus][1]) < int(desStop[theStop.roundTrip_ob][bus][1]):
                        print(takeBus[theStop.roundTrip_ob][bus], desStop[theStop.roundTrip_ob][bus])
                    sameBusesOB.append(obList)


            ibList = list(set(takeBus[theStop.roundTrip_ib].keys()) & set(desStop[theStop.roundTrip_ib].keys()))
            if ibList:
                for bus in ibList:
                    if int(takeBus[theStop.roundTrip_ib][bus][1]) < int(desStop[theStop.roundTrip_ib][bus][1]):
                        print(takeBus[theStop.roundTrip_ib][bus], desStop[theStop.roundTrip_ib][bus])
                    sameBusesIB.append(ibList)
        
            '''
            print(takeBus, desStop, sep = '\n')
            print("-------")
            print("RT_OB: ", set(takeBus[theStop.roundTrip_ob].keys()) & set(desStop[theStop.roundTrip_ob].keys()))
            print("RT_IB: ", set(takeBus[theStop.roundTrip_ib].keys()) & set(desStop[theStop.roundTrip_ib].keys()))
            print("--------------")
            input("Press Enter")
            '''
    # print(sameBusesOB, type(sameBusesOB), sameBusesOB == None, len(sameBusesOB) == 0)
    
    #endregion
    
    #region Transfer Bus
    if len(sameBusesOB) is None and len(sameBusesIB) is None:

        print(f"{takeStopName} 前往 {desStopName} 需要轉乘", "---------------", sep = '\n')
    
        to_TF_Stops = []
        TF_to_Stops = []

        takeBusesInfo = []
        desBusesInfo = []


        #region Find Transfer Stop

        #region Find Take to Transfer
        for take in takeInfo:
            for bus in list(take[theStop.roundTrip_ob].keys()):
                for stop in busList:
                    if bus in stop[theStop.roundTrip_ob]:
                        if stop not in to_TF_Stops:
                            to_TF_Stops.append(stop)             
                        if bus not in takeBusesInfo:
                            takeBusesInfo.append(bus)
                            
            for bus in list(take[theStop.roundTrip_ib].keys()):
                for stop in busList:
                    if bus in stop[theStop.roundTrip_ib]:
                        if stop not in to_TF_Stops:
                            to_TF_Stops.append(stop)
                        if bus not in takeBusesInfo:
                            takeBusesInfo.append(bus)
                            
        #endregion

        #region Find Transfer to Des
        for des in desInfo:
            for bus in list(des[theStop.roundTrip_ob].keys()):
                for stop in busList:
                    if bus in stop[theStop.roundTrip_ob]:
                        if stop not in TF_to_Stops:
                            TF_to_Stops.append(stop)
                        if bus not in desBusesInfo:
                            desBusesInfo.append(bus)
                            
            for bus in list(des[theStop.roundTrip_ib].keys()):
                for stop in busList:
                    if bus in stop[theStop.roundTrip_ib]:
                        if stop not in TF_to_Stops:
                            TF_to_Stops.append(stop)
                        if bus not in desBusesInfo:
                            desBusesInfo.append(bus)
        #endregion
        #endregion

                            
        tf = [stop for stop in to_TF_Stops if stop in TF_to_Stops]
        #endregion


        #region Bus to Transfer
        tfBuses = []
        for stop in tf:
            for bus in list(stop[theStop.roundTrip_ob].keys()):
                if bus not in tfBuses:
                    tfBuses.append(bus)
            
            for bus in list(stop[theStop.roundTrip_ib].keys()):
                if bus not in tfBuses:
                    tfBuses.append(bus)
                    
        take2TF_Buses = sorted(list(set(takeBusesInfo) & set(tfBuses)))
        #endregion

        #region Select Bus Take to Transfer

        print("可撘乘的公車：", "------", sep = '\n')
        for bus in take2TF_Buses:
            print(bus)
            
        print("---------------")
        selectBus = input("選擇撘乘公車：") or take2TF_Buses[0]
        print("---------------", f"你所選擇的公車：{selectBus}", "---------------", sep = '\n')


        tfStops = []
        for takeStop in takeInfo:
            
            if selectBus in list(takeStop[theStop.roundTrip_ob].keys()):
                for tfStop in tf:
                    if selectBus in list(tfStop[theStop.roundTrip_ob].keys()) \
                        and int(takeStop[theStop.roundTrip_ob][selectBus][1]) < int(tfStop[theStop.roundTrip_ob][selectBus][1]) \
                        and tfStop not in tfStops:
                        tfStops.append(tfStop)
            if selectBus in list(takeStop[theStop.roundTrip_ib].keys()):
                for tfStop in tf:
                    if selectBus in list(tfStop[theStop.roundTrip_ib].keys()) \
                        and int(takeStop[theStop.roundTrip_ib][selectBus][1]) < int(tfStop[theStop.roundTrip_ib][selectBus][1]) \
                        and tfStop not in tfStops:
                        tfStops.append(tfStop)
        #endregion
                        
        #region Select Transfer Stop
        print("可轉乘的站點：", "------", sep = '\n')
        tfList = []
        for tfStop in tfStops:
            if tfStop[theStop.stopName_CN] not in tfList:
                tfList.append(tfStop[theStop.stopName_CN])
                print(tfStop[theStop.stopName_CN])
        #endregion
        
        #region From Transfer Stop
        print("---------------")
        selectTF_Stop = input("選擇轉乘站：") or tfList[0]
        print("---------------")

        selectTF2des = []
        TF_Buses = []

        for tfStop in busList:
            if tfStop[theStop.stopName_CN] == selectTF_Stop:
                # print(stop)
                selectTF2des.append(tfStop)
                
                for tfBus in list(tfStop[theStop.roundTrip_ob].keys()):
                    if tfBus not in TF_Buses:
                        TF_Buses.append(tfBus)
                
                for tfBus in list(tfStop[theStop.roundTrip_ib].keys()):
                    if tfBus not in TF_Buses:
                        TF_Buses.append(tfBus)
                

        TF2des_Buses = sorted(list(set(desBusesInfo) & set(TF_Buses)))
        #endregion

        #region Select Bus from Transfer to Des
        print("可轉乘的公車：", "------", sep = '\n')
        for bus in TF2des_Buses:
            print(bus)
        print("---------------")
        selectTF_Bus = input("選擇轉乘公車：") or TF2des_Buses[0]
        print("---------------", f"你所選擇的公車：{selectTF_Bus}", "---------------", sep = '\n')


        arrive2Des = []
        for takeStop in selectTF2des:
            
            if selectTF_Bus in list(takeStop[theStop.roundTrip_ob].keys()):
                for desStop in desInfo:
                    if selectTF_Bus in list(desStop[theStop.roundTrip_ob].keys()) \
                        and int(takeStop[theStop.roundTrip_ob][selectTF_Bus][1]) < int(desStop[theStop.roundTrip_ob][selectTF_Bus][1]) \
                        and desStop not in tfStops:
                        arrive2Des.append(desStop)
            if selectTF_Bus in list(takeStop[theStop.roundTrip_ib].keys()):
                for desStop in desInfo:
                    if selectTF_Bus in list(desStop[theStop.roundTrip_ib].keys()) \
                        and int(takeStop[theStop.roundTrip_ib][selectTF_Bus][1]) < int(desStop[theStop.roundTrip_ib][selectTF_Bus][1]) \
                        and desStop not in tfStops:
                        arrive2Des.append(desStop)
        #endregion

        #region Show Select Path


        # if len(arrive2Des) != 0:
        desList = []
        for stop in arrive2Des:
            if stop[theStop.stopName_CN] == desStopName and stop[theStop.stopName_CN] not in desList:
                desList.append(stop[theStop.stopName_CN])
            
        arriveMsg = f"抵達：{', '.join(desList)}"
        print(arriveMsg, "---------------", sep = '\n')
            
        print("所選擇的路徑：", f"在 {takeStopName} 公車站", f"撘乘 {selectBus}", f"到 {selectTF_Stop} 轉乘站", f"轉乘 {selectTF_Bus}", arriveMsg, "---------------", sep = '\n')
            
        #endregion
    #endregion

#endregion


#region System Function
functionDict = {1:[findStop, "查站點"], 2:[findBusInfo, "查公車"], 3:[takeBus, "撘公車"]}
for i in list(set(functionDict.keys())):
    print(i, functionDict[i][1], sep = ":")

selectFunction = input("選擇系統功能：") or 1
functionDict[int(selectFunction)][0]()
#endregion