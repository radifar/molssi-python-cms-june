#!/usr/bin/env python
# coding: utf-8

# ## Geometry Analysis Homework solution

# In[1]:


import numpy as np
import os


# In[2]:


file_location = os.path.join('data','water.xyz')
print(file_location)


# In[4]:


xyz_file = np.genfromtxt(file_location, dtype='unicode', skip_header=2)


# In[5]:


print(xyz_file)


# In[6]:


symbols = xyz_file[:,0]
coordinates = xyz_file[:,1:]
print(symbols)
print(coordinates)


# In[7]:


coordinates = coordinates.astype(np.float)


# In[8]:


print(coordinates)


# $ distance = \sqrt{(x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2} $

# In[13]:


num_atoms = len(symbols)
for num1 in range(0,num_atoms):
    for num2 in range(0,num_atoms):
        if num1<num2:
            x_distance = coordinates[num1,0]-coordinates[num2,0]
            y_distance = coordinates[num1,1]-coordinates[num2,1]
            z_distance = coordinates[num1,2]-coordinates[num2,2]
            distance_12 = np.sqrt(x_distance**2+y_distance**2+z_distance**2)
            if distance_12<1.5:
                print(F'{symbols[num1]:2} to {symbols[num2]:2} : {distance_12:.3f}')


# In[18]:


import numpy
import os
file_location = os.path.join('data','water.xyz')
xyz_file = numpy.genfromtxt(fname=file_location, dtype='unicode', skip_header=2)
symbols = xyz_file[:,0]
coordinates = xyz_file[:,1:]
coordinates = coordinates.astype(numpy.float)
num_atoms = len(symbols)
for num1 in range(0,num_atoms):
    for num2 in range(0,num_atoms):
        if num1<num2:
            x_distance = coordinates[num1,0]-coordinates[num2,0]
            y_distance = coordinates[num1,1]-coordinates[num2,1]
            z_distance = coordinates[num1,2]-coordinates[num2,2]
            distance_12 = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
            if distance_12 > 0 and distance_12 <= 1.5:
                print(F'{symbols[num1]} to {symbols[num2]} : {distance_12:.3f}')


# In[ ]:




