# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:11:44 2021

@author: polykarpos polykarpidis
"""
#example of stochastic process (voices of corpus 1)
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
	for voice in line:
		all_char+=1
		if voice == 'G':
			counter+=1

print('len(G):', counter)
print("number_of_chars:", all_char)
print()



counter = 0
all_char = 0
for line in all_data:
	previous = [line[0]]
	for voice in line[1:]:
		all_char+=1
		if previous+[voice] == ['G','F']:
			counter+=1

print('len(G,F):', counter)
print("number_of_bigrams:", all_char)
print()



counter = 0
all_char = 0
for line in all_data:
	previous = line[0:2]
	for voice in line[2:]:
		all_char+=1
		if previous+[voice] == ['G','F','E']:
			counter+=1

print('len(G,F,E):', counter)
print("number_of_trigrams:", all_char)
