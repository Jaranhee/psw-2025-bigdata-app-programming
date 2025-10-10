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

#location을 미국으로 하고, date를 인덱스로 설정하는 df 실습


















