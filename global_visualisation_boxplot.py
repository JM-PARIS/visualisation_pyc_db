#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@FILE :Untitled-1
@Description :
@ :2026/02/04 16:13:03
@Author : JM PARIS
'''

###LIBRARIES
###
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from scipy.stats import gaussian_kde
import math as math
import seaborn as sns


#import fichier
df = pd.read_csv("20250201_PyC_database_version3_4.csv")

##boxplot
def daplot_boxplot(a, df = df):
    #separate unit description from data
    unit_description = df.loc[[0]]
    units = df.loc[[1]]

    df= df.drop([0, 1])
    sns.histplot(data=df, x=a, shrink=.8, color = "#CC79A7",
                 bins = 50, edgecolor = "#CC79A7", alpha = 0.6,
                 label = "with big papers")

    df=df.drop(df[df["id"]=="122"].index)
    df=df.drop(df[df["id"]==122].index)
    df=df.drop(df[df["id"]=="95"].index)
    
    sns.histplot(data=df, x=a, shrink=.8, color = "#56B4E9",
                  bins = 50, label = "without big papers",
                  edgecolor = "#0072B2", alpha = 0.6)


    plt.xticks(rotation=90)
    plt.xlabel(unit_description[a].values[0])
    plt.legend()

    return()

daplot_discrete("FRI2")
# %%
