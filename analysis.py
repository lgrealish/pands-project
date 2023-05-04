# analysis.py
# Author: Linda Grealish
# This program reads in data from the iris.csv file and produces various analysis, plot and summary outputs

# https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
# https://gist.github.com/accessnash/7c255c0cfc12d2725ac79f6710ba19a3
# https://notebook.community/xR86/ml-stuff/kaggle/iris/Simple%20analysis%20of%20Iris%20dataset
# https://realpython.com/pandas-plot-python/

# import the modules needed 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

# use the Pandas library to load the CSV file and create a dataframe
# variable ifds stands for iris flower dataset
# with "index_col='Id'" I am eliminating the Id column as it is unnecessary in this case
# reference for index_col: https://realpython.com/python-csv/
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
# csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

ifds = pd.read_csv("iris.csv", index_col = "Id")


# defining the three different species variables
iris_s = ifds[ifds.Species == "Iris-setosa"]
iris_vers = ifds[ifds.Species == "Iris-versicolor"]
iris_virg = ifds[ifds.Species == "Iris-virginica"]

# code for outputting variables summary data to .txt file
# https://www.geeksforgeeks.org/sys-stdout-write-in-python/
def summary_output():
    sys.stdout = open ("output_summary_variabe.txt","w")
    print ("\n")
    print ("==============================================================================")
    print ("Details of the whole dataset:")
    print ("\n")
    print (ifds)
    print ("==============================================================================")
    print ("Summary Statistics for the Iris Flower Dataset Dataframe")
    print ("\n")
    print (ifds.describe())
    print ("\n")
    print ("==============================================================================")
    print ("A concise summary of the Iris Flower Dataset Dataframe")
    print ("\n")
    print (ifds.info())
    print ("\n")
    print ("==============================================================================")
    print ("The number of distinct classes or species types of iris in the dataframe")
    print ("\n")
    print (ifds.nunique)
    print ("\n")
    print ("==============================================================================")
    print("Number of occurances of each of the species:")
    print ("\n")
    # https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
    print (ifds["Species"].value_counts())
    print ("\n")
    print ("In percentile:")
    print("\n")
    # https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6
    print (((ifds["Species"].value_counts(normalize=True))*100))
    print ("\n")
    print ("==============================================================================")
    # https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset
    print ("A summary of the mean and median for sepal length, sepal width, petal length \n and petal width for each of the three species")
    print ("\n")
    print(ifds.groupby('Species').agg([np.mean, np.median]))
    print ("\n")
    print ("==============================================================================")
    sys.stdout.close()    
'''
# https://realpython.com/pandas-groupby/#pandas-groupby-putting-it-all-together
# https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset
# https://www.geeksforgeeks.org/pandas-groupby-and-computing-median/
# this code uses the groupby() to summarise the mean and median sepal width, sepal length,
# petal length and petal width for each of the species variables
ifds.groupby('Species').agg(['mean', 'median']).describe() # passing a list of recognized strings
print(ifds.groupby('Species').agg([np.mean, np.median]))
'''

# function for plotting a histogram for sepal length
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
    plt.savefig("Sepal-width.png")
    plt.show()

# function for plotting a histogram for petal length
def petal_length_hist():
    plt.figure(figsize = (9,9))
    sns.distplot(iris_s["PetalLengthCm"],  kde = False, label = "Iris setosa", color = "blue")
    sns.distplot(iris_vers["PetalLengthCm"],  kde = False, label = "Iris versicolor", color = "orange")
    sns.distplot(iris_virg["PetalLengthCm"],  kde = False, label = "Iris virginica", color = "green")
    plt.title("Petal length in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    plt.savefig("Petal-lenght.png")
    plt.show()

# function for plotting a histogram for petal width
def petal_width_hist():
    plt.figure(figsize = (9,9))
    sns.distplot(iris_s["PetalWidthCm"],  kde = False, label = "Iris setosa", color = "blue")
    sns.distplot(iris_vers["PetalWidthCm"],  kde = False, label = "Iris versicolor", color = "orange")
    sns.distplot(iris_virg["PetalWidthCm"],  kde = False, label = "Iris virginica", color = "green")
    plt.title("Petal width in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    plt.savefig("Petal-width.png")
    plt.show()

def histograms():
    sepal_length_hist()
    sepal_width_hist()
    petal_length_hist()
    petal_width_hist()



# https://datagy.io/seaborn-pairplot/
# https://www.javatpoint.com/pair-plot-in-python

def pairplot():
    sns.pairplot(ifds,hue='Species')
    plt.savefig("Iris-dataset-pairplot.png")
    plt.show()


# https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset

# function for plotting a scatterplot for sepal length and width
def sepal_length_width_scat():
    plt.figure(figsize = (9,9))
    sns.scatterplot(x = "SepalLengthCm", y = "SepalWidthCm", data = ifds)
    plt.title("Sepal length and Sepal width comparison")
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.legend()
    plt.show()

# function for plotting a scatterplot for petal length and width
def petal_length_width_scat():
    plt.figure(figsize = (9,9))
    sns.scatterplot(x = "PetalLengthCm", y = "PetalWidthCm", data = ifds)
    plt.title("Petal length and Petal width comparison")
    plt.xlabel("Petal length")
    plt.ylabel("Petal width")
    plt.legend()
    plt.savefig("Petal-length-width.png")
    plt.show()

def scatterplots():
    sepal_length_width_scat()
    petal_length_width_scat()

summary_output()

#histograms()
#scatterplots()
#pairplot()   