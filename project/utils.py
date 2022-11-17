# Utils.py contains useful functions to be used in many different parts of the software

def sumvalues(values):
    """receives an array and returns the sum of the values in that sequence"""
    total_sum = 0  #assigning variable with a value 
    for i in range(0, len(values)): #looping through array by finding out array length
        if type(values[i]) == str: #Checking if each value is a string 
            pass #if it is, raise an exception
        else:
            total_sum = total_sum + values[i] #If its numerical add it to the total sum
    return total_sum #Returns the complete sum


def maxvalue(values):
    """Finds the highest value in an array"""    
    max_val = 0  #assigning variable with the first value of the array 
    for i in range(0, len(values)): #looping through array by finding out array length
        if type(values[i]) == str: #Checking if each value is a string 
            pass #if it is, raise an exception
        else:
            if max_val < values[i]: #If its numerical, compare to current max value
                max_val = values[i] #if bigger replaces as max value
            else:
                pass #since smaller go to the next value        
    return max_val #Returns the max value


def minvalue(values):
    """Finds the lowest value in an array"""    
    min_val = values[0]  #assigning variable with the first value of the array 
    for i in range(0, len(values)): #looping through array by finding out array length
        if type(values[i]) == str: #Checking if each value is a string 
            pass #if it is, raise an exception
        else:
            if min_val > values[i]: #If its numerical, compare to current min value
                min_val = values[i] #if smaller replaces as min value
            else:
                pass #since larger go to the next value        
    return min_val #Returns the lowest value


def meannvalue(values):
    """receives an array and returns the mean value of that sequence"""
    total_sum = 0  #assigning variable with a value 
    for i in range(0, len(values)): #looping through array by finding out array length
        if type(values[i]) == str: #Checking if each value is a string 
            pass #if it is, raise an exception
        else:
            total_sum = total_sum + values[i] #If its numerical add it to the total sum
    mean_val = total_sum / len(values) #Calcs the mean
    return mean_val #outputs value


def countvalue(values,xw):
    """Takes two parameters, values and xw. Looks in values and finds how many times value of xw occurs"""    
    total_occ = 0  #assigning variable to count occurences
    for i in range(0, len(values)): #looping through array by finding out array length
        if values[i] == xw: #Checking if each value is equivilent top the value wanted
            total_occ = total_occ + 1 #incrementing occurence variable
        else:
            pass # goiung to next value if no occurence found
    return total_occ #Returns the total occurences



