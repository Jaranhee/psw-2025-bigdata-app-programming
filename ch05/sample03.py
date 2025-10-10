import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

from ch05.common_function import is_windows_platform, is_mac_platform, get_font_name, init_plt

init_plt()

def get_covid_data_series(file_path):
    kor_df = pd.read_csv(file_path)
    kor_index_df = kor_df.set_index('date')
    return kor_index_df['total_cases']

kor_data = get_covid_data_series('data/covid_korea.csv')
usa_data = get_covid_data_series('data/covid_usa.csv')
index_data = kor_data.index

covid_df = pd.DataFrame(
    {
        '대한민국': kor_data,
        '미국': usa_data,
    }, index  = index_data)


lines = covid_df.plot.line()
plt.show()



print('-'*50)
print(index_data)

