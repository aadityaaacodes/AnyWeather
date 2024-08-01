from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import json

json_path = 'dataStorage.json'

def getInfo():
    with open(json_path, 'r') as jFile:
        return(json.load(jFile))

def putInfo(dumpFile):
    with open(json_path, 'w') as jFile:
        return(json.dump(dumpFile, jFile, indent=4))

x = getInfo() 
searchData = x['searchData']
weatherData = x['weatherData']



service = Service(executable_path='venv/bin/chromedriver')
driver = webdriver.Chrome(service=service)

