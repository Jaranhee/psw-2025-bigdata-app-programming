import os.path

import pandas as pd

covid_file_path = '../ch04/data/owid-covid-data.csv'
df = pd.read_csv(covid_file_path)

# 원하는 컬럼만
selected_columns = ['iso_code', 'location', 'date', 'total_cases', 'population']
selected_df = df[selected_columns]

#South Korea
south_korea_df = selected_df[selected_df.location == 'South Korea']
print('-'*50)
print(south_korea_df.head())

#data 칼럼에 인덱스 설정
korea_date_index_df = south_korea_df.set_index('date')
print('-'*50)
print(korea_date_index_df.head)

#저장(dataframe -> csv파일로)
korea_date_index_df.to_csv('./data/covid_korea.csv', encoding = 'UTF-8')

#location을 미국으로 하고, date를 인덱스로 설정하는 df 실습
usa_df = selected_df[selected_df.location == 'United States']
print('-'*50)
print(usa_df.head())

usa_date_index_df = usa_df.set_index('date')
print('-'*50)
print(usa_date_index_df.head)

"""iso code 가져오기
iso_code_list = raw_df['iso_code']
print('-'*50)
print(iso_code_list.unique())
"""

#저장(usa dataframe -> csv파일로)
usa_date_index_df.to_csv('./data/covid_usa.csv')













