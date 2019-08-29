

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
# [<the_expression> for <the_element> in <the_iterable> if <the_condition>]
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
(values) = [ (expression) for (item) in (collection) ]
The above list comprehension is equivalent to the following plain for-loop:

(values) = []
for (item) in (collection):
    (values).append( (expression) )
#*************************************************************
    
#Nested Conditionals
With a Python list comprehension, it doesn’t have to be a single condition; you can nest conditions. 
Here’s an example.

[i for i in range(8) if i%2==0 if i%3==0]
[0, 6]
Let’s see how this works. 
1. For integers 0 to 7, it first filters out the elements that aren’t perfectly divisible by 
2. For the remaining elements, it keeps only those that are divisible by 
3. Finally, it stores these elements in a list, and prints it out.
Remember, this is a nested conditional, not an AND operation of two conditions.
#*************************************************************
list1=[1,2,3,4]
#print([i for i in list1 if i%2==0] )

non_flat = [ [1,2,3], [4,5,6], [7,8] ]
print([x for x in non_flat])

print([y for x in non_flat for y in x])

print([y for x in non_flat for y in x if y%2==0] )

#*************************************************************
