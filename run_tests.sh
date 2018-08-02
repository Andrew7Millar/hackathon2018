#!/usr/bin/env bash

# Run original model
mkdir Output
python growth.py Input/photosynthesis_rate.txt Output/growth_rate.txt

# Run integrations with files
cisrun tests/test_growth.yml
cisrun tests/test_light.yml
cisrun tests/test_photosynthesis.yml
cisrun tests/test_canopy.yml

# Run complete integration network
cisrun tests/test_network.yml
