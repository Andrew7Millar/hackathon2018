#!/usr/bin/python
import sys
import numpy as np

def calc_photosynthesis(T, CO2, light):
    return light * CO2 / T

# File passed as command line argument
fname_in = sys.argv[1]
fname_out = sys.argv[2]

# Load columns from tab-delimited table
data = np.loadtxt(fname_in, delimiter='\t')

# Loop over rows calculating photosynthesis
photo = []
for i in range(data.shape[0]):
    T = data[i, 0]
    CO2 = data[i, 1]
    light = data[i, 2]
    iphoto = calc_photosynthesis(T, CO2, light)
    photo.append(iphoto)

# Save data to output file
np.savetxt(fname_out, photo)
