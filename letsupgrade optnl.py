# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 16:43:36 2021

@author: User
"""

# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	
print(lst)
