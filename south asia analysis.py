# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 15:51:33 2014

GWU Programming for Analytics Individual Project

@author: dstuckey
"""

import wbdata
import pandas
import matplotlib.pyplot as plt

 
#set up the countries I want
countries = ['BGD','IND','LKA','MDV','NPL']
#countries = ['BGD','BTN','IND','LKA','MDV','NPL']
 
#set up the indicator I want (just build up the dict if you want more than one)
#indicators = {'1.1_TOTAL.FINAL.ENERGY.CONSUM':'Total Energy Consumption'} #good for south asia
#indicators = {'NY.GDP.MKTP.CD':'GDP'} #good for south asia
#indicators = {'4.1.1_TOTAL.ELECTRICITY.OUTPUT':'Electricity Output'} #good for south asia
#indicators = {'SP.POP.TOTL':'Total Population'} #good for south asia
#indicators = {'SP.URB.TOTL.IN.ZS':'% Urban Pop',} #good for south asia

elecIndName = 'Electricity Output'
energyIndName = 'Total Energy Consumption'
indicators = {'4.1.1_TOTAL.ELECTRICITY.OUTPUT':elecIndName,
              '1.1_TOTAL.FINAL.ENERGY.CONSUM':energyIndName}

#grab indicators above for countires above and load into data frame
df = wbdata.get_dataframe(indicators, country=countries, convert_date=False)

print "\ndf.head():\n", df.head()

#df is "pivoted", pandas' unstack fucntion helps reshape it into something plottable
dfu = df.unstack(level=0)

#or get rid of multi-index
dfuElec = dfu[elecIndName]
print "\nElectricity columns: \n", dfuElec.columns

print "\nElec head and tail: \n", 
print dfuElec.head()
print dfuElec.tail()

#or get rid of multi-index
dfuEnergy = dfu[energyIndName]
print "\nEnergy columns: \n", dfuEnergy.columns

print "\nEnergy head and tail: \n", 
print dfuEnergy.head()
print dfuEnergy.tail()
 
# a simple matplotlib plot with legend, labels and a title
#dfu.plot(); 
#plt.legend(loc='best'); 
#plt.title("Energy Consumption"); 
#plt.xlabel('Date'); 
#plt.ylabel('Energy Consumption');