# Airlines Delay [![Awesome](https://awesome.re/badge.svg)](https://github.com/kfrawee/SalesAnalysis) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
### Airline on-time statistics and delay causes
#### by Muhammad Elkfrawy - <i> Dec 2020 </i>



## Introduction
Data visualization is an important skill that is used in many parts of the data analysis process. 

**Exploratory** data visualization generally occurs during and after the data wrangling process, and is the main method that you will use to understand the patterns and relationships present in your data. This understanding will help you approach any statistical analyses and will help you build conclusions and findings. This process might also illuminate additional data cleaning tasks to be performed. 

**Explanatory** data visualization techniques are used after generating your findings, and are used to help communicate your results to others. Understanding design considerations will make sure that your message is clear and effective. In addition to being a good producer of visualizations, going through this project will also help you be a good consumer of visualizations that are presented to you by others.


## Overview
This project has two parts that demonstrate the importance and value of data visualization techniques in the data analysis process. In the first part, I will use Python visualization libraries to systematically explore a selected dataset, starting from plots of single variables and building up to plots of multiple variables. 

In the second part, I will produce a short presentation that illustrates interesting properties, trends, and relationships that you discovered in your selected dataset. 

The primary method of conveying your findings will be through transforming your exploratory visualizations from the first part into polished, explanatory visualizations.



## Dataset :bookmark_tabs:

> The U.S. Department of Transportation's (DOT) [Bureau of Transportation Statistics](https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp) (BTS) tracks the on-time performance of domestic flights operated by large air carriers. Summary information on the number of on-time, delayed, canceled, and diverted flights appear in DOT's monthly [Air Travel Consumer Report](http://www.dot.gov/individuals/air-consumer/air-travel-consumer-reports), published about 30 days after the month's end, as well as in summary tables posted on this website. BTS began collecting details on the causes of flight delays in June 2003. Summary statistics and raw data are made available to the public at the time the Air Travel Consumer Report is released.

**This version of the dataset was compiled from the Statistical Computing Statistical Graphics 2009 Data Expo and is also [available here](http://stat-computing.org/dataexpo/2009/the-data.html) or [here](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HG7NV7).**

There are arround 2.4 million records in the dataset with 29 features [listed here](http://stat-computing.org/dataexpo/2009/the-data.html)  with description.

Before we started the analysis, We checked the numerical columns for missing values and imputed them using the linear interpolate function.


## Summary of Findings :notebook_with_decorative_cover:

I was intersted in finding out about:
- What are the factors effecting the flights cancellation?
- When do airline cancellations happen?
- Are cancellations related to delays?
- Is there any other interesting patterns?

After investigating and plotting the correlation matrix between the variables, we deduced That:

- Most of the flights not diverted (only 0.24%).
- The most cancellation flights were due to the carrier and weather reasons.
Northwest Airlines Inc. followed by American Airlines Inc. has the most delayed flights and American Airlines Inc. has the most canceled ones.
- We have found a negative correlation between the distance and the arrival delay, in which we observed that the shortest flights in distance are the most delayed on arrival.
- The best tome to book your flight is in early hours of the morning as they have the least delays over the hours of the day.


## Key Insights for Presentation :high_brightness:
For the presentation, I started with univariate distribution plots of numerical and categorical variables, using histograms and box plots for numericals variables, pie charts and bar charts for categorical variables.

Afterwards, Bivariate exploration by investigating the relationships between each pairs of variables with heatmap, scatter plots and clustered bar charts.

Finally, Multivariate exploration by creating plots of three or more variables to investigate the data even further, I was intersted only in
the relationship between dep. delay and arr. delay for each unique carrier.
