#==============Question 1====================

def hello_name(user_name):
    """Write a greeting that uses a username"""
    print("Hello "+ user_name + "!")

hello_name("Anna")

#==============Question 2====================

def first_odds(): 
    """Prints odd numbers from 1-100"""
number_list = range(0,100+1)
for number in number_list:
    if number %2 !=0:
        print(number)
        

#==============Question 3====================


def max_num_in_list(a_list):
    """Finds the max number in a list"""
    the_max = a_list[0]
    for index in a_list:
        if (index > the_max):
            the_max = index
    return the_max 

a_list = [1,5,7,10,12]
max_num = max_num_in_list(a_list)


print(max_num)
    


#==============Question 4====================

def is_leap_year(a_year):
    """Provides whether or not a year is a leap year"""
    if (a_year % 4) ==0:
        return True
    elif (a_year % 100) or (a_year % 400)==0:
        return False 
        
print(is_leap_year(1994))
    

#==============Question 5====================

def is_consecutive(a_list): 
    """Figures out if numbers in a list are consecutive"""
    n = len(a_list)
    for index in range(1,n):
        if a_list[index] - a_list[index] !=1: 
            return False
    return True 

a_list=[1,3,6,9,7]

print(is_consecutive(a_list))
