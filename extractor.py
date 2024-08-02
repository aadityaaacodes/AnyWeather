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

def performGoogleSearch(query):
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
    bar.send_keys(f"{query} Weather", Keys.RETURN)

    # collecting information on page
    weatherData["temperature"] = (driver.find_element(By.ID, "wob_tm")).text
    weatherData["precipitation"] = (driver.find_element(By.ID, "wob_pp")).text
    weatherData["humidity"] = (driver.find_element(By.ID, "wob_hm")).text
    weatherData["windspeed"] = (driver.find_element(By.ID, "wob_ws")).text
    weatherData["condition"] = (driver.find_element(By.ID, "wob_dc")).text

    # putInfo(x)
    # clicking button to weather.com
    anchor = driver.find_element(By.LINK_TEXT, "weather.com")
    anchor.click()

    # weather.com opens
    weatherData['aqi'] = (driver.find_element(By.CLASS_NAME, "DonutChart--innerValue--3_iFF")).text
    dawn_dusk = driver.find_elements(By.CLASS_NAME, "TwcSunChart--dateValue--2WK2q")
    weatherData['dawn'] = dawn_dusk[0].text
    weatherData['dusk'] = dawn_dusk[1].text
    weatherData['locale'] = (driver.find_element(By.CLASS_NAME, "CurrentConditions--location--1YWj_")).text

    cssSelectors = {
    "uvIndex" : "span[data-testid = 'UVIndexValue']",
    "pressure" : "span[data-testid = 'PressureValue']", 
    "visibility" : "span[data-testid = 'VisibilityValue']"
    }

    weatherData['pressure'] = (driver.find_elements(By.CSS_SELECTOR, "span[data-testid = 'PressureValue']"))[0].text
    
    weatherData['uv'] = (driver.find_elements(By.CSS_SELECTOR, "span[data-testid = 'UVIndexValue']"))[0].text

    weatherData['visibility'] = (driver.find_elements(By.CSS_SELECTOR, "span[data-testid = 'VisibilityValue']"))[0].text


    # shutting bot
    driver.quit

    # dumping JSON file to save changes
    putInfo(x)

def getLocation():
    x = getInfo()
    return(x)


performGoogleSearch(query="Cincinnati")