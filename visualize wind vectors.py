# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:43:01 2019

@author: Rabia Athar
"""

# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import rcParams
import matplotlib.colors as colors

#read data from file into datframe
df = pd.read_csv('field2.irreg', skiprows=6, sep=" ", names=['X', 'Y', 'Z', 'U', 'V', 'W'])

X=pd.to_numeric(df['X'])
Y=pd.to_numeric(df['Y'])
Z=pd.to_numeric(df['Z'])
U=pd.to_numeric(df['U'])
V=pd.to_numeric(df['V'])
W=pd.to_numeric(df['W'])
speed = np.sqrt(U*U + V*V)


rcParams['figure.figsize'] = (7, 7)
#plot quiver 
#Source: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.quiver.html?highlight=quiver#matplotlib.pyplot.quiver
plot=plt.quiver(X, Y, U, V, speed, width=0.005)
#plot properties
ax = plt.gca()
ax.set_title('Movements of water particles (caused by winds)')
#Source: https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html?highlight=facecolor#matplotlib.axes.Axes.set_facecolor
ax.set_facecolor('xkcd:black')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
#Source:https://matplotlib.org/api/colorbar_api.html?highlight=colorbar#module-matplotlib.colorbar
plt.colorbar(fraction=0.03, pad=0.06)
#save plot as JPEG image
plt.savefig('Rabia Plot.jpg')
plt.show()



