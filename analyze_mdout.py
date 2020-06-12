#!/usr/bin/env python

import argparse

'''
Good materials covering argparse
  1. https://realpython.com/command-line-interfaces-python-argparse/
  2. https://pymotw.com/2/argparse/
  
These materials helped me a lot getting the grasp of argparse
'''


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="This script parses AMBER mdout files to \
                                   extract the total energy. You can also use it to create plots")
  parser.add_argument('Path',
                      metavar='path',
                      type=str,
                      help='the path to mdout files')
  parser.add_argument('-p',
                      '--make_plots',
                      action='store_true',
                      help="generate plot file")
  
  args = parser.parse_args()
  
  mdout_file = args.Path
  mdout = open(mdout_file, 'r')
  lines = mdout.readlines()
  mdout.close()
  
  # Extract file_name from input file, then use it as the output: filename_Etot.txt
  # Not using split('.') since there is a possibility that the file have
  # more than one dot. Also this script is only for analyzing mdout file from AMBER
  
  filename = mdout_file[:-6]
  Etot_filename = filename + '_Etot.txt'
  
  with open(Etot_filename, 'w+') as f:
    for line in lines:
      if 'Etot' in line:
        energy = line.split()[2]
        f.write(F'{energy}\n')
      
      # The last two Etot values were some statistics associated with
      # the MD simulations and were not total energies.
      # They appear after the line 'A V E R A G E S   O V E R   30000 S T E P S'
      #
      # Therefore, if 'A V E R A G E S' encountered, exit out of 'for loop'
      
      if 'A V E R A G E S' in line:
        break
