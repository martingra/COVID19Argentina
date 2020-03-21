import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

currentDirectory = os.getcwd()
  
# Leemos el archivo csv con los casos
confirmed_df = pd.read_csv(currentDirectory + "\\data_world\\time_series_19-covid-Confirmed.csv") 
# deaths_df = pd.read_csv(currentDirectory + "\\data\\time_series_19-covid-Deaths.csv") 

del confirmed_df['Lat']
del confirmed_df['Long']
del confirmed_df['Province/State']

confirmed_df = confirmed_df.set_index('Country/Region')

confirmed_df.columns = pd.to_datetime(confirmed_df.columns)

legend = []


confirmed_df.loc['Argentina',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Argentina')
confirmed_df.loc['Spain',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('España')
confirmed_df.loc['Italy',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Italia')
confirmed_df.loc['Germany',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Alemania')
confirmed_df.loc['US',:].sum(axis=0).plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Estados Unidos')
confirmed_df.loc['France',:].sum(axis=0).plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Francia')
confirmed_df.loc['United Kingdom',:].sum(axis=0).plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Reino Unido')
confirmed_df.loc['China',:].sum(axis=0).plot.line(marker="o", linewidth=1, markersize=4)
legend.append('China')
confirmed_df.loc['Korea, South',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Corea del Sur')
confirmed_df.loc['Iran',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Iran')


plt.title('Cantidad de afectados COVID-19 Mundo')
plt.legend(legend)

plt.xlabel('Día')
plt.ylabel('Cantidad de afectados')

plt.show()