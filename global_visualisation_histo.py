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
 

#import fichier
df = pd.read_csv("20250201_PyC_database_version3_4.csv")

##HISTOGRAM

def daplot(a, df):
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



    kde_a = gaussian_kde(tab_a)
    kde_b = gaussian_kde(tab_b)

    xmin = min(min(tab_a), min(tab_b))
    xmax = max(max(tab_a), max(tab_b))

    bins = np.linspace(xmin, xmax, 50)
    xs = np.linspace(xmin, xmax, 400)

    #PLOT

    _, bins, _ = plt.hist(tab_b, density = True, alpha = 0.9, bins=50,
                           color = "#0072B2", label = "without big papers")
    plt.plot(xs, kde_b(xs),color = "#0072B2")

    # _ = plt.hist(tab_a, bins=bins, density=True, alpha=0.5,
    #              color = "#CC79A7", label = "with big papers")

    # plt.plot(xs, kde_a(xs),color = "#CC79A7")


    plt.xlabel(unit_description[a].values[0])
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.legend()

    plt.show()
    return()

#%%
daplot("MAP3", df)
# daplot("MAT3", df)
# daplot("SOC4", df)
# daplot("MAP1", df)
# %%
