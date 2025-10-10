import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import platform

#현재 파이썬이 열려 있는 os 확인
system = platform.system()
print(system)
'Windows'
'Darwin'
'Linux'

def is_windows_platform():
    return platform.system() == 'Windows'
def is_mac_platform():
    return platform.system() == 'Darwin'
def is_linux_platform():
    return platform.system() == 'Linux'

def get_font_name():
    if is_mac_platform():
        return 'AppleGothic'
    elif is_linux_platform():
        return 'linuxfont!!'
    else:
        return 'Malgun Gothic'

#한글폰트 초기화
def init_plt():
    rc('font', family=get_font_name())
    plt.rcParams['axes.unicode_minus'] = False