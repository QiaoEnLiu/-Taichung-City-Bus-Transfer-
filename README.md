哈囉！你好嗎？


![image](/Resource/中興幹線.png)


公車系統轉乘組合

	臺中市公車資料集轉乘分析(Taichung City Bus Transfer)

當乘客要撘乘公車前往目的地時，發現可抵達目的地的公車沒有經過乘客當下的站點，於是乘客就可以決定撘乘到可以換乘直達目的地站點的公車，此方式為轉乘；而此專案則是使用臺中市市政府開放資料平台​的「臺中市市區公車站牌資料」分析出轉乘組合，如果要從朝陽科大前往逢甲大學就​可以列出「131(朝陽科技大學-臺中火車站)25(臺中火車站-逢甲大學）」這其中一種轉乘組合。

此專案由Python撰寫，使用Anaconda-Spyder環境以「吉峰東自強路口」前往「逢甲大學（福星路）」測試，在輸入撘乘站點及目的站點後，先判斷是否可以直達，不可直達則輸出轉乘組合。


	Resource資料夾：臺中市公車站牌資料集（離線）

	臺中市市區公車站牌資料載點網頁： https://opendata.taichung.gov.tw/search/3e09d847-0fbd-41fa-9e6c-2b37aa47e07e
	
 
	Bus_OOP.py：適用於本專案的自建函數
	busSempleStatistics.py：臺中市公車簡易統計
	FilePath_OOP.py：檔案路徑、檔名、副檔名組合
	sameStops.py：兩條公車路線相同站點
	searchBus.py：讀取該公車路線
	searchStopName：輸入名稱查站名（CN/EN）
	stopInfo.py：該站點上所有公車路線
	TakeBus.py：從現在撘乘站前往目的地可撘哪些公車
	TransferBus.py：（此專案主要功能）前往目的地是否需要轉乘，若要轉乘則輸出需抵達哪站轉乘公車
 	劉喬恩_公車系統轉乘組合（簡報）.pdf：PDF簡報檔
