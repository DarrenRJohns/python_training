# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#print('hello world')


# Import the seaborn package
import seaborn as sns

# load the titanic example dataset and save it as a dataframe named titanic
titanic = sns.load_dataset('titanic')

# look at the first 5 rows of the dataframe
titanic.head()