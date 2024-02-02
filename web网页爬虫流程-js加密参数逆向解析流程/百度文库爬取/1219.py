# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： 1219.py
    @date：2023/12/19 15:20
    
"""
# 导入的包
import os.path
import time
from selenium import webdriver
import requests
from selenium.webdriver.support.select import Select

url = input('输入想要下载的百度文库地址：')  # 输入自己需要爬取的PPT地址
# 第一部分：手机模式打开一个电脑浏览器
options = webdriver.ChromeOptions()                                    # 配置chrome启动时属性的类
mobile_emulation = {"deviceName": "iPhone 6"}                           # 手机模式打开浏览器，手机类型:iPhone 6
options.add_experimental_option("mobileEmulation", mobile_emulation)  # 将mobile_emulation 添加到options中，这样浏览器就是通过手机模式打开
web = webdriver.Chrome() # 路径修改为自己电脑浏览器驱动路径
web.get(url)
time.sleep(2)

# 第二部分：将所有隐藏的ppt图片展示出来
def click_ele(click_xpath):
    # 单击指定控件
    click_ele = web.find_elements_by_xpath(click_xpath)
    if click_ele:
        click_ele[0].location_once_scrolled_into_view                               # 滚动到控件位置
        web.execute_script('arguments[0].click()', click_ele[0])                    # 单击控件，即使控件被遮挡，同样可以单击
# 点击继续阅读
xpath_continue_read_button = "//div[@class='foldpagewg-icon']"                      # 获取继续阅读得到xpath
click_ele(xpath_continue_read_button)                                               # 调用click_ele()
xpath_next_content_button = "//div[@class='btn-wrap']/div[@class='btn-cancel']"     # 获取下一页的xpath
click_ele(xpath_next_content_button)                                                # 调用click_ele()
click_count = 0
while True:
    # 如果到了最后一页就跳出循环
    if web.find_elements_by_xpath(
            "//div[@class='pagerwg-loadSucc hide']") or web.find_elements_by_xpath(
            "//div[@class='pagerwg-button' and @style='display: none;']"):
        break
    # 点击加载更多
    xpath_loading_more_button = "//span[@class='pagerwg-arrow-lower']"
    click_ele(xpath_loading_more_button)
    click_count += 1
    print("第{}次点击加载更多!".format(click_count))
    # 等待一秒，等浏览器加载
    time.sleep(2)
click_ele('//*[@id="wui-messagebox-cancel-1"]')
time.sleep(1)
# 图片元素的定位及获取
li_list = web.find_elements_by_class_name('retype-page')
img_url = []
for i in li_list:
    h2 = i.find_element_by_class_name('pic')
    time.sleep(3)
    h3 = h2.find_element_by_tag_name('img')
    time.sleep(1)
    img = h3.get_attribute('src')
    img_url.append(img)
# 创建文件夹进行保存
path = 'D://百度文库PPT//爬虫ppt图片'     # 看自己心情，将爬取的PPT图片放在哪里，比如：D://百度文库PPT//爬虫ppt图片
if not os.path.exists(path):        # 查找是否有存储的文件夹，没有则创建一个
    os.makedirs(path)
# 解析图片url,并保存到已创建的文件夹中
x = 1
for g in range(len(img_url)):
    r = requests.get(img_url[g])
    path = 'D://百度文库PPT//爬虫ppt图片//%d.jpg' % x
    print('正在爬取' + img)
    with open(path, "wb") as f:
        f.write(r.content)
        time.sleep(2)
        f.close()
        print('爬取成功')
        x += 1
