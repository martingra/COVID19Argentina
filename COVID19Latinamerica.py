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
confirmed_df.loc['Brazil',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Brasil')
confirmed_df.loc['Uruguay',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Uruguay')
confirmed_df.loc['Peru',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Peru')
confirmed_df.loc['Chile',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Chile')
confirmed_df.loc['Bolivia',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Bolivia')
confirmed_df.loc['Ecuador',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Ecuador')
confirmed_df.loc['Colombia',:].plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Colombia')


plt.title('Cantidad de afectados COVID-19 Mundo')
plt.legend(legend)

plt.xlabel('Día')
plt.ylabel('Cantidad de afectados')

plt.show()