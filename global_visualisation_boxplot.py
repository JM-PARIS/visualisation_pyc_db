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
def daplot_boxplot(var_num, var_class, df = df):
    unit_description = df.loc[[0]]
    units = df.loc[[1]]

    df= df.drop([0, 1])

    df[var_num] = pd.to_numeric(df[var_num])

    sns.boxplot(data=df, x = var_num, y = var_class, color = "#CC79A7")

    # plt.xticks(rotation=90)
    plt.xlabel(unit_description[var_num].values[0])
    # plt.legend()

    return()

daplot_boxplot("SOC2","soil3")
# %%
