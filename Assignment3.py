##############################################
#######EXERCISE 1 30 MARKS####################
##############################################
#
#STUDENT NAME: ANDISWA MADONDO
#STUDENT NUMBER:220833593
#DATE:2025/01/28
#ASSIGNMENT 3:PYTHON
#

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

##################
## Problem 1 - 10 Points##
##################

# Given the string:
s= 'fullstackslp'

# Use indexing to print out the following:
# 'f'
print(s[0])

# 'p'
print(s[-1])

# 'stack'
print(s[4:9])

# 'slp'
print(s[9:12])

# 'cks'
print(s[7:10])

# Bonus: Use indexing to reverse the STRINGS
rev = s[::-1]
print(rev)

##############
## Problem 2 - LISTS - 5 Marks##
##############

# Using keys and indexing, grab 'hello' from the following Dictionaries:

d1 = {'simple_key':'hello'}
print(d1["simple_key"])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

###############
## Problem 4 - SETS - 4 Marks##
###############

# USe a set to find the unique values of the list below

list = [1,1,1,1,1,2,2,2,2,3,3,3,3]
#Your code here:

new_list = set(list)
print(new_list)

###############
## Problem 5 - FORMATTING - 5 Marks##
###############

# You are given the variables:

age = 45
name = "Kyle"

# Use print formatting to print the following string
# "Hello my dog's name is Kyle and he looks 45 years old"
string = "Hello my dog's name is {} and he looks {} years old".format(name,age)
print(string)
