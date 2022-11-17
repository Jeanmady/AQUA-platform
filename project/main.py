# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def main_menu():
    """Displays 5 options and requires an input to decide what function it will call. Calls a function depending on the users input."""
    # prints all the options for the menu
    print("Press corresponding key to access sub-menus: \n R - Access the PR module \n I - Access the MI module \n M - Access the RM module \n A - Print the About text \n Q - Quit the application")
    while True:  #while loop so user is forced to chose an option in the main menu
        submenu_input = (input("Select a sub-menu to access: ")).upper() #gets the users input and ensures its uppercased
        if submenu_input == "R": #checks if input is r
            reporting_menu()
            break
        elif submenu_input == "I": #checks if input is r
            intelligence_menu() #calls corresponding function
            break #ends while loop
        elif submenu_input == "M": #checks if input is m
            monitoring_menu() #calls corresponding function
            break #ends while loop
        elif submenu_input == "A": #checks if input is a
            about() #calls corresponding function
            break #ends while loop
        elif submenu_input == "Q": #checks if input is q
            quit() #calls corresponding function
            break #ends while loop
        else: #defensive programing to ensure ecvery input has a response
            print("No valid input detected, try again") #states it wasn't a valid input and does not break the loop so the user is asked for another input


def reporting_menu():
    """Your documentation goes here"""
    # Your code goes here
    

def monitoring_menu():
    """Your documentation goes here"""
    # Your code goes here


def intelligence_menu():
    """Your documentation goes here"""
    # Your code goes here

def about():
    """Prints strings giving module code and candidate number then proceeds back to main menu"""
    print("Module Code: ECM1400") #prints module code
    print("Candidate Number: 227131") #prints candidate number
    print("Returning to main menu") #states that now going back to main menu
    main_menu() #calls main menu function to return to the main menu

def quit():
    """Quits the program"""
    # Your code goes here




if __name__ == '__main__':
    main_menu()