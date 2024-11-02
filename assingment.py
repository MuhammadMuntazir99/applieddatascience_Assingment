# i Have choosen olympics Data 2024 From Kaggle.com 
import pandas
import matplotlib.pyplot as plot
import seaborn

#file loading & reading some top lines from file 
olympicsecnomics = pandas.read_csv(r'C:\Users\muntazir\Downloads\olympics-economics.csv')
print(olympicsecnomics.head())

#Data Cleaning 
print(olympicsecnomics.isnull().sum())
olympicsecnomics.drop_duplicates(inplace=True)

#Bar Chart
plot.figure(figsize=(14,6))
plot.bar(olympicsecnomics['country'],olympicsecnomics['gold'],color='gold')
plot.ylabel('Gold medals')
plot.xlabel('Country')
plot.xticks(rotation=90)  
plot.show()

# Heat Map
columns_choosen = olympicsecnomics[['gold','total','gdp','population']]
comatrix = columns_choosen.corr()
plot.figure(figsize=(12,12))
seaborn.heatmap(comatrix,annot=True,cmap='PuOr',linewidths=0.7)
plot.show()

# Scatter Chart 
plot.figure(figsize=(8,8))
plot.scatter(olympicsecnomics['gdp'],olympicsecnomics['gold'],color='red',edgecolor='black')
plot.ylabel('Gold medals')
plot.xlabel('GDP')
plot.show()