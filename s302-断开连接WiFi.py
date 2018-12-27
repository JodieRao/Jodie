# coding=utf-8
from appium import webdriver
import time
desired_caps = {
                'platformName': 'Android',
                'deviceName': '123456789',
                'platformVersion': '4.4.2',
                # apk包名
                'appPackage': 'com.incall.apps.setting',
                # apk的launcherActivity
                'appActivity': 'com.incall.apps.setting.MainActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element_by_id("com.incall.apps.setting:id/setting_listbutton_internet").click()
for i in range(30):
    driver.find_element_by_id("android:id/title").click()
    driver.find_element_by_id("com.incall.apps.setting:id/wifi_dialog_button1").click()
    time.sleep(1)
    driver.find_element_by_id("android:id/title").click()
    driver.find_element_by_id("com.incall.apps.setting:id/wifi_dialog_button1").click()
    time.sleep(15)
print("总计断开连接30次")