#!/usr/bin/env python3
# 06d81475cfa374cabf01f228fa99dd9c
import binascii
import getpass
import json
import os
import random
import re
import sys
import time
from urllib import parse
import pyperclip
import requests
from bs4 import BeautifulSoup as bs
# from PIL import Image, ImageEnhance
from imageio.config.plugins import des
from pyDes import *

# 检测操作系统
system = os.name
if system == 'nt':
    clean_mode = 'cls'
elif system == 'posix':
    clean_mode = 'clear'
else:
    print(Color('\t警告：未识别的操作系统，可能存在兼容性问题。'))
    if (input('是否继续（y/n）:') != 'y') & (input('是否继续（y/n）:') != 'Y'):
        sys.exit()
    colorful = False

# 切换工作路径
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# 临时颜色管理函数
def Color(text, display=None, foreground=None, background=None):
    if display == None:
        return (text)
    elif foreground == None:
        return (('\033[%dm%s\033[0m') % (display, text))
    elif background == None:
        return (('\033[%d;%dm%s\033[0m') % (display, foreground, text))
    else:
        return (('\033[%d;%d;%dm%s\033[0m') % (display, foreground, background, text))


# 错误处理函数
def Fatal_err(text, err):
    os.system(clean_mode)
    print(Color('\t\t百度文库下载器by_Serendipity_Fu\n', 1, 31))
    print(Color(text) + Color(str(err), 5, 31), end='')
    sys.stdout.flush()
    getpass.getpass('（回车退出）')
    sys.exit()


def Err(text):
    print(Color('\n' + text, 5, 31), end='')
    sys.stdout.flush()
    getpass.getpass('（回车继续）')


# 使用向导
if not os.path.exists('config.conf'):
    # 默认设置
    name = '百度文库下载器by_Serendipity_Fu'
    refresh = False
    enter_time = 0.5
    exit_time = 1
    textout_time = 0.01
    name_limit = 100
    if system == 'posix':
        colorful = True
    else:
        colorful = 'only_red'
    ua_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36 Edg/80.0.361.54'
    ]


    # 定义临时函数

    # 标题栏函数
    def Wizard_ui(at=None):
        os.system(clean_mode)
        if at == None:
            print(('\t\t使用向导（共9步）\n'))
        else:
            print(('\t\t使用向导（第%d步，共9步）\n') % at)


    # 临时文字输出函数
    def Textout(text, end='\n', display=None):
        for i in text:
            print(Color(i, display), end='')
            sys.stdout.flush()
            time.sleep(0.01)
        print(end=end)


    # 向导主程序

    # 教程主程序
    os.system(clean_mode)
    Textout('\t\t' + name, display=1)
    Textout(
        '\t检测到这是首次启动，接下来将进行简单的说明以及设置\n\n\t说明：本软件为百度文库下载器，复制百度文库链接到此软件即可下载百度文库文档。在此软件中，以下类型的文档不能下载：\n\t1.vip专享文档\n\t2.付费文档\n')
    sys.stdout.flush()
    getpass.getpass('\t（回车继续）')
    Wizard_ui(1)
    Textout('\t在这个软件中，你可以使用键盘输入数字或链接，键盘回车来确定。像这样：')
    Textout('\n\t\t菜单（请随便选择以下的一个选项来继续）')
    Textout('\t[1]继续\n\t[2]继续\n\t[3]继续')
    task = input('\t请输入要执行的任务：')
    while (task != '1') & (task != '2') & (task != '3'):
        Err('\t错误的输入，请再试一次吧：')
        Wizard_ui(1)
        Textout('\t在这个软件中，你可以使用键盘输入数字或链接，键盘回车来确定。像这样：')
        Textout('\n\t\t菜单（请随便选择以下的一个选项来继续）')
        Textout('\t[1]继续\n\t[2]继续\n\t[3]继续')
        task = input('\t请输入要执行的任务：')
    Textout('\t就是这样！', end='')
    sys.stdout.flush()
    getpass.getpass('（回车继续）')
    Wizard_ui(2)
    Textout('\t在某些场景下，软件可能会要求你输入y或者n来表示是或否（不分大小写）。像这样：')
    task = input('\n\t是否下载该文件(y/n):')
    while (task != 'y') & (task != 'n') & (task != 'Y') & (task != 'N'):
        Err('\t错误的输入，请再试一次吧：')
        Wizard_ui(2)
        Textout('\t在某些场景下，软件可能会要求你输入y或者n来表示是或否（不分大小写）。像这样：')
        task = input('\n\t是否下载该文件(y/n):')
    if (task == 'y') | (task == 'Y'):
        Textout('\t就是这样！你选择了"是"', end='')
    else:
        Textout('\t就是这样！你选择了"否"', end='')
    sys.stdout.flush()
    getpass.getpass('（回车继续）')

    # 设置主程序
    Wizard_ui()
    Textout('\t接下来我们来进行一些简单的设置')
    Textout('\t(如果看不懂，可以不输入直接回车来使用默认设置。输入‘小写c’可以返回上一项设置。浏览器标示请自行在后续生成的config.json文件中设置)')
    getpass.getpass('\t（回车继续）')
    name = '百度文库下载器by_Serendipity_Fu'
    config_list = [name, refresh, enter_time, exit_time, textout_time, name_limit, colorful, ua_list]
    i = 0
    while i != 8:
        # 软件名设置
        if i == 0:
            Wizard_ui(3)
            config = input('\t请设置软件名称（默认百度文库下载器by_Serendipity_Fu）：')
            if config == '':
                Textout('\t已使用默认设置')
            else:
                config_list[i] = config
                Textout('\t软件名已设置为：' + config)
            getpass.getpass('\t（回车继续）')

        # 刷新设置
        elif i == 1:
            Wizard_ui(4)
            config = input('\t请设置是否在软件初始化后刷新账户积分，默认否（y/n）：')
            if config == '':
                Textout('\t已设置为不刷新')
                getpass.getpass('\t（回车继续）')
            elif (config == 'y') | (config == 'Y'):
                config_list[i] = True
                Textout('\t已设置为刷新')
                getpass.getpass('\t（回车继续）')
            elif (config == 'n') | (config == 'N'):
                Textout('\t已设置为不刷新')
                getpass.getpass('\t（回车继续）')
            elif config == 'c':
                i -= 2
                getpass.getpass('（回车以回到上一步）')
                getpass.getpass('\t（回车继续）')
            else:
                i -= 1
                Err('\t（错误的输入）')

        # 初始化完成等待时间设置
        elif i == 2:
            Wizard_ui(5)
            config = input('\t请设置软件初始化完成后等待时间（默认0.5秒）：')
            if config == '':
                Textout('\t已使用默认设置')
                getpass.getpass('\t（回车继续）')
            elif config == 'c':
                i -= 2
                getpass.getpass('\t（回车以回到上一步）')
            else:
                try:
                    if float(config) < 0:
                        raise Exception
                    config_list[i] = float(config)
                except:
                    i -= 1
                    Err('\t错误的输入，请输入正数')
                else:
                    Textout('\t初始化完成后等待时间已设置为%f秒' % float(config))
                    getpass.getpass('\t（回车继续）')

        # 退出前等待时间设置
        elif i == 3:
            Wizard_ui(6)
            config = input('\t请设置软件退出前等待时间（默认1秒）：')
            if config == '':
                Textout('\t已使用默认设置')
                getpass.getpass('\t（回车继续）')
            elif config == 'c':
                i -= 2
                getpass.getpass('\t（回车以回到上一步）')
            else:
                try:
                    if float(config) < 0:
                        raise Exception
                    config_list[i] = float(config)
                except:
                    i -= 1
                    Err('\t错误的输入，请输入正数')
                else:
                    Textout('\t退出前等待时间已设置为%f秒' % float(config))
                    getpass.getpass('\t（回车继续）')

        # 文字输出速度设置
        elif i == 4:
            Wizard_ui(7)
            config = input('\t请设置文字输出速度（越小越快，默认0.01）：')
            if config == '':
                Textout('\t已使用默认设置')
                getpass.getpass('\t（回车继续）')
            elif config == 'c':
                i -= 2
                getpass.getpass('\t（回车以回到上一步）')
            else:
                try:
                    if float(config) <= 0:
                        raise Exception
                    config_list[i] = float(config)
                except:
                    i -= 1
                    Err('\t错误的输入，请输入正数')
                else:
                    Textout('\t文字输出速度已设置为%f秒' % float(config))
                    getpass.getpass('\t（回车继续）')

        # 文件名最大重复数设置
        elif i == 5:
            Wizard_ui(8)
            config = input('\t请设置文件名最大重复数（默认100个）：')
            if config == '':
                Textout('\t已使用默认设置')
                getpass.getpass('\t（回车继续）')
            elif config == 'c':
                i -= 2
                getpass.getpass('\t（回车以回到上一步）')
            else:
                try:
                    if int(config) <= 0:
                        raise (Exception)
                    config_list[i] = int(config)
                except:
                    i -= 1
                    Err('\t错误的输入，请输入正整数')
                else:
                    Textout('\t文件名最大重复数已设置为%d个' % int(config))
                    getpass.getpass('\t（回车继续）')

        # 颜色显示设置
        elif i == 6:
            Wizard_ui(9)
            config = input('\t请设置是否完全不显示文字特效，默认否（y/n）：')
            if config == '':
                Textout('\t已设置为显示文字特效')
                getpass.getpass('\t（回车继续）')
            elif (config == 'y') | (config == 'Y'):
                config_list[i] = False
                Textout('\t已设置为完全不显示文字特效')
                getpass.getpass('\t（回车继续）')
            elif (config == 'n') | (config == 'N'):
                Textout('\t已设置为显示文字特效')
                getpass.getpass('\t（回车继续）')
            elif config == 'c':
                i -= 2
                getpass.getpass('（回车以回到上一步）')
                getpass.getpass('\t（回车继续）')
            else:
                i -= 1
                Err('\t错误的输入')

        # 是否返回
        elif i == 7:
            Wizard_ui(9)
            config = input('\t请重新进行设置，默认否（y/n）：')
            if config == '':
                pass
            elif (config == 'y') | (config == 'Y'):
                i = -1
            elif (config == 'n') | (config == 'N'):
                pass
            elif config == 'c':
                i -= 2
                getpass.getpass('（回车以回到上一步）')
                getpass.getpass('\t（回车继续）')
            else:
                i -= 1
                Err('\t错误的输入')
        i += 1

    # 生成设置文件
    config_dict = {
        'name': config_list[0],
        'refresh': config_list[1],
        'enter_time': config_list[2],
        'exit_time': config_list[3],
        'textout_time': config_list[4],
        'name_limit': config_list[5],
        'colorful': config_list[6],
        'ua_list': config_list[7]
    }
    with open('config.conf', 'w') as file:
        json.dump(config_dict, file, indent=4, separators=(',', ': '))
    Textout('\t使用向导运行完成', end='')
    getpass.getpass('（回车继续）')
    os.system(clean_mode)

# 读取设置
try:
    with open('config.conf') as file:
        fileJson = json.load(file)
    name = fileJson['name']
    refresh = fileJson['refresh']
    exit_time = fileJson['exit_time']
    enter_time = fileJson['enter_time']
    textout_time = fileJson['textout_time']
    name_limit = fileJson['name_limit']
    colorful = fileJson['colorful']
    ua_list = fileJson['ua_list']
    if (type(name) != str) | (type(refresh) != bool) | ((type(exit_time) != int) & (type(exit_time) != float)) | (
            (type(enter_time) != int) & (type(enter_time) != float)) | (type(name_limit) != int) | (
            (type(colorful) != int) & (type(colorful) != bool) & (type(colorful) != str)) | (type(ua_list) != list):
        os.remove('config.conf')
        Fatal_err('\t设置文件错误，', '已删除')
except Exception as err:
    Fatal_err('\t读取设置时出现致命错误，错误信息为：', err)
ua = random.choice(ua_list)

# 加密函数和密钥
key = b'12345678'
DES = des(key, CBC, key, pad=None, padmode=PAD_PKCS5)


def DES_Encrypt(data):  # DES加密
    return (binascii.b2a_hex(DES.encrypt(data.encode())).decode())


def DES_Decrypt(data):  # DES解密
    return (DES.decrypt(binascii.a2b_hex(data)).decode())


# 爬虫函数及其变量
post = None
get = None


def Get(http, params=None, succback='', failback='', errback=''):
    global get
    try:
        get = requests.get(http, headers={"User-Agent": ua}, params=params)
    except Exception as err:
        Fatal_err(errback, err)

    if get.status_code == 200:
        if succback != '':
            Textout(succback)
    else:
        Fatal_err(failback, post.status_code)


def Post(http, data, succback='', failback='', errback=''):
    global post
    try:
        post = requests.post(http, headers={"User-Agent": ua}, data=data)
    except Exception as err:
        Fatal_err(errback, err)

    if post.status_code == 200:
        if succback != '':
            print(Color(succback))
    else:
        Fatal_err(failback, post.status_code)


# 界面函数
def Color(text, display=None, foreground=None, background=None):  # 颜色管理
    if type(colorful) == bool:
        if colorful:
            if display == None:
                return (text)
            elif (foreground == None):
                return (('\033[%dm%s\033[0m') % (display, text))
            elif background == None:
                return (('\033[%d;%dm%s\033[0m') % (display, foreground, text))
            else:
                return (('\033[%d;%d;%dm%s\033[0m') % (display, foreground, background, text))
        else:
            return (text)

    else:
        if colorful == 'only_red':
            if display != None:
                if foreground == 31:
                    return (('\033[%d;%dm%s\033[0m') % (display, foreground, text))
                else:
                    return (('\033[%dm%s\033[0m') % (display, text))
            else:
                return (text)
        else:
            if display == None:
                return (('\033[0;%dm%s\033[0m') % (colorful, text))
            elif foreground == 31:
                return (('\033[%d;%dm%s\033[0m') % (display, foreground, text))
            else:
                return (('\033[%d;%dm%s\033[0m') % (display, colorful, text))


def Title_ui():  # 主标题
    os.system(clean_mode)
    print(Color('\t\t' + name + '\n', 1, 34))


def Textout(text, end='\n', display=None, foreground=None, background=None, sleep_time=textout_time):  # 文字输出
    for i in text:
        print(Color(i, display, foreground, background), end='')
        sys.stdout.flush()
        time.sleep(sleep_time)
    print(end=end)


def Download(http):  # 主下载程序函数
    Title_ui()
    print(Color('\t开始下载：') + http)
    Post('http://www.blpack.com/post.php',
         {'usrname': DES_Decrypt(fileJson['user']), 'usrpass': DES_Decrypt(fileJson['passwd']), 'docinfo': http,
          'taskid': 'up_down_doc1'}, failback='\t请求失败，状态码为：', errback='请求错误，错误信息为：')
    phpjsonload = json.loads(post.text)
    if phpjsonload['result'] == 'succ':
        Get(phpjsonload['url'], failback='\t访问失败，状态码为：', errback='\t访问错误，错误信息为：')
        soup = bs(get.text, features='html5lib')
        img_untreated = soup.select_one('body > div:nth-child(2) > div > div:nth-child(2) > img')
        vid_untreated = re.search(r'=([^&]+)&', get.url).group(0)
        vid = vid_untreated[1:len(vid_untreated) - 1]
        if img_untreated == None:
            Post('http://www.blpack.com/downdoc.php', failback='\t验证验证码时返回异常，状态码为：', errback='\t验证验证码时错误，错误信息为',
                 data={'vid': vid, 'v_input': None, 'taskid': 'directDown'})
        else:
            Post('http://www.blpack.com/downdoc.php', failback='\t验证验证码时返回异常，状态码为：', errback='\t验证验证码时错误，错误信息为',
                 data={'vid': vid, 'v_input': '验证', 'taskid': 'directDown'})
        phpjsonload = json.loads(post.text)
        if phpjsonload['result'] == 'down_succ':
            link = phpjsonload['dlink']
        else:
            try:
                Err('\t下载失败。来自服务器的消息：' + phpjsonload['msg'])
            except:
                Err('\t下载失败，请重试。服务器返回：' + phpjsonload['result'])
            return (1)
        link_decode = parse.unquote(link)
        start = link_decode.find('filename="')
        stop = link_decode.find('; filename*')
        if start == -1:
            name = parse.unquote(
                link_decode[link_decode.find('filename*=utf-8') + 17:link_decode.find('&KSSAccessKeyId=') - 1])
        else:
            name = parse.unquote(link_decode[start + 10:stop - 1])

        def write():
            try:
                with open('Download/' + name, 'wb') as file:
                    Get(link, failback='\t服务器相应异常，状态码为：', errback='\t下载时出错，错误信息为：')
                    file.write(get.content)
            except Exception as err:
                Fatal_err('\t写入文件失败,请检查软件权限。错误信息为：', err)
            else:
                Textout('\t文件：' + name + ' 已保存在Download文件夹下')
                getpass.getpass('\t（回车继续）')

        if os.path.exists('Download/' + name):
            Textout('\t文件已存在。')
            task = input('\t是否覆盖？(y/n):')
            if (task == 'y') | (task == 'Y'):
                write()
            elif (task == 'n') | (task == 'N'):
                i = 0
                while True:
                    if i == name_limit:
                        Err('\t同名文件过多')
                        break
                    i += 1
                    name += ('(%d)' % i)
                    if not os.path.exists('users/' + name + '.json'):
                        write()
        else:
            write()
    else:
        Err('\t服务器返回异常，请检查后重试')


# 初始化部分
os.system(clean_mode)
Textout('\t\t' + name, display=1)

# 创建下载文件夹
if not os.path.exists('Download'):
    Textout('\t创建下载文件夹...', end='')
    try:
        os.mkdir('Download')
    except Exception as err:
        Fatal_err('\t创建下载文件夹时出错，错误信息为：', err)
    print(Color('done'))

# 判断用户信息存在与否
if os.path.exists('user.json'):
    path = 'user.json'
else:
    Textout('\t未找到用户文件，请将用户文件(user.json)拖入此窗口并回车')
    path = input(Color('\t用户文件：'))
try:
    if DES_Decrypt(path) != '管理员模式':
        raise (Exception)
except:
    pass

# 管理员菜单
else:
    while True:
        os.system(clean_mode)
        print(Color('\t\t管理员菜单\n', 1, 34))
        Textout('\t[1]加密\n\t[2]解密\n\t[3]创建用户文件\n\t[4]退出', display=0, foreground=36)
        task = input(Color('\n\t请输入要执行的任务：'))

        # 加密
        if task == '1':
            Title_ui()
            Textout('\t结果为：' + DES_Encrypt(input(Color('\t请输入要加密的字符：'))), end='')
            getpass.getpass('（回车继续）')

        # 解密
        elif task == '2':
            Title_ui()
            try:
                Textout('\t结果为：' + DES_Decrypt(input(Color('\t请输入要解密的字符：'))), end='')
            except Exception as err:
                print(Color('\t解密失败，错误信息为：'), end='')
                sys.stdout.flush()
                print(Color(str(err), 0, 31))
            getpass.getpass('（回车继续）')

        # 创建用户文件
        elif task == '3':
            Title_ui()
            user_dict = {}
            user_dict['user'] = DES_Encrypt(input(Color('\t请输入用户名：')))
            user_dict['passwd'] = DES_Encrypt(getpass.getpass(Color('\t请输入密码（无回显）：')))
            name = input(Color('\t请输入要保存的文件名（不包含后缀，默认为user）：'))
            if name == '':
                name = 'user'
            if not os.path.exists('users'):
                Textout('\t创建用户文件夹...', end='')
                try:
                    os.mkdir('users')
                except Exception as err:
                    Fatal_err('\t创建用户文件夹时出错，错误信息为：', err)
                print(Color('done'))


            # 写入文件函数
            def write():
                try:
                    with open('users/' + name + '.json', 'w') as file:
                        json.dump(user_dict, file, indent=4, separators=(',', ': '))
                except Exception as err:
                    Fatal_err('\t写入文件时出错，错误信息为：', err)
                else:
                    Textout('`\t' + name + '.json 已保存到users文件夹')
                    getpass.getpass('\t（回车继续）')


            if os.path.exists('users/' + name + '.json'):
                Textout('\t文件已存在。')
                task = input(Color('\t是否覆盖？(y/n):'))
                if (task == 'y') | (task == 'Y'):
                    write()
                elif (task == 'n') | (task == 'N'):
                    i = 0
                    while True:
                        if i == name_limit:
                            Err('\t同名文件过多')
                            break
                        i += 1
                        name += ('(%d)' % i)
                        if not os.path.exists('users/' + name + '.json'):
                            write()
            else:
                write()

        # 退出
        elif task == '4':
            os.system(clean_mode)
            print(Color('\t\t' + name + '\n', 1))
            Textout('\n\t感谢使用', end='', display=1, foreground=33)
            time.sleep(exit_time)
            os.system(clean_mode)
            sys.exit()

        else:
            Err('\t错误的输入')

# 读取用户信息文件
Textout('\t读取用户信息...', end='')
try:
    with open(path) as file:
        fileJson = json.load(file)
except Exception as err:
    Fatal_err('\t读取用户信息文件失败，错误信息为：', err)
else:
    print(Color('done'))

# 测试用户信息文件
Textout('\t测试用户信息文件...', end='')
try:
    if (DES_Decrypt(fileJson['user']) == b'') | (DES_Decrypt(fileJson['passwd']) == b''):
        Textout('用户信息文件无法解密，请检查后重试')
        getpass.getpass('\t（回车退出）')
        sys.exit()
except Exception as err:
    Fatal_err('\t用户信息解密错误，错误信息为：', err)
else:
    print(Color('done'))

# 测试网络连接
Textout('\t连接远程服务器...', end='')
Get('http://www.blpack.com', succback='done', failback='连接失败，请稍后重试。状态码为：', errback='连接错误，请稍后重试。错误信息为：')
Textout('\t登陆账户...', end='')
Post('http://www.blpack.com/post.php',
     {'usrname': DES_Decrypt(fileJson['user']), 'usrpass': DES_Decrypt(fileJson['passwd']), 'taskid': 'getwealth'},
     failback='\t登陆失败，请稍后重试。状态码为：', errback='\t登陆错误，请稍后重试。状态码为：')
phpjsonload = json.loads(post.text)
try:
    if phpjsonload['result'] == 'succ':
        print(Color('done'))
        Textout('\t初始化完成!')
        time.sleep(enter_time)
except Exception as err:
    Fatal_err('登陆失败:', err)

# 主程序部分
while True:
    # 绘制ui
    Title_ui()
    if refresh:
        refresh = False
        Textout('\t剩余积分：', end='', display=1, foreground=33)
        Post('http://www.blpack.com/post.php',
             {'usrname': DES_Decrypt(fileJson['user']), 'usrpass': DES_Decrypt(fileJson['passwd']),
              'taskid': 'getwealth'}, failback='\t登陆失败，请稍后重试。状态码为：', errback='\t登陆错误，请稍后重试。状态码为：')
        phpjsonload = json.loads(post.text)
        if phpjsonload['result'] == 'succ':
            Textout(phpjsonload['wealth'] + '\n', display=1, foreground=33)
        else:
            Fatal_err('\t服务器返回异常，返回值为：', phpjsonload['result'])
    else:
        Textout('\t剩余积分：' + phpjsonload['wealth'] + '\n', display=0, foreground=33)
    Textout('\t[1]下载文档\n\t[2]刷新\n\t[3]重置\n\t[4]退出', display=0, foreground=36)
    task = input(Color('\n\t请输入要执行的任务：'))

    # 下载文档
    if task == '1':
        Title_ui()
        get_clip = pyperclip.paste()
        if 'https://wenku.baidu.com/view/' in get_clip:
            print(Color('\t已从粘贴板捕获：' + get_clip))
            task = input(Color('\t是否下载该文档？(y/n):'))
            if (task == 'y') | (task == 'Y'):
                Download(get_clip)
            elif (task == 'n') | (task == 'N'):
                http = input(Color('\t请输入文档链接：'))
                if 'https://wenku.baidu.com/view/' in http:
                    Download(http)
                else:
                    Err('\t链接格式不正确，请完整复制文档链接')
            else:
                Textout('\t错误的输入', end='')
                getpass.getpass('（回车继续）')
        else:
            http = input(Color('\t请输入文档链接：'))
            if 'https://wenku.baidu.com/view/' in http:
                Download(http)
            else:
                Err('\t链接格式不正确，请完整复制文档链接')
        refresh = True

    # 刷新
    elif task == '2':
        refresh = True

    # 重置
    elif task == '3':
        Title_ui()
        Textout('\t此操作将删除config.conf文件并退出程序，但不会删除user.json。', display=1, foreground=31)
        task = input(Color('\n\t是否继续(y/n):'))
        if (task == 'y') | (task == 'Y'):
            try:
                os.remove('config.conf')
            except Exception as err:
                Fatal_err('\t删除config.conf失败，错误信息为：', err)
            else:
                Title_ui()
                Textout('\t删除完成')
                Textout('\t感谢使用', end='', display=1, foreground=33)
                time.sleep(exit_time)
                os.system(clean_mode)
                sys.exit()
        elif (task == 'n') | (task == 'N'):
            pass
        else:
            Err('\n错误的输入')

    # 退出
    elif task == '4':
        Title_ui()
        Textout('\t感谢使用', end='', display=1, foreground=33)
        time.sleep(exit_time)
        os.system(clean_mode)
        sys.exit()

    else:
        try:
            if DES_Decrypt(pyperclip.paste()) != '管理员模式':
                raise (Exception)
        except:
            Err('\n\t错误的输入')
        else:
            # 管理员菜单
            while True:
                os.system(clean_mode)
                print(Color('\t\t管理员菜单\n', 1, 34))
                Textout('\t[1]加密\n\t[2]解密\n\t[3]创建用户文件\n\t[4]退出', display=0, foreground=36)
                task = input(Color('\n\t请输入要执行的任务：'))

                # 加密
                if task == '1':
                    Title_ui()
                    Textout('\t结果为：' + DES_Encrypt(input(Color('\t请输入要加密的字符：'))), end='')
                    getpass.getpass('（回车继续）')

                # 解密
                elif task == '2':
                    Title_ui()
                    try:
                        Textout('\t结果为：' + DES_Decrypt(input(Color('\t请输入要解密的字符：'))), end='')
                    except Exception as err:
                        print(Color('\t解密失败，错误信息为：'), end='')
                        sys.stdout.flush()
                        print(Color(str(err), 0, 31))
                    getpass.getpass('（回车继续）')

                # 创建用户文件
                elif task == '3':
                    Title_ui()
                    user_dict = {}
                    user_dict['user'] = DES_Encrypt(input(Color('\t请输入用户名：')))
                    user_dict['passwd'] = DES_Encrypt(getpass.getpass(Color('\t请输入密码（无回显）：')))
                    name = input(Color('\t请输入要保存的文件名（不包含后缀，默认为user）：'))
                    if name == '':
                        name = 'user'
                    if not os.path.exists('users'):
                        Textout('\t创建用户文件夹...', end='')
                        try:
                            os.mkdir('users')
                        except Exception as err:
                            Fatal_err('\t创建用户文件夹时出错，错误信息为：', err)
                        print(Color('done'))


                    # 写入文件函数
                    def write():
                        try:
                            with open('users/' + name + '.json', 'w') as file:
                                json.dump(user_dict, file, indent=4, separators=(',', ': '))
                        except Exception as err:
                            Fatal_err('\t写入文件时出错，错误信息为：', err)
                        else:
                            Textout('`\t' + name + '.json 已保存到users文件夹')
                            getpass.getpass(Color('\t（回车继续）'))


                    if os.path.exists('users/' + name + '.json'):
                        Textout('\t文件已存在。')
                        task = input(Color('\t是否覆盖？(y/n):'))
                        if (task == 'y') | (task == 'Y'):
                            write()
                        elif (task == 'n') | (task == 'N'):
                            i = 0
                            while True:
                                if i == name_limit:
                                    Err('\t同名文件过多')
                                    break
                                i += 1
                                name += ('(%d)' % i)
                                if not os.path.exists('users/' + name + '.json'):
                                    write()
                    else:
                        write()

                # 退出
                elif task == '4':
                    break

                else:
                    Err('\t错误的输入')