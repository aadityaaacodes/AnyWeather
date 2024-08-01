from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

json_path = 'dataStorage.json'

def getInfo():
    with open(json_path, 'r') as jFile:
        return(json.load(jFile))

def putInfo(dumpFile):
    with open(json_path, 'w') as jFile:
        return(json.dump(dumpFile, jFile, indent=4))


def performGoogleSearch():
    # JSON -> Dictionary
    x = getInfo() 
    searchData = x['searchData']
    weatherData = x['weatherData']

    # starting selenium bot
    service = Service(executable_path='venv/bin/chromedriver')
    driver = webdriver.Chrome(service=service)

    # performing google search
    driver.get("https://www.google.com/")
    bar = driver.find_element(By.CLASS_NAME, "gLFyf")
    bar.clear()
    bar.send_keys(f"{searchData['city']}, {searchData['state']}, {searchData['country']} Weather", Keys.RETURN)

    # collecting information on page
    weatherData["temperature"] = (driver.find_element(By.ID, "wob_tm")).text
    weatherData["precipitation"] = (driver.find_element(By.ID, "wob_pp")).text
    weatherData["humidity"] = (driver.find_element(By.ID, "wob_hm")).text
    weatherData["windspeed"] = (driver.find_element(By.ID, "wob_ws")).text
    weatherData["condition"] = (driver.find_element(By.ID, "wob_dc")).text

    # shutting bot
    driver.close

    # dumping JSON file to save changes
    putInfo(x)