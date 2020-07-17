# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 19:27:37 2020

@author: Sushir
"""

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

covid = pd.read_csv("Datasets/time_series_covid19_confirmed_global.csv")
#covid.head(10)
#covid.shape

dataframe = covid.drop(["Lat","Long"],axis=1,inplace=True)
#dataframe.head(10)

covid_agg = covid.groupby("Country/Region").sum()
#covid_agg.head()
#covid_agg.shape

#To visualize
##covid_agg.loc["China"]
covid_agg.loc["China"].plot()
covid_agg.loc["Brazil"].plot()
covid_agg.loc["India"].plot()
plt.legend()

#Calculate first derivative
covid_agg.loc["India"].diff().plot()
#Max. cases in 24hrs
covid_agg.loc["India"].diff().max()

#Max. infection rate for all countries
c = list(covid_agg.index)
max_infect = []
for i in c :
    max_infect.append(covid_agg.loc[i].diff().max())
#max_infect
covid_agg["Max_infection_rate"] = max_infect
#covid_agg.head()

newDF = pd.DataFrame(covid_agg["Max_infection_rate"])
newDF.head()


happyData = pd.read_csv("Datasets/worldwide_happiness_report.csv")
#happyData.head()

notreq = ["Overall rank","Score","Perceptions of corruption","Generosity"]
happyData.drop(notreq,axis=1,inplace=True)
happyData.head()

happyData.set_index("Country or region",inplace=True)
happyData.shape
newDF.shape

# Not same no. of rows in newDF and happyData 
#Perform inner join

data = newDF.join(happyData,how="inner")
data.head()

#correlation matrix
data.corr()

#plot results
x = data["Healthy life expectancy"]
y = data["Max_infection_rate"]
#sb.scatterplot(x,y)
#Scaling
sb.scatterplot(x,np.log(y))
sb.regplot(x,np.log(y))

#Can plot for other columns like Max_infection_rate Vs GDP per capita...etc

