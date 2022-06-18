### screenshot_stock_price.py

import sys
import os
import time
import io

args = sys.argv
global user_name
user_name = args[1]
global login_pass
login_pass = args[2]

jpg_path = "/Users/******/git/web_scraper/jpg"

from datetime import datetime
now_datetime = datetime.now()
yyyymmdd = now_datetime.strftime("%Y%m%d")

def screenshot_sbi():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    
    options = Options()
    options.add_argument('--log-level=3')
    if option_headless == 1:
        options.add_argument('--headless')
        
    ### chrome webdriver setting
    driver = webdriver.Chrome(chrome_options=options, executable_path="c:/driver/chromedriver.exe")
    driver.get("https://www.sbisec.co.jp/ETGate")
    
    time.sleep(3)
    driver.find_element_by_name("user_id").send_keys(user_name)
    driver.find_element_by_name("user_password").send_keys(login_pass)
    driver.find_element_by_name("ACT_login").click()
    print("*** # TOP Page ***")
    
    time.sleep(2)
    driver.save_screenshot(os.path.join(jpg_path,"toppage_%s.png") %yyyymmdd)
    print("*** # KOZA KANRI ***")
    time.sleep(2)
    driver.find_element_by_xpath("//img[@src='https://sbisec.akamaized.net/sbisec/images/base02/g_head02_account02.gif']").click()
    print("*** # KOZA NISA ***")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="footer01P"]/div[5]/div[3]/ul/li[3]/a').click()
    
    # Get_ScreenShot_Before
    time.sleep(2)
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)
    driver.save_screenshot(os.path.join(jpg_path,"nisa_%s.png") %yyyymmdd)

    driver.quit()
    return()


def line_notificate():
    line_notify_token = "***"
    line_notify_url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    message = "LINE notification"
    payload = {'message': message}
    line_notify = requests.post(line_notify_url, headers=headers, params=payload,)
    return()

if __name__ == '__main__':

    option_setting = 0 # 1 means headless mode "ON"
    global option_headless
    option_headless = option_setting

    screenshot_sbi()
    # line_notificate()

    exit()
