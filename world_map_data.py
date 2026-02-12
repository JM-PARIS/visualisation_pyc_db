#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 14:34:11 2025

@author: jmp
"""
#%%
import numpy as np
import geopandas
import pandas as pd
import matplotlib.pyplot as plt
import geodatasets
import cmcrameri.cm as cmc


import mpl_scatter_density # adds projection='scatter_density'
from matplotlib.colors import LinearSegmentedColormap


#import fichier
df = pd.read_csv("all_coordinates.csv") #_new
df.head()

#drop NA
df.isnull().sum()
df = df.dropna()
df.info()

# Getting world map data from geo pandas
worldmap  = geopandas.read_file(geodatasets.get_path("naturalearth.land"))

#%%

# Creating axes and plotting world map
fig, ax = plt.subplots(figsize=(32, 20))
worldmap.plot(color="lightgrey", ax=ax)


# Plotting tourist source markets
x = df['long3']
y = df['lat3']
z = df['PyC100']
p = plt.scatter(x, y, 
               c=z,
               cmap=cmc.lajolla_r,
               edgecolors = 'black'
            )
plt.colorbar(label='% PyC/SOC')



# Creating axis limits and title
plt.xlim([-180, 180])
plt.ylim([-90, 90])

plt.title("Data available where")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()


# %%
from scipy.stats import gaussian_kde

x = np.array(df['long3'])
y = np.array(df['lat3'])

xy = np.vstack([x,y])
z = gaussian_kde(xy)(xy)


idx = z.argsort()
x, y, z = x[idx], y[idx], z[idx]

fig, ax = plt.subplots()
ax.scatter(x, y, c=z, s=100)
plt.show()



# %%
fig, ax = plt.subplots(figsize=(16, 10))
worldmap.plot(color="lightgrey", ax=ax)
plt.xlim([-180, 180])
plt.ylim([-90, 90])
sc = ax.scatter(x, y, c=z, s=10)
plt.colorbar(sc, label='Number of points per pixel',ax=ax)

plt.title("Data available where")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()



# %%

