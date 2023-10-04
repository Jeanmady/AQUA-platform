# main.py controls the program calling all other files
import reporting as rep # imports the reporting.py file for use in reporting function
import intelligence as intel # imports thr intelligence.py file for use in intelligence function
import sys # imports the system libraary

def main_menu():
    """
    Displays 5 options and requires an input to decide what function it will call. Calls a function depending on the users input.
    parameters: None
    returns: None
    """
    # prints all the options for the menu
    print("Press corresponding key to access sub-menus: \n R - Access the PR module \n I - Access the MI module \n M - Access the RM module \n A - Print the About text \n Q - Quit the application")
    while True:  # while loop so user is forced to chose an option in the main menu
        submenu_input = (input("Select a sub-menu to access: ")).upper() # gets the users input and ensures its uppercased
        if submenu_input == "R": # checks if input is r
            reporting_menu() # calls corresponding function
            break # ends while loop
        elif submenu_input == "I": # checks if input is i
            intelligence_menu() # calls corresponding function
            break # ends while loop
        elif submenu_input == "M": # checks if input is m
            monitoring_menu() # calls corresponding function
            break # ends while loop
        elif submenu_input == "A": # checks if input is a
            about() # calls corresponding function
            break # ends while loop
        elif submenu_input == "Q": # checks if input is q
            quit() # calls corresponding function
            break # ends while loop
        else: # defensive programing to ensure ecvery input has a response
            print("No valid input detected, try again") # states it wasn't a valid input and does not break the loop so the user is asked for another input


def reporting_menu():
    """
    Calls a pollution analysis based ion users input, returns requested data then returns to main menu
    parameters: None
    returns: None
    """
    print("Choose a pollution analysis: \n DA - Daily Average \n DM - Daily Median \n HA - Hourly Average \n MA - Monthly Average \n PHD - Peak Hour Data \n CMD - Count Missing Data \n FMD - Fill Missing Data \n E- Exit to Main Menu") #prints all the options for the menu
    while True:  # while loop so user is forced to chose an option in the main menu
        reporting_menu_input = (input("Choose an option: ")).upper() # gets the users input and ensures its uppercased
        if reporting_menu_input == "DA": # Checks if input is DA
            monitoring_station = choose_monitoring_station() # Calls monitoring station function to gather user choice
            pollutant = choose_pollutant() # Calls pollutant function to gather user choice
            daily_average = rep.daily_average(1,monitoring_station, pollutant) # calls daily average function
            print("Daily averages are: \n {}".format(daily_average)) # Returns data requested
            main_menu() # Calls main menu
            break # ends while loop
        elif reporting_menu_input == "DM": # Checks if input is DM
            monitoring_station = choose_monitoring_station() # Calls monitoring station function to gather user choice
            pollutant = choose_pollutant() # Calls pollutant function to gather user choice
            daily_median = rep.daily_median(1,monitoring_station, pollutant) # calls daily median function
            print("Daily medians are: \n {}".format(daily_median)) # Returns data requested
            main_menu() # Calls main menu
            break # ends while loop
        elif reporting_menu_input == "HA": # Checks if input is HA
            monitoring_station = choose_monitoring_station() # Calls monitoring station function to gather user choice
            pollutant = choose_pollutant() # Calls pollutant function to gather user choice
            hourly_average = rep.hourly_average(1,monitoring_station, pollutant) # calls hourly average function
            print("Hourly averages are: \n {}".format(hourly_average)) # Returns data requested
            main_menu() # Calls main menu
            break # ends while loop
        elif reporting_menu_input == "MA": # Checks if input is MA
            monitoring_station = choose_monitoring_station() # Calls monitoring station function to gather user choice
            pollutant = choose_pollutant() # Calls pollutant function to gather user choice
            monthly_average = rep.monthly_average(1,monitoring_station, pollutant) # calls monthly average function
            print("Monthly averages are: \n {}".format(monthly_average)) # Returns data requested
            main_menu() # Calls main menu
            break # ends while loop
        elif reporting_menu_input == "PHD": # Checks if input is PHD
            date = input("Choose a date in format YYYY-MM-DD: ") # gets user input for a date
            if date[:4] != "2021":
                print("Date is out of range returning to main menu")
                main_menu()
            else:
                pass
            monitoring_station = choose_monitoring_station() # Calls monitoring station function to gather user choice
            pollutant = choose_pollutant() # Calls pollutant function to gather user choice
            peak_hour_date = rep.peak_hour_date(1,date, monitoring_station, pollutant) # calls peak hour data function
            print("Peak hour date is: \n {}".format(peak_hour_date)) # Returns data requested
            main_menu() # Calls main menu
            break # ends while loop
        elif reporting_menu_input == "CMD": # Checks if input is CMD
            monitoring_station = choose_monitoring_station() # Calls monitoring station function to gather user choice
            pollutant = choose_pollutant() # Calls pollutant function to gather user choice
            count_missing_data = rep.count_missing_data(1,monitoring_station, pollutant) # calls count missing data function
            print("Number of missing data is: \n {}".format(count_missing_data)) # Returns data requested
            main_menu() # Calls main menu
            break # ends while loop
        elif reporting_menu_input == "FMD": # Checks if input is FMD
            new_value = input("Enter a new value to replace all no-data entries: ") # gets user input for the new value
            monitoring_station = choose_monitoring_station() # Calls monitoring station function to gather user choice
            pollutant = choose_pollutant() # Calls pollutant function to gather user choice
            fill_missing_data = rep.fill_missing_data(1,new_value, monitoring_station, pollutant) # calls reporting menu function
            print("Data with the missing no-data filled: \n {}".format(fill_missing_data)) # Returns data requested
            main_menu() # Calls main menu
            break # ends while loop
        elif reporting_menu_input == "E": # Checks if input is E
            print("Returning to Main Menu") # Informs user of returning to main menu
            main_menu() # calls main menu function
        elif reporting_menu_input == "M": # checks if correct key has been input
            main_menu() # calls main menu function
            break # ends while loop
        else: # defensive programing to ensure every input has a response
            print("No valid input, try again") # states it wasn't a valid input and does not break the loop so the user is asked for another input 


def choose_monitoring_station():
    """
    Function to aid user in choosing a monitoring station
    parameters: None
    returns: Chosen monitoring station variable
    """
    while True: # while loop so user is forced to chose an option in monitoring station menu
        monitoring_station = (input("Choose a monitoring station: \n H - Harlington \n M - Marylebone Road \n NK - N Kensington \n E - Return to reporting Menu \n Option chosen: ")).upper() #lists all the users choices and records the input
        if monitoring_station == "H": # Checks if users input is Harlington
            monitoring_station = "Pollution-London Harlington" # sets correct syntax so the correct csv file can be called
            break # Ends while loop
        elif monitoring_station == "M": # Checks if users input is Marylebone
            monitoring_station = "Pollution-London Marylebone Road" # sets correct syntax so the correct csv file can be called
            break # Ends while loop
        elif monitoring_station == "NK": # Checks if users input is N Kensington
            monitoring_station = "Pollution-London N Kensington" # sets correct syntax so the correct csv file can be called
            break # Ends while loop
        elif monitoring_station == "E": # Checks if users input is exit
            print("Returning to Reporting Menu") # Informs user of returning to reporting menu
            reporting_menu() # calls the function
        else: # defensive programing to ensure every input has a response
            print("No valid input, try again") # states it wasn't a valid input and does not break the loop so the user is asked for another input 
    return monitoring_station # Returns final choice


def choose_pollutant():
    """
    Function to aid user in choosing a pollutant
    parameters: None
    returns: pollutant choice variable
    """
    while True: # while loop so user is forced to chose an option in the pollutant menu
        pollutant_choice = (input("Choose a Pollutant: \n pm10 \n no \n pm25 \n E - Return to reporting Menu \n Option chosen: ")) # lists al the users choices and records the input
        if pollutant_choice == "pm10": # Checks if users input is pm10
            break # Ends while loop
        elif pollutant_choice == "no": # Checks if users input is no
            break # Ends while loop
        elif pollutant_choice == "pm25": #Checks if users input is pm25
            break # Ends while loop
        elif pollutant_choice == "E" or pollutant_choice == "e": # Checks if users input is exit to reporting menu
            print("Returning to Reporting Menu") # Informs user of returning to reporting menu
            reporting_menu() # calls the function
        else: # defensive programing to ensure every input has a response
            print("No valid input, try again") # states it wasn't a valid input and does not break the loop so the user is asked for another input        
    return pollutant_choice # Returns final choice


def monitoring_menu():
    """Your documentation goes here"""
    # Your code goes here


def intelligence_menu():
    """
    Calls a intelligence option determined by a user, prints requested output then returns to menu
    parameters: None
    returns: None
    """
    print("Choose an Intelligence option: \n R - Find red pixels \n C - Find cyan pixels \n D - Detect connected components \n DS - Detect connected components sorted \n E - Exit to Main Menu")
    while True:
        intelligence_menu_input = (input("Choose an option: ")).upper() # gets the users input and ensures its uppercased
        if intelligence_menu_input == "R": # Checks if input is R
            print(intel.find_red_pixels("data/map.png", 50, 100)) # Calls the function
            main_menu() # Returns to main menu
            break # Ends while loop
        elif intelligence_menu_input == "C": # Checks if input is C
            print(intel.find_cyan_pixels("data/map.png", 100, 50)) # Calls the function
            main_menu() # Returns to main menu
            break # Ends while loop
        elif intelligence_menu_input == "D": # Checks if input is D
            print(intel.detect_connected_components()) # Calls the function
            main_menu() # Returns to main menu
            break # Ends while loop
        elif intelligence_menu_input == "DS": # Checks if input is DS
            print(intel.detect_connected_components_sorted()) # Calls the function
            main_menu() # Returns to main menu
            break # Ends while loop
        elif intelligence_menu_input == "E": # Checks if input is E
            print("Returning to Main Menu") # Informs user of returning to main menu
            main_menu() # calls main menu function
        else:
            print("No valid input, try again") # No valid input so while condition isnt met and loop continues


def about():
    """
    Prints strings giving module code and candidate number then proceeds back to main menu
    parameters: None
    returns: None
    """
    print("Module Code: ECM1400") # prints module code
    print("Candidate Number: 227131") # prints candidate number
    print("Returning to main menu") # states that now going back to main menu
    main_menu() # calls main menu function to return to the main menu


def quit():
    """
    Quits the program
    parameters: None
    returns: None
    """
    sys.exit("Goodbye!!") # Exits program


if __name__ == '__main__':
    main_menu()