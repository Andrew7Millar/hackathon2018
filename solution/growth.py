#!/usr/bin/python
from cis_interface.interface import CisInput, CisOutput

# Input & output channels
input = CisInput('photosynthesis_rate')
output = CisOutput('growth_rate', '%f\n')

# Loop over photosynthetic rates, calculating growth
while True:
    # Receive photosynthetic rate
    flag, data_input = input.recv()
    if not flag:
        print('growth: No more input.')
        break
    prate = data_input[0]
    # Calculate growth
    grate = 0.5 * prate
    print('growth: photosynthesis rate = %f ---> growth rate = %f' % (
        prate, grate))
    # Send growth to output
    flag = output.send(grate)
    if not flag:
        raise Exception('growth: Error sending growth rate.')
