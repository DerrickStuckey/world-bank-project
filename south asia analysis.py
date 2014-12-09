# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 15:51:33 2014

GWU Programming for Analytics Individual Project

@author: dstuckey
"""

import wbdata
import pandas
import datetime

saveDir = "./data"
createCSVs = False

# Read DF from CSV
def readFromCSV(dfName):
    df = pd.read_csv(saveDir + '/' + dfName + '.csv')
    return df

# Function to save a dataframe to CSV
def saveToCsv(df, dfName):
    df.to_csv(saveDir + '/' + dfName + '.csv')

# All countries in the "South Asia" region, 
# except Afghanistan which is missing data
countries = ['BGD','IND','LKA','MDV','NPL','BTN','PAK']

# Names for each indicator to be used throughout
elecIndName = 'Electricity Output'
energyIndName = 'Total Energy Consumption'
gdpIndName = 'GDP'
popIndName = 'Total Population'

indicators = {'4.1.1_TOTAL.ELECTRICITY.OUTPUT':elecIndName,
              '1.1_TOTAL.FINAL.ENERGY.CONSUM':energyIndName,
              'NY.GDP.MKTP.CD':gdpIndName}
              
# Define time period where all data is available
startTime = datetime.datetime(year=1990,month=1,day=1)
endTime = datetime.datetime(year=2009,month=12,day=31)

#grab indicators above for countires above and load into data frame
df = wbdata.get_dataframe(indicators, country=countries, convert_date=False,
                          data_date=(startTime,endTime))

#debugging:
#print "\ndf.head():\n", df.head()

#df is "pivoted", pandas' unstack fucntion helps reshape it into something plottable
dfu = df.unstack(level=0)

#dataframe of just electricity values
dfuElec = dfu[elecIndName]

#dataframe of just Energy values
dfuEnergy = dfu[energyIndName]

#dataframe of just GDP values
dfuGDP = dfu[gdpIndName]

# if flagged, create a set of CSV files, one for each indicator
if (createCSVs):
    saveToCsv(df, "South_Asian_Stats")
    saveToCsv(dfuElec, "South_Asian_ELectricity_Production")
    saveToCsv(dfuEnergy, "South_Asian_Energy_Usage")
    saveToCsv(dfuGDP, "South_Asian_GDP")