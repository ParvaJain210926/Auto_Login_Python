from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def startBot (username,password,url):
    #path to driver where you installed chrome driver
    path = "C:\\Users\\parva\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    service =Service(path)

    chrome_options=Options()
    chrome_options.add_argument("--start-maximized")
    driver= webdriver.Chrome(service=service,options=chrome_options)

    print("opening login page")

    driver.get(url)


    print("entering username")
    driver.find_element(By.ID,"login_field").send_keys(username)
    print("entering password")
    driver.find_element(By.ID,"password").send_keys(password)
    print("Clicking on login")

    driver.find_element(By.NAME,"commit").click()
    print("Login Processing")

    time.sleep(5)
    driver.quit()


username="Username"#enter the username
password="12345678" #enter the password

url="https://github.com/login" # link to page where you want to login


startBot(username, password,url)

