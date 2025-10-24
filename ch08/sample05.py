import os
import pandas as pd
from matplotlib import pyplot as plt

def get_covid_data(iso_code):
    file_path = './data/common_covid.csv'

    df = pd.read_csv(file_path)
    filter_df = df[df.iso_code == iso_code]
    index_df = filter_df.set_index('date')

    rate = 1

    return index_df['total_cases'] * rate
#end-def

kor_data = get_covid_data('KOR')
usa_data = get_covid_data('USA')
fra_data = get_covid_data('FRA')
gbr_data = get_covid_data('GBR')
pol_data = get_covid_data('POL')
index_data = kor_data.index

data = {
    'KOR': kor_data,
    'USA': usa_data,
    'FRA': fra_data,
    'GBR': gbr_data,
    'POL': pol_data,
}

covid_df = pd.DataFrame(data, index = index_data)
covid_df[:].plot.line(rot = 45)
plt.show()