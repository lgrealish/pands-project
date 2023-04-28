# analysis.py
# Author: Linda Grealish
# This program reads in data from the iris.csv file and produces various analysis


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys


# variable ifds stands for iris flower dataset
# with read.csv() we are reading the .csv file and storing it into ifds variable for further use and manipulation
# with "index_col='Id'" I am eliminating the Id column as it is unnecessary in this case
# reference for index_col: https://realpython.com/python-csv/

ifds = pd.read_csv('iris.csv', index_col='Id')
'''
print(ifds)
print (ifds.describe())
print (ifds.info())


#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
print (ifds["Species"].value_counts())

ifds.hist()
plt.show()

sns.set()
sns.pairplot(ifds, hue="Species")
plt.show()
'''
def sepal_length_hist():
    # https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
    plt.figure(figsize = (9,9))
    
    
    # https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/
    sns.distplot(iris_s["SepalLengthCm"],  kde = False, label = "Iris setosa", color = "deeppink", )
    sns.distplot(iris_vers["SepalLengthCm"],  kde = False, label = "Iris versicolor", color = "mediumorchid")
    sns.distplot(iris_virg["SepalLengthCm"],  kde = False, label = "Iris virginica", color = "navy")
    plt.title("Sepal length in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    #plt.savefig("Sepal-lenght.png")
    plt.show()

    #function for plotting a histogram for sepal width
def sepal_width_hist():
    plt.figure(figsize = (9,9))
    sns.distplot(iris_s["SepalWidthCm"],  kde = False, label = "Iris setosa", color = "deeppink")
    sns.distplot(iris_vers["SepalWidthCm"],  kde=False, label = "Iris versicolor", color = "mediumorchid")
    sns.distplot(iris_virg["SepalWidthCm"],  kde=False, label = "Iris virginica", color = "navy")
    plt.title("Sepal width in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    plt.savefig("Sepal-width.png")
    plt.show()
