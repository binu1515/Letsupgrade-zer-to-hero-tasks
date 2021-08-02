# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:50:20 2021

@author: User
"""

## importing string module
import string
## function to check for the panagram
def is_panagram(string, alphabets):
   ## looping over the alphabets
   for char in alphabets:
      ## if char is not present in string
      if char not in string.lower():
         ## returning false
         return False
   return True
## initializing alphabets variable
alphabets = string.ascii_lowercase
## initializing strings
string_one = "The Quick Brown Fox Jumps Over The Lazy Dog"
string_two = "TutorialsPoint TutorialsPoint"
print("Panagram") if is_panagram(string_one, alphabets) else print("Not Panagram")
print("Panagram") if is_panagram(string_two, alphabets) else print("Not Panagram")