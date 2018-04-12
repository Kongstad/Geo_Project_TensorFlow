#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:16:53 2018

@author: peterkongstad
"""

import rasterio

dataset=rasterio.open('sentinel2images/S2A_MSIL1C_20170605T141011_N0205_R053_T26WNE_20170605T141006.SAFE/GRANULE/L1C_T26WNE_A010203_20170605T141006/IMG_DATA/T26WNE_20170605T141011_TCI.jp2')