#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Catalogue all towns in the province of Como, based on the # of words in the name
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'
__version__ = 'x.x.x'


# imports
import requests
import bs4


# define the url
url = "http://www.comuni-italiani.it/013/lista.html"

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'html.parser')

towns = []
for item in soup.find_all('td'):
    if item.string == None:
        continue
    else:
        if item.string[0] in "0123456789":
            continue
        else:
            towns.append(item.string)

# trim garbage in the html parsing
towns = towns[:-11]

# variable storage
double = []
triple = []
quadruple = []

# iterate through the towns to separate the ones that have 2 or more names
for town in towns:
    if len(town.split()) == 2:
        double.append(town)
    if len(town.split()) == 3:
        triple.append(town)
    if len(town.split()) == 4:
        quadruple.append(town)
    if len(town.split()) == 5:
        quintuple.append(town)

# print results
print(len(double))
print(len(triple))
print(len(quadruple))
