# coding=utf-8
from appium import webdriver
#从appium中导入webdriver
import time
desired_caps = {
                'platformName': 'Android',
                 #是安卓的还是ios的，声明手机是Android还是ios
                'deviceName': '123456789',
                 #连接的设备的名称“adb devices”
                'platformVersion': '4.4.2',
                 #安卓的版本号，从手机的设置里看
                'appPackage': 'com.incall.apps.btphone',
                 # apk包名 “aapt dump badging 包名（可将文件拖至cmd）”，日志中可以看到package name
                'appActivity': 'com.incall.apps.btphone.activity.BtActivity'
                 # apk的launcherActivity,“aapt dump badging 包名（可将文件拖至cmd）”,日志中查找
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#启动服务，appium就相当于一个服务器
time.sleep(2)
driver.find_element_by_id("com.incall.apps.btphone:id/rb3").click()
time.sleep(8)
for i in range(1000):
    driver.find_element_by_id("com.incall.apps.btphone:id/useforRefishLL").click()
    time.sleep(10)
print("总计搜索1000次")










