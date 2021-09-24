# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:11:44 2021

@author: polykarpos polykarpidis
"""
#example of information content
all_data = [["a","G","F","E","F","G","a","b","a","G","G","F","F","E","G"],
		["G","F","E","F","G","a","b","a","G","G","F","F","E","G"],
		["G","F","E","F","G","a","b","a","G","G","F","F","E","G"],
		["G","F","E","F","G","a","G","G","F","F","E","G"],
		["G","F","E","F","G","a","G","G","F","F","E","G"],
		["G","F","E","F","G","a","G","G","F","F","E","G"],
		["G","F","E","F","G","a","G","G","F","F","E","G"],
		["G","F","F","G","a","G","G","F","F","E","G"],
		["G","F","F","G","a","G","G","F","F","E","G"],
		["G","F","F","G","a","G","G","F","F","E","G"],
		["G","F","F","G","a","G","G","F","F","E","G"],
		["G","F","E","F","G","a","G","G","F","G"],
		["G","F","G","a","G","G","F","F","E","G"],
		["G","G","F","G","a","G","G","F","G"],
		["G","F","E","F","G","a","F","F","G"],
		["F","E","F","G","a","G","E","G"],
		["G","F","G","a","F","F","G"]]


counter = 0
all_char = 0
for line in all_data:
	previous = [line[0]]
	for voice in line[1:]:
		all_char+=1
		print(previous+[voice])
		if previous+[voice] == ['b','a']:
			counter+=1
		previous = [voice]
		
		
		
print('len(b,a):', counter)
print("number_of_bigrams:", all_char)
print()
