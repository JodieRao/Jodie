# coding=utf-8
from appium import webdriver
import time
desired_caps = {
                'platformName': 'Android',
                'deviceName': '123456789',
                'platformVersion': '4.4.2',
                'noRest':'Ture',
                # apk包名
                'appPackage': 'com.incall.apps.btphone',
                # apk的launcherActivity
                'appActivity': 'com.incall.apps.btphone.activity.BtActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#time.sleep(2)
for i in range(100):
    driver.find_element_by_id("com.incall.apps.btphone:id/recordTel").click()
    time.sleep(7)
    driver.find_element_by_id("com.incall.apps.btphone:id/norhangup").click()
    time.sleep(4)
print("总计拨打电话100次")