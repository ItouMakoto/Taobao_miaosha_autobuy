from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import datetime

usr=''
pw=""
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe',options=chrome_options)
try:
    driver.maximize_window()
except:
    print("maxed")
def login(url,user,passWord):#选择一个购物车内的商品
    """登录模块,用于登录淘宝，并选中需要购买的商品按钮，结束"""
    # 获取网页源信息
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
    time.sleep(1)
    # """(修改)勾选你需要购买的物品"""
    driver.find_element_by_xpath('//*[@id="J_Item_1731224185307"]/ul/li[1]/div/div/div/label').click()
def buy_good(buy_time):

    while True:
        # 读取系统当前时间
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 是否到可以购买的时间了
        if now_time <= buy_time:
            try:
                driver.find_element_by_id("J_Go").click()#提交
                time.sleep(0.05)
                # 点击提交订单按钮
                while True:

                    try:
                        driver.find_element_by_xpath('//a[@class="go-back"]').click()  # 提交
                        break
                    except:
                        print("没有出现")
                        time.sleep(1)

                #driver.find_element_by_xpath('//*[@id="submitOrder_1"]/div/a[2]').click()
                # 输入密码进行支付了
                break
            except:
                time.sleep(1)
        print(now_time)

if __name__ == "__main__":
    url = 'https://www.taobao.com/'
    login(url=url,user=usr,passWord=pw)
    """定时购买"""
    buy_good('2020-01-31 20:00:00')

    #购买调试测试
   # driver.find_element_by_id("J_Go").click()  # 提交
    # 点击提交订单按钮
#    driver.find_element_by_xpath('//*[@id="submitOrder_1"]/div/a[2]').click()