#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brilliant

4.1 Programming and CS

n-gram model


@author: marek

Created: 2024.10.31
Modified: 2024.10.31
"""

filename = 'data/jekyll.txt'
reader = open(filename)

# reader is a file object, it doesn't print the text
# A file object is a special Python data type for accessing
# and manipulating files stroed on a computer or a server.
# print(reader)

# file objects provide the method ```readlines()``` that returns a **list**
lines = reader.readlines()

print(lines[:7])
