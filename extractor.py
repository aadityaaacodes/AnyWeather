from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json, os

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
    weatherData = x['weatherData']

    # Bot setup to not use GUI & Shared Memory
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")  # Set window size
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    # chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument('--disable-gpu')



    # starting selenium bot
    service = Service(executable_path='venv/bin/chromedriver')
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    # performing google search
    driver.get("https://www.google.com/")
    bar = driver.find_element(By.CLASS_NAME, "gLFyf")
    bar.send_keys(f"{query} Weather", Keys.RETURN)
    driver.get_screenshot_as_file("google.png")
    
    # collecting information on page
    weatherData["temperature"] = (driver.find_element(By.ID, "wob_tm")).text
    weatherData["precipitation"] = (driver.find_element(By.ID, "wob_pp")).text
    weatherData["humidity"] = (driver.find_element(By.ID, "wob_hm")).text
    weatherData["windspeed"] = (driver.find_element(By.ID, "wob_ws")).text
    weatherData["condition"] = (driver.find_element(By.ID, "wob_dc")).text

    # clicking button to weather.com
    anchor = driver.find_element(By.LINK_TEXT, "weather.com")
    anchor.click()

    # weather.com opens
    driver.get_screenshot_as_file("weather.png")
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
    # print((getInfo())['weatherData'])

    # deleting images
    os.remove("google.png")
    os.remove("weather.png")



# performGoogleSearch(query="Cincinnati")

# performGoogleSearch("Los Angeles")