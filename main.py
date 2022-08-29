from ast import main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

import time
from bs4 import BeautifulSoup
import pandas as pd
global driver

option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36')
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(0.5)

with open('stealth.min.js') as f:
    js = f.read()
    
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
    "source":js
})

driver.get("https://www.qcc.com")
driver.maximize_window()


def get_result_table(result_html):
    soup = BeautifulSoup(result_html,"lxml")
    x=str(soup.find("table","ntable"))
    result_table=pd.read_html(x)[0]
    company_name=result_table[result_table[2]=='企业名称'][3].values[0]
    company_size=result_table[result_table[0]=='人员规模'][1].values[0]
    result = pd.DataFrame([company_name,company_size])
    return result;

final_result=pd.DataFrame()
file_list=list(pd.read_excel('企业白名单.xlsx')['公司名称'])

print("-----")

for file in file_list:
    print("Excel conten: " + file)
    # driver.switch_to.window(driver.window_handles[-1])
    # text_label = driver.find_element(By.ID,'searchKey')
    # text_label.clear()
    # text_label.send_keys(file)
    # time.sleep(1)
    # button=driver.find_element(By.CLASS_NAME,'input-group-btn')
    # button.click()
    # driver.implicitly_wait(5)
    # try:
    #     results = driver.find_element(By.XPATH,'//*[@class="maininfo"]/div[1]/span[1]')
    #     results.click()
    #     driver.switch_to.window(driver.window_handles[-1])
    #     result_table=get_result_table(driver.page_source)
    #     final_result=final_result.append(result_table)
    #     driver.close()
    # except:
    #     continue
print("++++++++")