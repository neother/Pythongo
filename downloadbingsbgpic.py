
'''
error code
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml.
reason: need to install lxml lib
1. pip install wheel
2. download the lxml file: www.lfd.uci.edu/~gohlke/pythonlibs/
3. install the downloaded file: pip install lxml_文件名.whl
'''
# codes are used to download the background pic. of the ulr www.bing.com.

import requests
import re
from bs4 import BeautifulSoup
import time
import win32api
import win32con
import win32gui
import os

URL = requests.get('https://cn.bing.com/?FORM=BEHPTB&ensearch=1')
#URL = requests.get('https://cn.bing.com')
soup = BeautifulSoup(URL.text, 'lxml')   # lxml is parser
#.text will return the unicode data
html = soup.find_all('script')
html = str(html)
reg = re.compile('az.*?jpg+', re.M | re.S)
out = reg.search(html).group()
iurl = 'https://cn.bing.com/' + out
im = requests.get(iurl).content
#.content  will return the byte type data

date = time.strftime('%m-%d-%Y-%H%M%S', time.localtime())
path = 'D:/BingPic/' + date + '.jpg'

print(path)

with open(path, 'wb')as imf:

    imf.write(im)

# set the desktop background picture with the win32 API
# open the register path
reg_key = win32api.RegOpenKeyEx(
    win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
#
win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
#
win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
# refresh the desktop
win32gui.SystemParametersInfo(
    win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)
print("Setting completed")
