#!/usr/bin/env python

import numpy as np
import os
import argparse

def calc_dist(coord1,coord2):
    '''
    Calculate distance between coordinate
    '''
    x_dist = coord1[0]-coord2[0]
    y_dist = coord1[1]-coord2[1]
    z_dist = coord1[2]-coord2[2]
    distance_12 = np.sqrt(x_dist**2 + y_dist**2 + z_dist**2)
    return distance_12

def bond_check(distance, min_dist=0, max_dist=1.5):
    '''
    Check if a distance is a bond based on a minimum and maximum length.
    Inputs: distance, min_length, max_length
    Defaults: min_length=0, max_length=1.5
    Return: True or False
    '''
    if min_dist < distance <= max_dist:
        return True
    else:
        return False

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This script analyzes a user provided xyz file and outputs all the bonds.")
    parser.add_argument("xyz_file", help="The filepath for the xyz file to analyze")
    args = parser.parse_args()

    file_location = args.xyz_file
    xyz_file = np.genfromtxt(file_location, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coordinates = xyz_file[:,1:]
    coordinates = coordinates.astype(np.float)

    num_atoms = len(symbols)
    for num1 in range(0,num_atoms):
        for num2 in range(0, num_atoms):
            if num1<num2:
                distance = calc_dist(coordinates[num1], coordinates[num2])
                if bond_check(distance):
                    print(F'{symbols[num1]:2} to {symbols[num2]:2} : {distance:.3f}')