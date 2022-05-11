''' 
Programmed By Christian Moloci
Chapter 9 Lab
based on: http://programarcadegames.com/index.php?chapter=lab_functions&lang=en
'''

#import libraries
import random



#First Function. used for comparing numbers to eachother
def min3(x, y, z):
    # If statements for comaring numbers to eachother to find lowest value and return 
    if x < y and z > y:
        return x
    if x < z and y > x:
        return x
    if y < x and z > x:
        return y
    if y < z and x > y:
        return y
    if z < y and x > z:
        return z
    if z < x and y > x:
        return z
    if x == y and y == z:
        return x

# Pass numbers through the comparison function
print("the lowest value is: ", min3(4, 7, 5))
print("the lowest value is: ", min3(4, 5, 5))
print("the lowest value is: ", min3(4, 4, 4))
print("the lowest value is: ", min3(-2, -6, -100))
print("the lowest value is: ", min3("Z", "B", "A"))

# Second Part of lab

# Function that runs math based on numbers passed through it to create boxes using *'s
def box(height_Num, width_Num):
    star = "*"
    for i in range(height_Num):
        print(width_Num * star)

# pass numbers through the function and print blank lines to seperate it
box(7,5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3,2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3,10) # Print a box 3 high, 10 across

# Thrid Part of lab

# Function to find index of a number
def find(my_list, indexNum):
    # uses try and except to test if it's possible to run and if it cant, there is code for exceptions
    try:
        print("I found the number at the location : ", my_list.index(indexNum))
    except ValueError:
        print("Out of bounds, number not found at any location")

# List given from programarcadegames.com to use with the function
my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

# Used to locate the index of the values below
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)

#Fourth part of lab

# Just an empty print function to provide a line break
print("")

# function to return randomized list
def create_list(list_size):
    #must convert my_list1 for a var to a list
    my_list1 = []
    #for final part of lab
    my_list2 = []
    #for loop to keep adding random numers in range list_size
    for i in range(list_size):
        list_item = random.randint(1, 6) #var to hold temp rand num
        my_list1.append(list_item) # append random number to list
        my_list2.append(list_item) # append random number to list
    return my_list1 #return list

my_list1 = create_list(5) # call func and define range
print("here are some random numbers: ", my_list1) # print final rand list

# second part of four

#function to count how many times a number appears in a list
def count_list(main_list, list_index_num):
    count = main_list.count(list_index_num)
    print("the given list has", count, "values of", list_index_num)

# passes list through func
count = count_list([1,2,3,3,3,4,2,1],3)

#third part of four

#function that calculates average of a list
def average_list(avg):
    #finds the length of the list
    avg_div_num = len(avg)
    #sums the list
    sum_avg = sum(avg)
    #does the math
    avg = sum_avg / avg_div_num
    # returns the average
    return avg

# Passes list through avg func
avg = average_list([1,2,3])
#prints final avg
print("the avaerage of the given list is", avg)

#Final Part of lab

#10,000 rand nums
my_list2 = create_list(10000)
print("here are 10,000 random numbers: ", my_list2)

# Count elements in a list
count_list(my_list2, 1)
count_list(my_list2, 2)
count_list(my_list2, 3)
count_list(my_list2, 4)
count_list(my_list2, 5)
count_list(my_list2, 6)

# Avaerage of those 10,000 numbers
print("the average of the list containing 10,000 raadom numbers is", average_list(my_list2))