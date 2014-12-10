# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 15:51:33 2014

GWU Programming for Analytics Individual Project

@author: dstuckey
"""

import wbdata
import pandas as pd
import datetime
import MySQLdb as myDB
from sqlalchemy import create_engine

#Run parameters
saveDir = "./data"
createCSVs = False
useDB = False

#Database configuration info
mysql_host = "173.194.241.40"
mysql_user = "root"
mysql_pass = "beer"
mysql_db = "worldbank"
data_table = "south_asia_stats"

# Read DF from CSV
def readFromCSV(dfName):
    df = pd.read_csv(saveDir + '/' + dfName + '.csv')
    return df

# Function to save a dataframe to CSV
def saveToCsv(df, dfName):
    df.to_csv(saveDir + '/' + dfName + '.csv')
    
# Returns single DB Connect object to be used multiple times
def getDBConnect():
    return myDB.connect(host=mysql_host,
                        user=mysql_user,
                        passwd=mysql_pass,
                        db=mysql_db)
       
# Function to save DataFrame to MySQL database
def saveToDB(df, table, dbConnect):
    #clean up any 'NaN' fields which mysql doesn't understand
    dfClean = df.where((pd.notnull(df)), None)
    dfClean.to_sql(con=dbConnect,
                    name=table,
                    if_exists="replace",
                    flavor='mysql')

# Missing sqlalchemy.schema module
def readFromDB(table, dbConnect):
    engine = create_engine('mysql+mysqldb://' + mysql_user + ':' + mysql_pass + '@' + mysql_host + '/' + mysql_db)
    
    df = pd.read_sql_table(table, con=engine)
    return df

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

#If useDB flag is True, save the dataframe to the database and read it back out
if (useDB):
    dbCon = getDBConnect()
    saveToDB(df, data_table, dbCon)
    df = readFromDB(data_table, dbCon)

#unstack dataframe to separate into one dataframe per indicator
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