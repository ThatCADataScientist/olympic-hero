# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(columns = {'Total':'Total_Medals'},inplace = True)
data.head()


# --------------

data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])
data['Better_Event']
better_event = data['Better_Event'].value_counts().idxmax()
better_event


# --------------
# #Code starts here
top_countries = pd.DataFrame(data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']])
top_countries=top_countries[:-1]

def top_ten(df,Col):
    country_list=list()
    country_list= list((df.nlargest(10,Col)['Country_Name']))
    return country_list
top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
common = [x for x in top_10_summer if x in top_10_winter and x in top_10]



# --------------
#Code starts here
summer_df=top_countries[top_countries['Country_Name'].isin(top_10_summer)]
winter_df=top_countries[top_countries['Country_Name'].isin(top_10_winter)]
top_df=top_countries[top_countries['Country_Name'].isin(top_10)]
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))
ax_1.bar(data['Country_Name'],data["Total_Summer"])
ax_1.set(title='Top 10 in Summer')
ax_2.bar(data['Country_Name'],data["Total_Winter"])
ax_2.set(title='Top 10 in Winter')
ax_3.bar(data['Country_Name'],data["Total_Medals"])
ax_3.set(title='Top 10 in Both Seasons')
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=(data['Gold_Summer']/data['Total_Summer'])
summer_max_ratio = summer_df['Golden_Ratio'].max(axis = 0)
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df['Golden_Ratio']=(data['Gold_Winter']/data['Total_Winter'])
winter_max_ratio = winter_df['Golden_Ratio'].max(axis = 0)
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio']=(data['Gold_Total']/data['Total_Medals'])
top_max_ratio = top_df['Golden_Ratio'].max(axis=0)
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']


# --------------
#Code starts here
data_1=data.drop(data.tail(1).index)
data_1['Total_Points']=(data['Gold_Total']*3)+(data['Silver_Total']*2)+(data['Bronze_Total']*1)
most_points = data_1['Total_Points'].max(axis=0)
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']


# --------------
#Code starts here
best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.show()


