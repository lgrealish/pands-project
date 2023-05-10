# Programming and scripting project 2023

This repository is used for the final project given during the Programming and Scripting module on Higher Diploma in Data Analytics course from ATU. Topic of the project is research and investigation of Fisher's Iris dataset.

## Table of contents
* [Iris dataset information](#iris-dataset)
    * [Iris dataset history](#iris-dataset-history)
    * [Iris dataset file](#iris-dataset-file)
* [Dataset code and summary output](#dataset-code-and-output-summary)
    * [Dataset import](#dataset-import)
    * [Imported libraries and modules](#imported-libraries-and-modules)
    * [Dataset output summary](#datasetsummary)
* [Plots](#plots)
    * [Histograms](#histograms)
    * [Pairplot](#pairplot)
    * [Scatterplots](#scatterplots)   
    * [Boxplots](#boxplots)
* [Summary and Conclusions](#summary-and-conclusions)
* [Technologies](#technologies)
* [References](#references)

# **Iris dataset**

## **Iris dataset history**

Iris flower data, also known as Fisher's Iris dataset was introduced by British biologist and statistician Sir Ronald Aylmer Fisher. In 1936, Sir Fisher published a report titled [“The Use of Multiple Measurements in Taxonomic Problems”](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x) in the journal Annals of Eugenics. In this article, Fisher developed and evaluated a linear function to differentiate Iris species based on the morphology of their flowers. It was the first time that the sepal and petal measures of the three Iris species as mentioned above appeared publicly.

It is a multivariate data set of 50 samples which the author gathered on each of three species of Irises: setosa, versicolor and virginica. Measurements of 4 properties of 50 flowers of each of the plants were taken, namely Sepal length, Sepal width, Petal Length, and Petal width. The author suggests that the petal and sepal lengths and widths are characteristics which can be used to identify which species they belong to based on a linear discriminant model[Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis). Fisher himself developed the linear discriminant model, a statistical, machine learning and pattern recognition technique used to distinguish between two or more objects, classes or events.  [Iris Data set wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set) Fisher presented the data for the 3 species in a table with each of the four measurements and subsequently, tables of observed means, sums of squares etc. in order to demonstrate how each species can be discriminated from one another. 

<img src = https://github.com/lgrealish/pands-project/blob/main/iris-species-image.png alt= "Iris flower species">

## **Iris dataset file**

This Iris dataset contains a set of 150 records which represent three iris species (*Iris setosa*, *Iris versicolor* and *Iris virginica*) with 50 samples each. 

The columns that represent records mentioned above are:

* Id
* SepalLengthCm
* SepalWidthCm
* PetalLengthCm
* PetalWidthCm
* Species


Iris dataset used in this analysis can be found among files in this repository as [iris.csv](https://github.com/lgrealish/pands-project/blob/main/iris.csv).


# **Dataset code and output summary**

## **Dataset import**

```python
    ifds = pd.read_csv("iris.csv", index_col = "Id")
```
This line of code is used for reading the .csv file into a *pandas* DataFrame and storing it as a variable *ifds* (iris flower dataset) for further analysis and manipulation.

Since *pandas* is using zero-based integer indices in the DataFrame,  *index_col = "Id"* was used to make the Id column an index column while reading the file. That means that the index column will not be taken into consideration while analysing the data. [realpython](https://realpython.com/python-csv/)

The data was downloaded from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data as a .data file which I then converted to .csv.

Alternatively, the data could be read in directly from a url, and the code for this can be seen in the analysis.py file.  In order to avoid any potential issues with connectivity I decided not to use this method.

## **Imported libraries and modules**

```python
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    import sys
```
***NumPy*** is a Python library that provides a  multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more. [numpy](https://numpy.org/devdocs/user/whatisnumpy.html)

***Matplotlib*** is a comprehensive visualisation library in Python, built on NumPy arrays, for creating static, animated and interactive 2D plots or arrays. [matplotlib] (https://matplotlib.org/)\
*matplotlib.pyplot* is a state-based interface to *matplotlib*. It provides a MATLAB-like way of plotting. *pyplot* is mainly intended for interactive plots and simple cases of programmatic plot generation. [matplotlib](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)

***Seaborn*** is a library for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures. [seaborn](https://seaborn.pydata.org/index.html)

***Pandas*** The Pandas library is a useful package for importing labelled data such as the iris data set. It makes data such as csv files much easier to work with.

***sys*** module represents system-specific parameters and functions and provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

## **Dataset output summary**

As instructed in the project scope, the summary of the variables in the dataset are saved in a single text file and do not show upon running the code in analysis.py. [output_summary_variable.txt](https://github.com/lgrealish/pands-project/blob/main/output_summary_variable.txt)

The defined function *summary_output()* contains the code for creating the dataset summary and writing it to a single .txt file.  This was achieved using the sys.stdout module. [geeksforgeeks](https://www.geeksforgeeks.org/sys-stdout-write-in-python/) [programcreek](https://www.programcreek.com/python/example/11/sys.stdout)

From the output summary text file, we can see the following details of the data set:

- There are 150 rows and 5 columns in the DataFrame.
- There are 50 observations for each species class.
- There are no null values in any of the columns, SepalLengthCm. SepalWidthCm, PetalLengthCm, PetalWidthCm or Species.

This output from the *describe()* function shows the count, mean, standard deviation and percentiles for each of the 4 variables, sepal length, sepal width, petal length and petal width.

<details>
           <summary>Output</summary>
           <p>

           SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
    count     150.000000    150.000000     150.000000    150.000000
    mean        5.843333      3.054000       3.758667      1.198667
    std         0.828066      0.433594       1.764420      0.763161
    min         4.300000      2.000000       1.000000      0.100000
    25%         5.100000      2.800000       1.600000      0.300000
    50%         5.800000      3.000000       4.350000      1.300000
    75%         6.400000      3.300000       5.100000      1.800000
    max         7.900000      4.400000       6.900000      2.500000

</p>
</details>    

- Sepal length has the highest mean while petal width has the lowest mean.
- The standard deviation in the petal lengths shows the highest variability of the four measurements at 1.76 while the standard deviations of the petal width is approx. 0.43cm.
- The shortest petal in the data set is 1cm with the longest measuring 6.9cm.
- The sepal length has a larger mean than the other 3 variables.


This output from the *groupby()* function shows mean and median sepal length, sepal width, petal length and petal width by species. [tutorialspoint](https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset)

``` python
        print (ifds.groupby("Species").describe().T)
```
<details>
           <summary>Output</summary>
           <p>

                            SepalLengthCm        SepalWidthCm        PetalLengthCm        PetalWidthCm       
                            mean median         mean median          mean median         mean median
    Species                                                                                          
    Iris-setosa             5.006    5.0        3.418    3.4         1.464   1.50        0.244    0.2
    Iris-versicolor         5.936    5.9        2.770    2.8         4.260   4.35        1.326    1.3
    Iris-virginica          6.588    6.5        2.974    3.0         5.552   5.55        2.026    2.0

</p>
</details>    

# **Plots**

In this section I will look at the plots that I produced to visualise and summarise the dataset.

## **Histograms**

A histogram is a representation of the distribution of data.  The histograms below show the distribution of each of the measurement variables by species across the dataset.

To create the histograms firstly I defined 4 separate functions, 1 for each of the variables (SepalLengthCm. SepalWidthCm, PetalLengthCm, PetalWidthCm).  These were then grouped in a function called *histograms()*.

The variables *iris_s*, *iris_vers* and *iris_virg* are used to subset original DataFrames for Iris setosa, Iris versicolor and Iris virginica, respectively. They are outside the histogram functions to allow for multiple use, if necessary. [cmdlinetips](https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/)

Various other parameters were included in order to make the plots more aesthetically pleasing.  These include size definition of the title, labels text as well the colour choice. [stackoverflow](https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib) [medium](https://medium.com/swlh/how-to-create-a-seaborn-palette-that-highlights-maximum-value-f614aecd706b)

<img src = "https://github.com/lgrealish/pands-project/blob/main/Sepal-length.png" alt = "Sepal length" width = "450" height = "450"><img src = "https://github.com/lgrealish/pands-project/blob/main/Sepal-width.png" alt = "Sepal length" width = "450" height = "450">

<img src = "https://github.com/lgrealish/pands-project/blob/main/Petal-length.png" alt = "Petal length" width = "450" height = "450"><img src = "https://github.com/lgrealish/pands-project/blob/main/Petal-width.png" alt = "Petal width" width = "450" height = "450">

The histogram for the sepal length shows quite a bit of variation with a number of various peaks while the sepal width is more centred around the 3cm but with smaller peaks either side.  

We can see that the Iris setosa has a petal length and petal width that is much smaller than the those of the other 2 species.  The Iris setosa also has the smallest sepal length but the largest sepal width.

## **Pairplot**

[datagy](https://datagy.io/seaborn-pairplot/)
[towardsdatascience](https://towardsdatascience.com/seaborn-pairplot-enhance-your-data-understanding-with-a-single-plot-bf2f44524b22#:~:text=The%20Seaborn%20Pairplot%20allows%20us,to%20become%20familiar%20with%20it.)

Using the *pairplot()* function from the *seaborn* library we can produce the following pairplot which displays all pairwise relationships between variables within a dataset.  It creates a nice visualisation which summarises a large amount of data in a single figure.  Pairplots give a good comparison and observation of the data and provides enough information to draw conclusions.

Because there are 4 different variables in our data set (SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm) a 4x4 plot is created.

<img src = "https://github.com/lgrealish/pands-project/blob/main/Iris-dataset-pairplot.png" alt = "Sepal length, width and Petal length, width " width = "450" height = "450">

The pairplot shows that the Iris setosa is clearly different to the other 2 species.  We can also see that is more difficult to differentiate the other 2 species from one another as there is more overlap in the data points.

## **Scatterplots**

Scatterplots shows how the different variables in the dataset correlate with one another.  One variable is plotted on the x-axis with the other plotted on the y-axis.  The scatterplots below show the relationship between sepal measurements and petal measurements.

Just like the histogram code, each scatterplot was defined in a separate function before being grouped in a *scatterplot()* function. [tutorialspoint](https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset)

<img src = "https://github.com/lgrealish/pands-project/blob/main/Sepal-length-width.png" alt = "Sepal length and Sepal width" width = "450" height = "450"><img src = "https://github.com/lgrealish/pands-project/blob/main/Petal-length-width.png" alt = "Petal length and Petal width" width = "450" height = "450">

From the Sepal length and Sepal width scatterplot it is easier to distinguish Iris setosa than Iris versicolor and Iris virginica. Iris setosa has wider and shorter sepals, while the other species are not easy to differentiate based on this data.  It also shows some negative correlation, those flowers with the smaller sepal widths tend to have longer lengths.

From the Petal length and Petal width scatterplot the difference between the three species is much more noticeable. Iris setosa is very distinct and has the smallest and narrowest petals of the three. Iris virginica has the biggest petals.

We can also see that there is a correlation between petal length and width, the flowers that have the smallest petal length also have the smallest petal width.

## **Boxplots**

Boxplots were generated using the *seaborn* module and are very useful for showing various statistics in one plot, including minimum, quartiles, median and maximum.  As well as showing the distribution of values within each species class they also allow for comparisons across the 3 species.  The x-axis denotes the data to be plotted while the y-axis shows the frequency of distribution.

[geeksforgeeks](https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/)
[pythongraphygallery](https://www.python-graph-gallery.com/30-basic-boxplot-with-seaborn?utm_content=cmp-true)

<img src = "https://github.com/lgrealish/pands-project/blob/main/Boxplots.png" alt = "Sepal and Petal observations by species" width = "450" height = "450">

The boxplots above show that the Iris setosa stands out as having a much smaller petal size (both length and width).

# **Summary and Conclusions**

For this project I used the *pandas*, *numpy*, *matplotlib* and *seaborn* libraries modules and *sys* module.  I examined the statistical properties of the Fisher Iris data set and used the aforementioned libraries and module to visualise the data, giving us a better understanding of the data.  As the old saying goes, a picture paints a thousand words!

The Iris data set is quite a small data set with a sample size of only 150 with its observations divided evenly into 3 species classes.  This makes me believe that it was not a random sample selection.

The average petal length of the Iris setosa is much smaller than the other 2 species.  The Iris virginica has the largest average petal length measuring almost 4 times more than that of the Iris setosa.  There is little difference between the average petal length of the Iris virginica and Iris versicolor.

The average petal width of the Iris setosa is also significantly smaller than that of the other two species.  

The standard deviation across the species show that Iris setosa is much less variable that either of the other 2.

The differences in average sepal length across the species varies much less but the Iris setosa still has the smallest of the three.

The only measurements that the Iris setosa has the highest average for is the sepal width.

If compared by sepal width and length, Iris versicolor and Iris virginica would not be easily distinguishable.

Looking at all of the statistics of both sepal and petal measurements generated in the output summary code as well as the plots it appears differences between the Iris setosa and the other two species is more pronounced than any other differences between the three classes. 

# **Technologies**

  * Visual Studio Code - version 1.78.1
  * Cmder - version 221218 [64]

# **References**

  https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x
  https://en.wikipedia.org/wiki/Linear_discriminant_analysis
  https://en.wikipedia.org/wiki/Iris_flower_data_set
  https://realpython.com/python-csv/
  https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
  https://www.youtube.com/watch?v=02BFXhPQWHQ
  https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
  https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6
  https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.describe.html
  https://note.nkmk.me/en/python-pandas-t-transpose/#:~:text=Use%20the%20T%20attribute%20or,columns%20swapped%20(%3D%20transposed%20object)
  https://realpython.com/pandas-groupby/#pandas-groupby-putting-it-all-together
  https://www.geeksforgeeks.org/pandas-groupby-and-computing-median/
  https://datascienceparichay.com/article/pandas-groupby-median/
  https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
  https://numpy.org/devdocs/user/whatisnumpy.html
  https://matplotlib.org/)%5C
  https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
  https://seaborn.pydata.org/index.html
  https://www.geeksforgeeks.org/sys-stdout-write-in-python/
  https://www.programcreek.com/python/example/11/sys.stdout
  https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset
  https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/
  https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
  https://medium.com/swlh/how-to-create-a-seaborn-palette-that-highlights-maximum-value-f614aecd706b
  https://datagy.io/seaborn-pairplot/
  https://towardsdatascience.com/seaborn-pairplot-enhance-your-data-understanding-with-a-single-plot-bf2f44524b22#:~:text=The%20Seaborn%20Pairplot%20allows%20us,to%20become%20familiar%20with%20it
  https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/
  https://www.python-graph-gallery.com/30-basic-boxplot-with-seaborn?utm_content=cmp-true
  https://stackoverflow.com/questions/24383700/resize-image-in-the-wiki-of-github-using-markdown
  https://stackoverflow.com/questions/24319505/how-can-one-display-images-side-by-side-in-a-github-readme-md
  https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#headers




