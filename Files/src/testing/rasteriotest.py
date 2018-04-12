
"""
Created on Thu Apr 12 16:16:53 2018

@author: peterkongstad
"""

import rasterio

#Rasterio opens the file into a DATASET
dataset=rasterio.open('sentinel2images/S2A_MSIL1C_20170605T141011_N0205_R053_T26WNE_20170605T141006.SAFE/GRANULE/L1C_T26WNE_A010203_20170605T141006/IMG_DATA/T26WNE_20170605T141011_TCI.jp2')

#Saves the boundaries of the map.
boundaries=dataset.bounds

#Defines the coordinate reference system used in the image.
referencesystem=dataset.crs

#Shows how many bands are in the image
bands=dataset.indexes

#Define the three bands of the image
band1=dataset.read(1)
band2=dataset.read(2)
band3=dataset.read(3)

#Shows format information in greater details
referencesystem2=dataset.crs.wkt

#%% Showing imported image
import rasterio
from matplotlib import pyplot
from rasterio.plot import show
#Shows the entire 3 bands in the image.
show(dataset)

#Creating 3 figures with the 3 bands in the image
fig, (axr, axg, axb) = pyplot.subplots(1,3, figsize=(21,7))
show((dataset, 1), ax=axr, cmap='Reds', title='red channel')
show((dataset, 2), ax=axg, cmap='Greens', title='green channel')
show((dataset, 3), ax=axb, cmap='Blues', title='blue channel')
pyplot.show()

