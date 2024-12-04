import pandas as pd
import numpy as np
p=pd.read_csv('AQI_Data.csv')
print('First 8 rows: \n',p.head(8))
print('Last 5 rows: \n',p.tail(5))
print('dtype and number of non- null values in each column: \n')
print(p.info())

m= p.groupby('City')['AQI'].apply(lambda x: np.mean(x))
print('Cities with mean AQI: \n',m)

maxPM=p.groupby('City')['PM2.5'].apply(lambda x: np.max(x))
print('Cities with their max PM2.5: \n',maxPM)

minPM=p.groupby('City')['PM10'].apply(lambda x: np.min(x))
print('Cities with their min PM10: \n',minPM)

q= dict(zip(p['City'].unique(), np.array([len(p[p['City'] == city]) for city in p['City'].unique()])))
print('Rows corressponding to each city: \n : ',q)

p['total'] = np.sum(p[['PM2.5','PM10','NO2','CO','O3','SO2']], axis=1)
print(p['total'])

p['total'].to_csv('pollutant.txt', mode='w', index=False)
