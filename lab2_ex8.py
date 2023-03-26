# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 22:42:37 2023

@author: Admin
"""
import nltk
import re
 
try:
    file = open('C:/Users/Admin/Downloads/message.txt')
    for line in file:
        line = line.strip()
        emails = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+\.[0-9a-zA-z]+", line)
        if(len(emails) > 0):
            print(emails)
 
except FileNotFoundError as e:
    print(e)