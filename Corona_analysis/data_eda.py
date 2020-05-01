import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('state_wise.csv')
data['Date'] = pd.to_datetime(data['Date'],dayfirst=True)
#total cases
grouped = data.groupby(data['Name of State / UT']).sum()
sns.barplot(y = grouped.index ,x= grouped['Total Confirmed cases (Indian National)'] )

#by date analysis

grouped_by_date = data.groupby(data['Date']).sum()
plt.figure(figsize=(17,16))

plt.xticks(rotation=90)
sns.set_style('dark')
sns.lineplot(data=grouped_by_date["Total Confirmed cases"],label="Total Confirmed cases")
sns.lineplot(data=grouped_by_date["Death"],label='deaths')
sns.lineplot(data=grouped_by_date['Cured/Discharged/Migrated'],label= 'Cured/Discharged/Migrated')


#active_data

sns.set_style('dark')
grouped_active_data=data.groupby("Name of State / UT").sum()
grouped_active_data=(grouped_active_data.sort_values(by="Active cases"))
plt.xticks(rotation=90)
sns.barplot(x=grouped_active_data['Active cases'], y=grouped_active_data.index)






