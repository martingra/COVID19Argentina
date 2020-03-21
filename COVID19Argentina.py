import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

currentDirectory = os.getcwd()
  
# Leemos el archivo csv con los casos
confirmed_df = pd.read_csv(currentDirectory + "\\data\\time_series_19-covid-Confirmed.csv") 
deaths_df = pd.read_csv(currentDirectory + "\\data\\time_series_19-covid-Deaths.csv") 

del confirmed_df['Lat']
del confirmed_df['Long']
del confirmed_df['Country/Region']

confirmed_df = confirmed_df.set_index('Province/State')

confirmed_df.columns = pd.to_datetime(confirmed_df.columns)

tot_arg = confirmed_df.sum(axis=0)

tot_arg.plot.line(marker="o", linewidth=3, markersize=8)

legend = ['Argentina']

for idx in confirmed_df.index:
    if(confirmed_df.loc[idx,:].sum() > 0):
        confirmed_df.loc[idx,:].plot.line(marker="o", linewidth=1, markersize=4)
        legend.append(idx)

plt.title('Cantidad de afectados COVID-19 Argentina')
plt.legend(legend)

plt.xlabel('Día')
plt.ylabel('Cantidad de afectados')

plt.show()