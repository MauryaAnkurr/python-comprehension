

#Creating a list is as simple as putting different comma-separated values between square brackets. For example −

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]

#************************************************************
#BASIC SYNTAX:
#[ expression for item in list if conditional ]

#IS EQUIVALENT TO:
#for item in list:
#    if conditional:
#        expression

#************************************************************
#Another example
#new_list = []
#for i in old_list:
    #if filter(i):
        #new_list.append(expressions(i))

#List comprehension view .IS EQUIVALENT TO.
#new_list = [expression(i) for i in old_list if filter(i)]

#*************************************************************
#Breaking of the statement.How it works  
# new_list = [expression(i) for i in old_list if filter(i)]
#1 .new_list    
#2 .The new list (result).
#expression(i)
#Expression is based on the variable used for each element in the old list.

#for i in old_list
#The word for followed by the variable name to use, followed by the word in the
#old list.

#if filter(i)
#Apply a filter with an If-statement.
#*************************************************************
