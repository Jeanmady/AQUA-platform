# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


def daily_average(data, monitoring_station, pollutant):
    """takes three parameters: data, monitoring_station and pollutant. Uses these to output the daily averages for 365 days for the chosen pollutant and monitoring station"""
    df = pd.read_csv('data/{}.csv'.format(monitoring_station), #calling the csv file using pandas
                    usecols=['date', 'time', 'no', 'pm10', 'pm25'],  #stating coloumns 
                    parse_dates=['date']) #declaring the data type of dates so it has pandas date functionaslity
    df['no'] = pd.factorize(df['no'])[0].astype(float) #Objects cannot be changed when reading csv initially so must be changed after
    df['pm10'] = pd.factorize(df['pm10'])[0].astype(float)
    df['pm25'] = pd.factorize(df['pm25'])[0].astype(float)
    daily_average = df.groupby('date')[pollutant].mean() #daily average is calculated here by using groupby to group the dates together then uses the parameter to select what data the mean function will be carried out on
    return(daily_average) #return the values
    

def daily_median(data, monitoring_station, pollutant):
    """takes three parameters: data, monitoring_station and pollutant. Uses these to output the daily medians for 365 days for the chosen pollutant and monitoring station"""
    df = pd.read_csv('data/{}.csv'.format(monitoring_station), #calling the csv file using pandas
                    usecols=['date', 'time', 'no', 'pm10', 'pm25'],  #stating coloumns 
                    parse_dates=['date']) #declaring the data type of dates so it has pandas date functionaslity
    df['no'] = pd.factorize(df['no'])[0].astype(float) #Objects cannot be changed when reading csv initially so must be changed after
    df['pm10'] = pd.factorize(df['pm10'])[0].astype(float)
    df['pm25'] = pd.factorize(df['pm25'])[0].astype(float)
    daily_median = df.groupby('date')[pollutant].median() #daily median is calculated here by using groupby to group the dates together then uses the parameter to select what data the median function will be carried out on
    return(daily_median) #return the values

def hourly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here
def monthly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here
def peak_hour_date(data, date, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here

def count_missing_data(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here

def fill_missing_data(data, new_value, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here
print(daily_median(1,'Pollution-London Harlington','pm25'))