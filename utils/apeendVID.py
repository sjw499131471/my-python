existIDstr = "115+/143+/137+/117+/096+/091+/095+/146/142/135/144/133/132/123/108/097/083/077/076/075/057/046/045/043/024/021/016/003"
existIDList=existIDstr.split('/')
existIDSourceList=[x.replace('+','') for x in existIDList]
toDownloadIDList=[x.replace('+','') for x in existIDList if '+' in x]
print('已经检索过的vid:' + str(existIDSourceList))
print('要下载的vid:' + str(toDownloadIDList))
allIDstr = "076/075/077/083/096/091/095/097/108/117/123/132/144/135/137/142/143/146/164/175/196/189/186/188/198/206/201/207/214/016/024/043/046/045/057/149/183/191/194/003/021/126/167/139/021/165/175/076/123/166/043/091/075/067/142/144/016/064/046/133/115/117/132/003/118/043/077/066/083/013/024/003/019/"
allIDList=allIDstr.split('/')
allUniqueIDList = list(set(allIDList))#去重
print('所有的vid:' + str(allUniqueIDList))
uncheckedIDList=[]
for vid in allUniqueIDList:
    if vid not in existIDSourceList:
        existIDSourceList.append(vid)
        uncheckedIDList.append(vid)
existIDSourceList.sort()
for vid in toDownloadIDList:
    existIDSourceList[existIDSourceList.index(vid)] += '+'
for vid in uncheckedIDList:
    existIDSourceList[existIDSourceList.index(vid)] += '?'
existIDSourceListStr = '/'.join(existIDSourceList)#格式化
print('结果：'+existIDSourceListStr)
