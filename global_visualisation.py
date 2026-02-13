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
from sklearn.linear_model import LinearRegression

#import fichier
df = pd.read_csv("20250201_PyC_database_version3_4.csv")


#separate unit description from data
unit_description = df.loc[[0]]
units = df.loc[[1]]

df= df.drop([0, 1])

#drop big papers
big_papers = False

if not big_papers:
    df=df.drop(df[df["id"]=="122"].index)
    df=df.drop(df[df["id"]==122].index)
    df=df.drop(df[df["id"]=="95"].index)


##PRESENTATION ONE VARIABLE

def daplot(a):
    
    tab_a = []

    for k in range(len(df[a])):
        try :
            tab_a += [float(df[a].values[k])]
        except ValueError:
            pass

    plt.hist(tab_a)

    #plt.text(all_min, all_max, "nbr pts: " +str(len(tab_a)))
    plt.show()
    return()



##EXTRACTED CORRELATION
# %%
def correl_plot(a,b):
    tab_a = []
    tab_b = []
    tab = []

    for k in range(len(df[a])):
        try :
            tab += [[float(df[a].values[k]),float(df[b].values[k])]]
        except ValueError:
            pass
    
    tab_a = np.array(tab)[:,0]
    tab_b = np.array(tab)[:,1]


    all_lat = df['lat3'].values[:]
    all_long = df['long3'].values[:]

    #lin reg
    x=[]
    y=[]

    print(len(tab_a),len(tab_b))

    coor_non_nan = []
    #removing nan values before linear regression
    for k in range(len(tab_a)):
        if [all_lat[k],all_long[k]] not in coor_non_nan: #to remove doubles of coordinates
            if not( np.isnan(tab_a[k]) or np.isnan(tab_b[k])):
                x += [tab_a[k]]
                y += [tab_b[k]]
                coor_non_nan += [[all_lat[k],all_long[k]]]


    #linear regression
    x = np.array(x).reshape(-1, 1)
    y = np.array(y)

    model = LinearRegression().fit(x, y)

    r_sq = model.score(x, y)
    print(f"coefficient of determination: {r_sq}")
    print(f"intercept: {model.intercept_}")
    print(f"slope: {model.coef_}")


    #plot

    x = x.reshape(-1,1)

    all_min = np.nanmin([np.nanmin(x),np.nanmin(y)])
    all_max = np.nanmax([np.nanmax(x),np.nanmax(y)])

    x_lin = np.linspace(all_min,all_max,2)
    y_lin = [model.intercept_ + k * model.coef_ for k in x_lin]

    plt.scatter(x,y, alpha = 0.05)
    plt.plot(x_lin, y_lin, color = 'red')
    plt.plot(x_lin,x_lin, color= "grey" )
    plt.xlabel(unit_description[a].values[0])
    plt.ylabel(unit_description[b].values[0])
    plt.title(a+' VS '+b)
    plt.xlim([all_min - 0.1*(all_max-all_min), all_max + 0.1*(all_max-all_min)])
    plt.ylim([all_min - 0.1*(all_max-all_min), all_max + 0.1*(all_max-all_min)])

    plt.gca().set_aspect(1)

    plt.text(all_min, all_max, "nbr pts: " +str(len(x)))
    plt.show()
    return()#x,y,coor_non_nan)

# %%

correl_plot("BD1","BD3")
correl_plot("MAP2","MAP3")
correl_plot("MAT2","MAT3")
correl_plot("alt2","alt3")
correl_plot("pH1","pH3")
correl_plot("clay1","clay3")
correl_plot("SOC2","SOC4")


# %%

##plot depth

soil_categ = ['forest floor', 'topsoil', 'intermediate', 'subsoil',"nan"]
colors = ['black','#E69F00','#56B4E9','#CC79A7','grey']

#create a dictionnary for colors
dic_color = {}
for k in range(len(soil_categ)):
    dic_color[soil_categ[k]] = colors[k]


def correl_plot_depth(a,b):
    tab_a = []
    tab_b = []
    tab_dp = []
    tab_lat = []
    tab_long = []

    depth_categ = []    #colors

    x=[]     #lin reg
    y=[]
    
    coor_non_nan = [] #for coordinates replicate

    #convert eventual string into floats
    for k in range(len(df[a])):
        try :
            tab_a += [float(df[a].values[k])]
            tab_b += [float(df[b].values[k])]
            tab_dp += [df["depth3"].values[k]]
            tab_lat += [df["lat3"].values[k]]
            tab_long += [df["long3"].values[k]]
        except ValueError:
            pass


    #removing nan values before linear regression
    for k in range(len(tab_a)):
        #to remove doubles of coordinates
        if [tab_lat[k],tab_long[k]] not in coor_non_nan:
            #if both values are different from nan
            if not( np.isnan(tab_a[k]) or np.isnan(tab_b[k])):
                x += [tab_a[k]]
                y += [tab_b[k]]
                depth_categ += [str(tab_dp[k])]
                coor_non_nan += [[tab_lat[k],tab_long[k]]]

    #linear regression
    x = np.array(x).reshape(-1, 1)
    y = np.array(y)

    model = LinearRegression().fit(x, y)

    r_sq = model.score(x, y)
    print(f"coefficient of determination: {r_sq}")
    print(f"intercept: {model.intercept_}")
    print(f"slope: {model.coef_}")


    #PLOT

    #reshape for plotting
    x = x.reshape(-1,1)
    
    #prepare min and max for axis limit
    all_min = np.nanmin([np.nanmin(x),np.nanmin(y)])
    all_max = np.nanmax([np.nanmax(x),np.nanmax(y)])

    #prepare linear regression plotting
    x_lin = np.linspace(all_min,all_max,2)
    y_lin = [model.intercept_ + k * model.coef_ for k in x_lin]

    #separation of categories of soil depth for scatter plotting
    split_x=[[] for k in range(len(soil_categ))]
    split_y=[[] for k in range(len(soil_categ))]
    print(soil_categ)

    for k in range(len(x)):
        which_col = soil_categ.index(depth_categ[k])
        split_x[which_col] += [x[k]]
        split_y[which_col] += [y[k]]

    print([len(r) for r in split_x])

    #sort list
    split_len = [len(l) for l in split_x]

    split_categ = [x for _,x in sorted(zip(split_len,soil_categ))]
    split_colors = [x for _,x in sorted(zip(split_len,colors))]

    split_x = sorted(split_x, key=len)
    split_y = sorted(split_y, key=len)

    #reverse for beautiful plot
    split_x = split_x[::-1]
    split_y = split_y[::-1]
    split_categ = split_categ[::-1]
    split_colors = split_colors[::-1]

    fig, ax = plt.subplots()
    
    for s in range(len(split_x)):
        ax.scatter(split_x[s],split_y[s], alpha = 0.1,
                   label = split_categ[s]+ " "+ str(len(split_x[s])), color= split_colors[s])


    plt.plot(x_lin, y_lin, color = 'red')
    plt.plot(x_lin,x_lin, color= "grey" )
    plt.xlabel(unit_description[a].values[0])
    plt.ylabel(unit_description[b].values[0])
    plt.title(a+' VS '+b)
    plt.xlim([all_min - 0.1*(all_max-all_min), all_max + 0.1*(all_max-all_min)])
    plt.ylim([all_min - 0.1*(all_max-all_min), all_max + 0.1*(all_max-all_min)])

    plt.gca().set_aspect(1)

    plt.text(all_min, all_max, "nbr pts: " +str(len(x)))
    leg = plt.legend()    
    for lh in leg.legend_handles: 
        lh.set_alpha(1)
    plt.show()
    return()#x,y,coor_non_nan)

correl_plot_depth("MAP2","MAP3")
correl_plot_depth("MAT2","MAT3")
correl_plot_depth("alt2","alt3")
correl_plot_depth("pH1","pH3")
correl_plot_depth("clay1","clay3")
correl_plot_depth("SOC2","SOC4")
correl_plot_depth("BD1","BD3")

# %%



