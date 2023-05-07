# Programming and scripting project 2023

This repository is used for the final project given during the Programming and Scripting module on Higher Diploma in Data Analytics course from ATU. Topic of the project is research and investigation of IFisher's iris dataset.

## Table of contents
* [Iris dataset information](#iris-dataset)
    * [Iris dataset history](#iris-dataset-history)
    * [Iris dataset file](#iris-dataset-file)
* [Dataset code and analysis](#dataset-code-and-analysis)

    * [Imported libraries and modules](#imported-libraries-and-modules)
    * [Dataset import](#dataset-import)

* [Plots](#plots)

* [Summary and Conclusions](#conclusions)
* [Technologies](#technologies)

* [References](#references)

# **Iris dataset**

## **Iris dataset history**

Iris flower data, also known as Fisher's Iris dataset was introduced by British biologist and statistitian Sir Ronald Aylmer Fisher. In 1936, Sir Fisher published a report titled [“The Use of Multiple Measurements in Taxonomic Problems”](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x) in the journal Annals of Eugenics. In this article, Fisher developed and evaluated a linear function to differentiate Iris species based on the morphology of their flowers. It was the first time that the sepal and petal measures of the three Iris species as mentioned above appeared publicly.\
It is a multivariate data set of 50 samples which the author gathered on each of three species of Irises: setosa, versicolor and virginica. Measurements of 4 properties of 50 flowers of each of the plants were taken, namely Sepal length, Sepal width, Petal Length, and Petal width. The author suggests that the petal and sepal lengths and widths are characteristics whcih can be used to identify which species they belong to based on a linear discriminant model. Fischer himself developed the linear discriminant model,a statistical, machine learning and pattern recognition technique used to distinguish between two or more objects, classes or events. Ref [Linear discriminant analysis] [https://en.wikipedia.org/wiki/Linear_discriminant_analysis]Ref [Iris Data set wikipedia] [https://en.wikipedia.org/wiki/Iris_flower_data_set] Fischer presented the data for the 3 species in a table with each of the four measurements and subsequently, tables of observed means, sums of squares etc in order to demonstrate how each species can be discriminated from one another. 


## **Iris dataset file**

This Iris dataset contains a set of 150 records which represent three iris species (*Iris setosa*, *Iris versicolor* and *Iris virginica*) with 50 samples each. 

The columns that represent records mentioned above are :

* Id
* SepalLengthCm
* SepalWidthCm
* PetalLengthCm
* PetalWidthCm
* Species


Iris dataset used in this analysis can be found among files in this repository as [Iris_dataset.csv](https://github.com/lgrealish/pands-project/blob/main/iris.csv).

# **Dataset code and analysis**

## **Dataset import**
```python
    ifds = pd.read_csv("iris.csv", index_col = "Id")
```
This line of code is used for reading the .csv file into DataFrame and storing it as a variable *ifds* (iris flower dataset) for further analysis and manipulation.\
Since *pandas* is using zero-based integer indices in the DataFrame,  *index_col = "Id"* was used to make the Id column an index column while reading the file. That means that the index column will not be taken into consideration while analysing the data.

The data was downloaded from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data as a . data file which I then converted to .csv.

## **Imported libraries**

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys
...

# **Technologies used** #

====

  * Visual Studio Code - version 1.77.1
  * Cmder - version 221218