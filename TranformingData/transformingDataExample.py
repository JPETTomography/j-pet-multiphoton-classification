#!/usr/bin/env python3.6

import pandas as pd
import sys
import pickle
import matplotlib.pyplot as plt

pathToFile = 'NEMA_IQ_384str_N0_1000_COINCIDENCES_PREPARED_part00'

if sys.argv[1]:
    pathToFile = sys.argv[1]

print("Loading data from " + pathToFile + ".")

data = pickle.load(open(pathToFile, 'rb'))
dataClass1 = data[data['class'] == 1]
dataClass2 = data[data['class'] == 2]
dataClass3 = data[data['class'] == 3]
dataClass4 = data[data['class'] == 4]

fig = plt.gcf()
fig.set_size_inches(15.5, 6.0)
fig.suptitle('Energia zmierzonych cząstek', fontsize = 16)
ax1 = plt.subplot(1,3,1)
ax1.ticklabel_format(style = 'sci', axis = 'y', scilimits = (0,0))
ax1.hist(dataClass1['e1'], bins = 100, alpha = 0.5, color = 'green', label = 'Class 1')
ax1.hist(dataClass2['e1'], bins = 100, alpha = 0.5, color = 'red', label = 'Class 2')
ax1.set_xlabel('Energy [keV]', fontsize = 20)
ax1.tick_params(direction = 'out', labelsize = 15)
ax1.legend()
ax2 = plt.subplot(1,3,2)
ax2.ticklabel_format(style = 'sci', axis = 'y', scilimits = (0,0))
ax2.hist(dataClass1['e1'], bins = 100, alpha = 0.5, color = 'green', label = 'Class 1')
ax2.hist(dataClass3['e1'], bins = 100, alpha = 0.5, color = 'red', label = 'Class 3')
ax2.set_xlabel('Energy [keV]', fontsize = 20)
ax2.legend()
ax2.tick_params(direction = 'out', labelsize = 15)
ax3 = plt.subplot(1,3,3)
ax3.ticklabel_format(style = 'sci', axis = 'y', scilimits = (0,0))
ax3.hist(dataClass1['e1'], bins = 100, alpha = 0.5, color = 'green', label = 'Class 1')
ax3.hist(dataClass4['e1'], bins = 100, alpha = 0.5, color = 'red', label = 'Class 4')
ax3.set_xlabel('Energy [keV]', fontsize = 20)
ax3.legend()
ax3.tick_params(direction = 'out', labelsize = 15)
plt.savefig('classEnergyDistribution.png')