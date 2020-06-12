#!/usr/bin/env python

import os
import numpy as np
import matplotlib.pyplot as plt
import argparse

'''
Good materials covering argparse
  1. https://realpython.com/command-line-interfaces-python-argparse/
  2. https://pymotw.com/2/argparse/
  
These materials helped me a lot getting the grasp of argparse
'''

def read_mdout(mdout_file):
  '''
  This function will read mdout_file, and write Etot mdout_file_Etot.txt
  It will return Etot_filename (Energy total output filename) which
  can be used for plotting.
  '''
  mdout = open(mdout_file, 'r')
  lines = mdout.readlines()
  
  # Extract file_name from input file, then use it as the output: filename_Etot.txt
  # Not using split('.') since there is a possibility that the file have
  # more than one dot. Also this script is only for analyzing mdout file from AMBER
  
  filename = mdout_file[:-6]
  Etot_filename = filename + '_Etot.txt'
  
  times = []
  etots = []
  
  for line in lines:
    if 'Etot' in line:
      etots.append(line.split()[2])
    if 'TIME(PS)' in line:
      times.append(line.split()[5])
      
  times = times[:-2]
  etots = etots[:-2]
  
  etots_len = len(etots)
  with open(Etot_filename, 'w+') as f:
    for i in range(etots_len):
      time = times[i]
      etot = etots[i]
      f.write(F'{time} {etot}\n')
  
  return Etot_filename


def plot_mdout(Etot_filename):
  '''
  This function will read the provided Etot_filename and plot the time vs energy total
  '''
  filename = Etot_filename[:-9]
  basename = os.path.basename(filename)
  
  data = np.genfromtxt(Etot_filename, dtype='unicode')
  data = data.astype(np.float)
  plt.figure()
  plt.title(F'Energy Total plot for {basename}.mdout')
  plt.xlabel('Simulation Time (ps)')
  plt.ylabel('Energy Total (kcal/mol)')
  plt.plot(data[:,0], data[:,1])
  
  # Remove _Etot.txt and append .png
  plot_filename = filename + '.png'
  plt.savefig(plot_filename)
  

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="This script parses AMBER mdout files to \
                                   extract the total energy. You can also use it to create plots")
  # Add nargs='*' to allow multiple file input (eg. 'mdout/*.mdout')
  parser.add_argument('Path',
                      metavar='path',
                      type=str,
                      nargs='*',
                      help='the path to mdout files')
  parser.add_argument('-p',
                      '--make_plots',
                      action='store_true',
                      dest='make_plots',
                      help="generate plot file")
  
  args = parser.parse_args()
  
  for mdout_file in args.Path:
    Etot_filename = read_mdout(mdout_file)
    if args.make_plots:
      plot_mdout(Etot_filename)
    
