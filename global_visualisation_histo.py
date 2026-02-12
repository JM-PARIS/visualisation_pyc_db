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

##HISTOGRAM

def daplot(a, df = df):
    #separate unit description from data
    unit_description = df.loc[[0]]
    units = df.loc[[1]]

    df= df.drop([0, 1])


    #prepare

    tab_a = [] #all values
    tab_b = [] #no big papers


    for k in range(len(df[a])):
        try :
            if not math.isnan(float(df[a].values[k])): #don't take nan
                tab_a += [float(df[a].values[k])]
        except ValueError:
            pass

    df=df.drop(df[df["id"]=="122"].index)
    df=df.drop(df[df["id"]==122].index)
    df=df.drop(df[df["id"]=="95"].index)

    for k in range(len(df[a])):
        try :
            if not math.isnan(float(df[a].values[k])): #don't take nan
                tab_b += [float(df[a].values[k])]
        except ValueError:
            pass

    #PLOT

    sns.histplot(tab_b, kde = True, stat = "percent", color = "#0072B2",
                 bins = 50, label = "without big papers ("+str(len(tab_b))+" pts)",
                 edgecolor = "#0072B2")
    sns.histplot(tab_a, kde = True, stat = "percent", color = "#CC79A7",
                 bins = 50, label = "with big papers ("+str(len(tab_a))+" pts)", edgecolor = "#CC79A7")

    plt.xlabel(unit_description[a].values[0])

    plt.legend()
    plt.show()
    return()

#%%
daplot("BD1")
# daplot("MAT3")
# daplot("SOC4")
# daplot("MAP1")
# %%



    sns.histplot(data=tips, x="day", shrink=.8)