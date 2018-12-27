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
driver.find_element_by_id("com.incall.apps.setting:id/setting_listbutton_bd").click()
for i in range(60):
    time.sleep(3)
    driver.find_element_by_id("com.incall.apps.setting:id/bt_delete_tv").click()
    time.sleep(1)
    driver.find_element_by_id("com.incall.apps.setting:id/buttonDialogLeft").click()
    time.sleep(1)
    driver.find_element_by_id("com.incall.apps.setting:id/ivRefishBackgrand").click()
    time.sleep(12)
    driver.find_element_by_xpath("//*[@text='B311']").click()
    time.sleep(17)
print("总计删除200次")