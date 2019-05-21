import time
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

cap = {
    "platformName": "Android",
    "platformVersion": "4.4.2",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.ss.android.article.news",
    "appActivity": "com.ss.android.article.news.activity.SplashBadgeActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)


def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


def handle_toutiao(driver):
    # 还有广告的可能
    # 处理用户隐私政策概要
    try:
        if WebDriverWait(driver, 7).until(lambda x: x.find_element_by_xpath(
                "//android.widget.LinearLayout[@resource-id='com.ss.android.article.news:id/nv']")):
            driver.find_element_by_xpath(
                "//android.widget.Button[@resource-id='com.ss.android.article.news:id/d06']").click()
    except:
        pass
    # 刷新新闻,下拉
    time.sleep(10)
    l = get_size(driver)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.25)
    y2 = int(l[1] * 0.85)
    driver.swipe(x1, y1, x1, y2)
    """
    1,执行下拉操作,停顿5秒
    2,向上滑动,直到出现"点击刷新",点击并等待
    """
    # view_text = WebDriverWait(driver,15).until(lambda x:x.find_elements_by_id("com.ss.android.article.news:id/title"))
    # print(view_text)
    # for item in view_text:
    #   print(item.get_attribute('name'))
    x3 = int(l[0] * 0.4)
    y3 = int(l[1] * 0.75)
    y4 = int(l[1] * 0.25)
    while True:
        driver.swipe(x3, y3, x3, y4)
        time.sleep(2)
        if "点击刷新" in driver.page_source:
            driver.find_element_by_id("com.ss.android.article.news:id/bpl").click()




if __name__ == '__main__':
    handle_toutiao(driver)
