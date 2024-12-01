from selenium import webdriver
import json

def openBrowser():
    print("Browser Setup :)")
    file = open('web/json/settings.json','r', encoding="utf-8")
    jsonData = file.read()
    obj = json.loads(jsonData)
    file.close()
    ProfilePath = obj['profilePath']

    optionsVar = webdriver.ChromeOptions() 
    optionsVar.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    optionsVar.add_argument(r"--user-data-dir=" + ProfilePath)
    optionsVar.add_argument(r'--profile-directory=CSGORollDailyCollector') 
    optionsVar.add_experimental_option("detach", True)
    webdriver.Chrome(options=optionsVar)

openBrowser()