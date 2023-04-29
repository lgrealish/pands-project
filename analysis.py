# analysis.py
# Author: Linda Grealish
# This program reads in data from the iris.csv file and produces various analysis


# import the modules needed 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

# reading the CSV file - iris.csv
# variable ifds stands for iris flower dataset
# with "index_col='Id'" I am eliminating the Id column as it is unnecessary in this case
# reference for index_col: https://realpython.com/python-csv/
ifds = pd.read_csv("iris.csv", index_col = "Id")
#show()

iris_s = ifds[ifds.Species == "Iris-setosa"]
iris_vers = ifds[ifds.Species == "Iris-versicolor"]
iris_virg = ifds[ifds.Species == "Iris-virginica"]


def sepal_length_hist():
    # https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
    plt.figure(figsize = (9,9))
    
    
    # https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/
    sns.distplot(iris_s["SepalLengthCm"],  kde = False, label = "Iris setosa", color = "blue", )
    sns.distplot(iris_vers["SepalLengthCm"],  kde = False, label = "Iris versicolor", color = "orange")
    sns.distplot(iris_virg["SepalLengthCm"],  kde = False, label = "Iris virginica", color = "green")
    plt.title("Sepal length in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    #plt.savefig("Sepal-lenght.png")
    plt.show()

    # function for plotting a histogram for sepal width
def sepal_width_hist():
    plt.figure(figsize = (9,9))
    sns.distplot(iris_s["SepalWidthCm"],  kde = False, label = "Iris setosa", color = "blue")
    sns.distplot(iris_vers["SepalWidthCm"],  kde=False, label = "Iris versicolor", color = "orange")
    sns.distplot(iris_virg["SepalWidthCm"],  kde=False, label = "Iris virginica", color = "green")
    plt.title("Sepal width in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    #plt.savefig("Sepal-width.png")
    plt.show()

#function for plotting a histogram for sepal width
def petal_length_hist():
    plt.figure(figsize = (9,9))
    sns.distplot(iris_s["PetalLengthCm"],  kde = False, label = "Iris setosa", color = "blue")
    sns.distplot(iris_vers["PetalLengthCm"],  kde = False, label = "Iris versicolor", color = "orange")
    sns.distplot(iris_virg["PetalLengthCm"],  kde = False, label = "Iris virginica", color = "green")
    plt.title("Petal length in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    #plt.savefig("Petal-lenght.png")
    plt.show()