from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import datetime
import string

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe',options=chrome_options)
try:
    driver.maximize_window()
except:
    print("maxed")
driver.get("https://www.baidu.com")
baidu=driver.current_window_handle
driver.get("https://www.sohu.com")
js = "window.open('https://www.taobao.com');"
driver.execute_script(js)
taobao=driver.current_window_handle
driver.switch_to.window(baidu)
testUrl=driver.current_url
if testUrl.lower().find("so")!=-1:
         driver.close()
         driver.switch_to.window(driver.window_handles[0])
         driver.find_element_by_xpath('//*[@id="mc-menu-hd"]/span[2]').click()
print (driver.current_window_handle)
# handles = driver.window_handles
# print(len(handles))
# for handle in handles:
#     currentPageUrl = driver.current_url
#     if currentPageUrl.lower().find("goo")!=-1:
#         driver.close()
#     driver.switch_to.window(handle)