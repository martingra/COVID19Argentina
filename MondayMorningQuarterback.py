import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

currentDirectory = os.getcwd()

days_margin = 18

# Leemos el archivo csv con los casos
confirmed_df = pd.read_csv(currentDirectory + "\\data_world\\time_series_19-covid-Confirmed.csv") 
# deaths_df = pd.read_csv(currentDirectory + "\\data\\time_series_19-covid-Deaths.csv") 

del confirmed_df['Lat']
del confirmed_df['Long']
del confirmed_df['Province/State']

confirmed_df = confirmed_df.set_index('Country/Region')

confirmed_df.columns = pd.to_datetime(confirmed_df.columns)

legend = []


arg = confirmed_df.loc['Argentina',:][confirmed_df.loc['Argentina',:]>0]
arg.reset_index(drop=True, inplace=True)
arg.plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Argentina')

comp = confirmed_df.loc['Italy',:][confirmed_df.loc['Italy',:]>0]
comp = comp[0:arg.count()+days_margin]
comp.reset_index(drop=True, inplace=True)
comp.plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Italia')

plt.title('Diario del Lunes COVID-19 Argentina vs Italia')
plt.legend(legend)

plt.xlabel('Día')
plt.ylabel('Cantidad de afectados')

plt.yticks(np.arange(0, comp.max(), comp.max()/20))

plt.grid(True)

plt.show()


###########################################################################

legend = []

arg.plot.line(marker="o", linewidth=1, markersize=4)
legend.append('Argentina')

comp = confirmed_df.loc['Spain',:][confirmed_df.loc['Spain',:]>0]
comp = comp[0:arg.count()+days_margin]
comp.reset_index(drop=True, inplace=True)
comp.plot.line(marker="o", linewidth=1, markersize=4)
legend.append('España')

plt.title('Diario del Lunes COVID-19 Argentina vs España')
plt.legend(legend)

plt.xlabel('Día')
plt.ylabel('Cantidad de afectados')

plt.show()