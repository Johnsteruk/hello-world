#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:11:57 2020

@author: john
"""

def encrypt(text,s):
    result=""
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65 )
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
    return result

text = "Ceasar CIPHER Demo"
s = 4
print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher: " + encrypt(text,s))
