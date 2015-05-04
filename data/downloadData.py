#!/usr/bin/python
# coding: utf-8
# filename: downloadData.py

import os

for i in range(1901, 2016):
    os.system('wget -r -np -nH --cut-dirs=3 -R index.html ftp://ftp.ncdc.noaa.gov/pub/data/gsod/${i}/')

