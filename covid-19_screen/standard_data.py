# 使用pandas解析excel文件

import pandas as pd

df = pd.read_excel("covid-19_vaccinated.xlsx", engine="openpyxl")

# get min and max value
percent_min = df.describe()['Percent'].min()
percent_max = df.describe()['Percent'].max()
#
fully_vaccinated_min = df.describe()['Fully vaccinated'].min()
fully_vaccinated_max = df.describe()['Fully vaccinated'].max()
#
