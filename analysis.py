import numpy as py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# variable ids stands for iris flower dataset
# with read.csv() we are reading the .csv file and storing it into ifds variable for further use and manipulation
# with "index_col='Id'" I am eliminating the Id column as it is unnecessary in this case
# reference for index_col: https://realpython.com/python-csv/

ids = pd.read_csv('iris.csv', index_col='Id')

print(ids)
print (ids.describe())
print (ids.info())


#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
print (ids["Species"].value_counts())

ids.hist()
plt.show()

sns.set()
sns.pairplot(ids, hue="Species")
plt.show()