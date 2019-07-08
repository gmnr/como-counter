#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Catalogue all towns in the province of Como, based on the # of words in the name
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'
__version__ = '0.1.0'


# imports
import requests
import bs4
from string import digits
from random import sample

# define the url
url = "http://www.comuni-italiani.it/013/lista.html"

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'html.parser')

towns = []
for item in soup.find_all('td'):
    if item.string == None:
        continue
    else:
        if item.string[0] in digits:
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
print('=' * 120)
print(f'The province of Como has {len(towns)} towns\n')
print(f"There are {len(towns) - len(double) - len(triple) - len(quadruple)} town's names that are composed by 1 word\n")
print(f"{len(double)} that are composed by 2 words such as -->  {', '.join(sample(double, 4))}")
print(f"{len(triple)} that are composed by 3 words such as -->  {', '.join(sample(triple, 4))}")
print(f"{len(quadruple)} that are composed by 4 words and those are -->  {', '.join(sample(quadruple, 4))}\n")
print('=' * 120)
