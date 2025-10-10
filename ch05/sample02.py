import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

from ch05.common_function import is_windows_platform, is_mac_platform, get_font_name

#한글폰트설정
rc('font', family = get_font_name())
plt.rcParams['axes.unicode_minus'] = False
jumsu1 = [3.5, 4.0, 4.5, 3.8]
jumsu2 = [3.0, 4.5, 4.0, 3.2]
year = [2024,2025,2026,2027]
jumsu_df = pd.DataFrame(
    {
        '점수1': jumsu1,
        '점수2': jumsu2,
    }, index  = year)


lines = jumsu_df.plot.line()
plt.show()
