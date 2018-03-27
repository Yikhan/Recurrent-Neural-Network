# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:31:24 2017

@author: XPS-12
"""


words = []
with open('stop-words-small.txt','r') as f:
    for line in f.readlines():
        words.append(line.strip())
        
print(words)