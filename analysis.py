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
'''
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']
ifds = pd.read_csv(csv_url, names = col_names)
'''
# https://www.youtube.com/watch?v=02BFXhPQWHQ
ifds = pd.read_csv("iris.csv", index_col = "Id")


# defining the three different species variables
iris_s = ifds[ifds.Species == "Iris-setosa"]
iris_vers = ifds[ifds.Species == "Iris-versicolor"]
iris_virg = ifds[ifds.Species == "Iris-virginica"]

# code for outputting variables summary data to .txt file
# https://www.geeksforgeeks.org/sys-stdout-write-in-python/
def summary_output():
    sys.stdout = open ("output_summary_variable.txt","w")
    print ("\n")
    print ("==============================================================================")
    print ("Details of the whole dataset:")
    print ("\n")
    print (ifds)
    print ("==============================================================================")
    print ("The number of null or missing values in the Iris Flower Dataframe:")
    print ("\n")
    print (ifds.isnull().sum())
    print ("\n")
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
    print (ifds.groupby('Species').agg([np.mean, np.median]))
    print ("\n")
    print ("==============================================================================")
    # https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.describe.html
    # https://note.nkmk.me/en/python-pandas-t-transpose/#:~:text=Use%20the%20T%20attribute%20or,columns%20swapped%20(%3D%20transposed%20object).
    print ("A summary of the count, mean, median, standard deviation, percentiles for each \n of the 4 variables and grouped by species type")
    print ("\n")  
    # using the .T function to transpose (swap the columns and rows) to make the output easier to read)  
    print (ifds.groupby("Species").describe().T)
    sys.stdout.close()    
''
# https://realpython.com/pandas-groupby/#pandas-groupby-putting-it-all-together
# https://www.geeksforgeeks.org/pandas-groupby-and-computing-median/
# https://datascienceparichay.com/article/pandas-groupby-median/

# function for plotting a histogram for sepal length
def sepal_length_hist():
    # https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
    plt.figure(figsize = (9,9))
    # https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/
    # https://medium.com/swlh/how-to-create-a-seaborn-palette-that-highlights-maximum-value-f614aecd706b
    sns.histplot(iris_s["SepalLengthCm"],  kde = False, label = "Iris setosa", color = "lightblue", )
    sns.histplot(iris_vers["SepalLengthCm"],  kde = False, label = "Iris versicolor", color = "lightslategray")
    sns.histplot(iris_virg["SepalLengthCm"],  kde = False, label = "Iris virginica", color = "steelblue")
    plt.title("Sepal length in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    plt.savefig("Sepal-length.png")
    plt.show()
  
# function for plotting a histogram for sepal width
def sepal_width_hist():
    plt.figure(figsize = (9,9))
    sns.histplot(iris_s["SepalWidthCm"],  kde = False, label = "Iris setosa", color = "lightblue")
    sns.histplot(iris_vers["SepalWidthCm"],  kde=False, label = "Iris versicolor", color = "lightslategray")
    sns.histplot(iris_virg["SepalWidthCm"],  kde=False, label = "Iris virginica", color = "steelblue")
    plt.title("Sepal width in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    plt.savefig("Sepal-width.png")
    plt.show()

# function for plotting a histogram for petal length
def petal_length_hist():
    plt.figure(figsize = (9,9))
    sns.histplot(iris_s["PetalLengthCm"],  kde = False, label = "Iris setosa", color = "lightblue")
    sns.histplot(iris_vers["PetalLengthCm"],  kde = False, label = "Iris versicolor", color = "lightslategray")
    sns.histplot(iris_virg["PetalLengthCm"],  kde = False, label = "Iris virginica", color = "steelblue")
    plt.title("Petal length in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    plt.savefig("Petal-length.png")
    plt.show()

# function for plotting a histogram for petal width
def petal_width_hist():
    plt.figure(figsize = (9,9))
    sns.histplot(iris_s["PetalWidthCm"],  kde = False, label = "Iris setosa", color = "lightblue")
    sns.histplot(iris_vers["PetalWidthCm"],  kde = False, label = "Iris versicolor", color = "lightslategray")
    sns.histplot(iris_virg["PetalWidthCm"],  kde = False, label = "Iris virginica", color = "steelblue")
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
    # using the hue paramter in seaborn denotes which column decides the colour, in this case the Species
    sns.pairplot(ifds,hue='Species')
    plt.savefig("Iris-dataset-pairplot.png")
    plt.show()


# https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset

# function for plotting a scatterplot for sepal length and width
def sepal_length_width_scat():
    plt.figure(figsize = (9,9))
    # using the hue paramter in seaborn denotes which column decides the colour, in this case the Species
    sns.scatterplot(x = "SepalLengthCm", y = "SepalWidthCm", data = ifds, marker = "o", 
                    hue = "Species", palette = ["blue","orange","green"], edgecolor = "dimgrey")
    plt.title("Sepal length and Sepal width comparison", size = 20)
    plt.xlabel("Sepal length", size = 16)
    plt.ylabel("Sepal width", size = 16)
    plt.legend()
    plt.savefig("Sepal-length-width.png")
    plt.show()

# function for plotting a scatterplot for petal length and width
def petal_length_width_scat():
    plt.figure(figsize = (9,9))
    # using the hue paramter in seaborn denotes which column decides the colour, in this case the Species
    sns.scatterplot(x = "PetalLengthCm", y = "PetalWidthCm", data = ifds, marker = "o", 
                    hue = "Species", palette = ["blue","orange","green"], edgecolor = "dimgrey")
    plt.title("Petal length and Petal width comparison", size = 20)
    plt.xlabel("Petal length", size = 16)
    plt.ylabel("Petal width", size = 16)
    plt.legend()
    plt.savefig("Petal-length-width.png")
    plt.show()

def scatterplots():
    sepal_length_width_scat()
    petal_length_width_scat()

# https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/
# https://www.python-graph-gallery.com/30-basic-boxplot-with-seaborn?utm_content=cmp-true
def boxplots():
    sns.set(style="ticks", palette="pastel")
    f, axes = plt.subplots(2, 2, sharey=False, figsize=(12, 8))
    f, axes = plt.subplots(2, 2, sharey=False, figsize=(12, 8))
    sns.boxplot(x="Species", y="PetalLengthCm",data=ifds, ax = axes[0,0])
    sns.boxplot(x="Species", y="SepalLengthCm", data=ifds, ax=axes[0,1])
    sns.boxplot(x="Species", y="PetalWidthCm", data=ifds, ax=axes[1,0])
    sns.boxplot(x="Species", y="SepalWidthCm", data=ifds, ax=axes[1,1])
    # adding a title to the plot
    f.suptitle("Boxplot of the Petal and Sepal measurements by Iris Species")
    plt.savefig("Boxplots.png")
    plt.show()

summary_output()

histograms()
scatterplots()
pairplot()  
boxplots() 
