# coding=utf-8
from appium import webdriver
import time
desired_caps = {
                'platformName': 'Android',
                'deviceName': '123456789',
                'platformVersion': '4.4.2',
                # apk包名
                'appPackage': 'com.incall.apps.btphone',
                # apk的launcherActivity
                'appActivity': 'com.incall.apps.btphone.activity.BtActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(2)
driver.find_element_by_id("com.incall.apps.btphone:id/rb3").click()
time.sleep(8)
for i in range(200):
    driver.find_element_by_id("com.incall.apps.btphone:id/bt_status_tv").click()
    time.sleep(1)
    driver.find_element_by_id("com.incall.apps.btphone:id/buttonDialogLeft").click()
    time.sleep(3)
    driver.find_element_by_id("com.incall.apps.btphone:id/bt_name_tv").click()
    time.sleep(20)
print("总计连接200次")