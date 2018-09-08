# _*_ coding:utf-8 _*_

import requests
import re

import time

import os


with open('lorem_ipsum', 'r', encoding='UTF-8') as f:

    string = f.read()
    p_line = re.sub('[\u4E00-\u9FA5]', '', string)
    pp_line = re.sub(
        '[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]', '', p_line)

with open('C:/Users/moochergaga/project/Tools/lorem_ipsum2', 'w', encoding='UTF-8') as f2:
    f2.write(pp_line)
