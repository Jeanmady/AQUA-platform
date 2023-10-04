# Reporting.py provides functions to manipulate pollution data
import numpy as np # Imports numpy library
import pandas as pd # Imports pandas library
import utils # imports utils.py


def daily_average(data, monitoring_station, pollutant):
    """
    Calculates the daily averages for a specified pollutant and monitoring station
    parameters: data, monitoring_station, pollutant
    return: A 2D array of the dates and the daily averages
    """
    daily_average = [] # Creates an array to store averages
    data = pd.read_csv('data/{}.csv'.format(monitoring_station)) # calling the csv file using pandas creating DataFrame
    all_dates = data['date'] # Creates a DataFrame of all the dates
    unique_dates = all_dates.drop_duplicates() # Drops all duplications of dates to only have unique dates
    data = fill_missing_data('', '0', monitoring_station, pollutant) # Fills the missing data by callling the fill missing data function
    data_pollutant = data[pollutant] # Creates a DataFrame of all the pollutants
    data_pollutant_array = list(data_pollutant) # Turns into an array
    for i in range(0,len(data_pollutant_array),24): # loops thorugh array
        day = [] # creates day array
        for items in range(i,i+24): # loops through dates in array
            day.append(float(data_pollutant_array[items])) # Adds dates to day array
        mean = utils.meannvalue(day) # Calculates the mean using the utility function meannvalue()
        daily_average.append(mean) # Adds mean values to the daily average array
    averages = np.array(daily_average) # Alters to numpy array
    daily_average = np.column_stack((unique_dates, averages)) # Concentates arrays into one 2d array
    return daily_average 
    

def daily_median(data, monitoring_station, pollutant): # Last thing try reomove median
    """
    Calculates the daily median for a specified pollutant and monitoring station
    parameters: data, monitoring_station, pollutant
    return: A 2D array of the dates and the daily medians
    """
    data = pd.read_csv('data/{}.csv'.format(monitoring_station)) # calling the csv file using pandas creating DataFrame
    all_dates = data['date'] # Creates a DataFrame for a date
    unique_dates = all_dates.drop_duplicates() # Drops all duplicates of the dates
    data = fill_missing_data('', '0', monitoring_station, pollutant) # Fills missing data using fill_missing_data function
    data[pollutant] = pd.to_numeric(data[pollutant]) # Numerifies the pollutant column
    median = data.groupby(['date']).median() # Groups by date and then applies median function
    median_1D = median.iloc[:,0] # Turns the median df into a 1d array
    daily_median = np.column_stack((unique_dates, median_1D)) # Joins the two arrays into one 2d array
    return daily_median


def hourly_average(data, monitoring_station, pollutant): 
    """
    Calculates the hourly averages for a specified pollutant and monitoring station
    parameters: data, monitoring_station, pollutant
    return: A 2D array of the hours and the hourly averages
    """
    hourly_average = [] # Creates an array to store averages
    data = pd.read_csv('data/{}.csv'.format(monitoring_station)) # calling the csv file using pandas creating DataFrame
    all_hours = data['time'] # Creates a DataFrame of all the hours
    unique_hours = all_hours.drop_duplicates() # Drops all duplications of hours to only have unique hours
    data = fill_missing_data('', '0', monitoring_station, pollutant) # Fills the missing data by callling the fill missing data function
    data_pollutant = data[pollutant] # Creates a DataFrame of all the pollutants
    data_pollutant_array = list(data_pollutant) # Turns into an array
    for i in range(0,24): # Loops through to create subarrays and iterate through appending of arrays
        hours = [] # creates hour array
        for items in range(i, 8760, 24): # loops through pollutants in steps of 24 with a max of 8760
            hours.append(float(data_pollutant_array[items])) # Adds polluatants to array
        mean = utils.meannvalue(hours) # Calculates the mean using the utility function meannvalue()
        hourly_average.append(mean) # Adds mean values to the hourly average array
    averages = np.array(hourly_average) # Alters to numpy array
    hourly_average = np.column_stack((unique_hours, averages)) # Concentates arrays into one 2d array
    return hourly_average


def monthly_average(data, monitoring_station, pollutant): 
    """
    Calculates the monthly averages for a specified pollutant and monitoring station
    parameters: data, monitoring_station, pollutant
    return: A 2D array of the months and the monthly averages
    """
    monthly_average = [] # Creates an array to store averages
    data = pd.read_csv('data/{}.csv'.format(monitoring_station)) # calling the csv file using pandas creating DataFrame
    all_months = data['date'].str[:-3] # Creates a DataFrame of all the dates
    unique_dates = all_months.drop_duplicates() # Drops all duplications of dates to only have unique dates
    unique_dates = unique_dates.reset_index(drop=True) # Resets the index to make sorting easier
    data = fill_missing_data('', '0', monitoring_station, pollutant) # Fills the missing data by callling the fill missing data function
    data_pollutant = data[pollutant] # Creates a DataFrame of all the pollutants
    data_pollutant_array = list(data_pollutant) # Turns into an array
    for i in range(0,12): # loops thorugh array
        month = [] # creates day arrays
        # Finds out what month it is and gives it the correct length of the month
        if unique_dates.iloc[i]  == "2021-02": # Checks if month is 02
            length_month = 28 # Applies correct length
        # Checks if month is 04,06, 09 or 11 ads they all have a length  of 30 days
        elif unique_dates.iloc[i]  == "2021-04" or unique_dates.iloc[i]  == "2021-06" or unique_dates.iloc[i]  == "2021-09" or unique_dates.iloc[i]  == "2021-11":
            length_month = 30 # Applies correct length
        else: # Once all possibilites exhausted length must be 31
            length_month = 31 # Applies correct length
        # Calculates the previous months length
        if i == 0: # CHecks if i is 0 so no error is thrown
            old_length_month = 0 # Sets month to equal 0
        else:
            # Finds out what previous months length wasw
            if unique_dates.iloc[i-1]  == "2021-02": # Checks if month is 02
                old_length_month = 28 # Applies correct length
                # Checks if month is 04,06, 09 or 11 ads they all have a length  of 30 days
            elif unique_dates.iloc[i-1]  == "2021-04" or unique_dates.iloc[i-1]  == "2021-06" or unique_dates.iloc[i-1]  == "2021-09" or unique_dates.iloc[i-1]  == "2021-11":
                old_length_month = 30 # Applies correct length
            else: # Once all possibilites exhausted length must be 31
                old_length_month = 31 # Applies correct length
        for items in range(old_length_month*24, ((length_month)*24)+(old_length_month*24)-1): # loops through months in array
            month.append(float(data_pollutant_array[items])) # Adds months to day array
        mean = utils.meannvalue(month) # Calculates the mean using the utility function meannvalue()
        monthly_average.append(mean) # Adds mean values to the monthly average array
    averages = np.array(monthly_average) # Alters to numpy array
    monthly_average = np.column_stack((unique_dates, averages)) # Concentates arrays into one 2d array
    return monthly_average
    
   
def peak_hour_date(data, date, monitoring_station, pollutant): 
    """
    Calculates the peak hour date for a specified date, pollutant and monitoring station
    parameters: data, date, monitoring_station, pollutant
    return: The peak hour and the value 
    """
    data = pd.read_csv('data/{}.csv'.format(monitoring_station)) # calling the csv file using pandas creating DataFrame
    data_filled = fill_missing_data('', '0', monitoring_station, pollutant) # Fills the missing data by callling the fill missing data function
    data_filled = data_filled.set_index('date') # Indexes the date
    data_filled = data_filled.loc[date] # Selects specifically date
    data_indexed = data_filled.set_index('time') # Indexes the time
    data_pollutant = data_indexed[pollutant] # Selects specifically pollutants
    data_pollutant = pd.to_numeric(data_pollutant) # Converts data_pollutant into a numeric type
    highest_value = data_pollutant[utils.maxvalue(data_pollutant)] # Calls the utils function maxvalue to apply on the pollutant data
    peak_hour = data_pollutant[data_pollutant == highest_value].index[0] # Finds the corresponding time to the peak value
    peak_hour = peak_hour[:-6] # Removes seconds and minutes from the time to display just peak hour
    return peak_hour, highest_value # Returns the hour and the data of the peak hour


def count_missing_data(data, monitoring_station, pollutant):
    """
    Counts the number of missing data entries in a specified monitoring station and pollutant
    parameters: data, monitoring_station, pollutant
    return: number of missing datas
    """
    pollutant_array = [] # Creates pollutant array
    data = pd.read_csv('data/{}.csv'.format(monitoring_station)) # calling the csv file using pandas creating DataFrame
    pollutant_data = data[pollutant] # Creates a DataFrame for pollutant data
    for i in range(0,len(pollutant_data)): # Loops through length of pollutants
        pollutant_array.append(pollutant_data[i]) # Adds pollutants to pollutants array
    null_data = utils.countvalue(pollutant_array, "No data") # Counts the number of no data ntries in the pollutant array
    return null_data # Returns null data count


def fill_missing_data(data, new_value, monitoring_station, pollutant):
    """
    Fills all missing data entries from a specified monitoring station and pollutant and then replaces with a chosen new value
    parameters: data, new_value, monitoring_station, pollutant
    return: A copy of the DataFrame with all the missing data filled with new value
    """
    data = pd.read_csv('data/{}.csv'.format(monitoring_station)) # calling the csv file using pandas creating DataFrame
    data = data.replace('No data', new_value) # Replaces all no data values with new value
    return data # Returns a copy of the data


