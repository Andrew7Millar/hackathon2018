#!/usr/bin/python
from cis_interface.interface.CisInterface import CisInput, CisOutput

def calc_photosynthesis(T, CO2, light):
    return light * CO2 / T

# Setup input/output channels
channel_in = CisInput('photo_in')
channel_out = CisOutput('photo_out', '%f')

# Loop over input
while True:
    # Input
    flag, idata = channel_in.recv()
    if not flag:
        # End of input
        break
    # Calculation
    T = idata[0]
    CO2 = idata[1]
    light = idata[2]
    iphoto = calc_photosynthesis(T, CO2, light)
    # Output
    flag = channel_out.send(iphoto)
    if not flag:
        print('Error sending output')
        break
