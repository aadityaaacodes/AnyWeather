from extractor import getInfo, putInfo

json_path = 'dataStorage.json'

x = getInfo()
y = x["searchData"]

    
def queryDumper(info):
    c = 0
    for i in y:
        y[i] = info[c]
        c += 1
    putInfo(x)

# li = ["Cincinnati", "Ohio", "USA"]
# queryDumper(li)