import pandas as pd
import matplotlib as plt

from ch05.common_function import init_plt

init_plt()
COL_POPULATION = 'population'
COL_TOTAL_CASES = 'total_cases'


def get_covid_data_series(file_path):
    df = pd.read_csv(file_path)
    index_df = df.set_index('date')

    population = df['population'].iat[0]

    return {
        'population': population,
        'data_sr': index_df['total_cases']
    }


kor_data = get_covid_data_series('../ch05/data/covid_korea.csv')
kor_data_index = kor_data['data_sr'].index

hi_data = get_covid_data_series('./hi_covid_data.csv')
hi_data_index = hi_data['data_sr'].index

data_index = kor_data_index.union(hi_data_index)