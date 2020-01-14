from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import datetime


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe',options=chrome_options)

cartUrl=""

try:
    driver.maximize_window()
except:
    print("maxed")
def login(url,buy_time):#选择一个购物车内的商品
    global cartUrl
    """登录模块,用于登录淘宝，并选中需要购买的商品按钮，结束"""
    # 获取网页源信息
    if url == "https://www.taobao.com/":
        driver.get(url)
    # 等浏览器与Selenium完美契合之后再进行下一步动作
    driver.implicitly_wait(2)
    """账号密码登陆: 但是有验证框 需要拖拽"""
    # locator = ("name", "TPL_username")
    ##driver.switch_to.frame("sufei-dialog-content");
    # WebDriverWait(driver, 5, 0.5).until(EC.visibility_of_element_located(locator), "out of time")
    # print("find")
    # driver.find_element_by_name("TPL_username").send_keys(user)  # user_pwd
    # driver.find_element_by_name("TPL_password").send_keys(passWord)  # user_pwd
    #time.sleep(4)
	#有滑块验证，没加
    #driver.find_element_by_id("J_SubmitStatic").click()  # 寻找id类型的确认
    """扫码登陆(自己扫码)："""
    # time.sleep(1)
    # driver.find_element_by_id("J_Static2Quick").click()  # 寻找id类型的确认
    # time.sleep(7)
    # # 查找购物车按钮的xpath并点击进入购物车
    if url=="https://www.taobao.com/":
        driver.find_element_by_xpath('//*[@id="mc-menu-hd"]/span[2]').click()
    cartUrl=driver.current_url
    # """(修改)勾选你需要购买的物品"""
    driver.find_element_by_xpath('//*[@id="J_Item_1731224185307"]/ul/li[1]/div/div/div/label').click()
    #time.sleep(3)  # 减速
    buy_good(buy_time)

def buy_good(buy_time):

    while True:
        # 读取系统当前时间
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 是否到可以购买的时间了
        if now_time <= buy_time:
            try:
                submit=driver.find_element_by_id("J_Go")
                while submit.get_attribute("class").find("disabled")!=-1:
                    pass
                submit.click()#提交
                testUrl()

                time.sleep(0.05)
                # 点击提交订单按钮
                while True:
                    try:
                        driver.find_element_by_xpath('//a[@class="go-back"]').click()  # 提交
                        testUrl()
                        break
                    except Exception as e:
                        print(e)
                        time.sleep(1)

                #driver.find_element_by_xpath('//*[@id="submitOrder_1"]/div/a[2]').click()
                # 输入密码进行支付了
                break
            except Exception as e:
                print(e)
                time.sleep(1)
        print(now_time)

def testUrl():
    testHandle = driver.current_window_handle
    js = "window.open('" + cartUrl + "');"
    driver.execute_script(js)
    cartHandle = driver.window_handles[1]
    driver.switch_to.window(testHandle)
    testUrl = driver.current_url
    if (testUrl.lower().find("wait") != -1 or testUrl.lower().find("undefined") != -1 or testUrl.lower().find("erro") != -1):
        driver.close()
        driver.switch_to.window(cartHandle)
        login(cartUrl, buy_time)
    else:
        driver.switch_to.window(cartHandle)
        driver.close()
        driver.switch_to.window(testHandle)

if __name__ == "__main__":
    url = 'https://www.taobao.com/'
    """定时购买"""
    buy_time='2020-01-01 20:00:00'
    login(url=url,buy_time=buy_time)


    #购买调试测试
   # driver.find_element_by_id("J_Go").click()  # 提交
    # 点击提交订单按钮
#    driver.find_element_by_xpath('//*[@id="submitOrder_1"]/div/a[2]').click()