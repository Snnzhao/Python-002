from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    
    browser.get('https://shimo.im/login?from=home')
    time.sleep(1)

    browser.find_element_by_xpath('//div[@class="form-wrapper"]')
    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('snnzhao@163.com')
    browser.find_element_by_xpath('//input[@name="password"]').send_keys('zhaosen123456')
    time.sleep(1)
    browser.find_element_by_xpath('//button[contains(@class,"sm-button submit sc-1n784rm-0 bcuuIb")]').click()

    cookies = browser.get_cookies() # 获取cookies
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:    
    browser.close()
    