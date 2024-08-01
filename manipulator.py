import json

json_path = 'dataStorage.json'

def putInfo(dumpFile):
    with open(json_path, 'w') as jFile:
        return(json.dump(dumpFile, jFile, indent=4))
    
