# -*- coding: utf-8 -*-
import pandas as pd

def transition_matrix_order1(data):
    alphabet = []
    for element in data:
        if element not in alphabet:
            alphabet.append(element)
    alphabet.sort()
    
    previous = data[0]
    matrix = pd.DataFrame(0.0, index=alphabet, columns=alphabet)
    
    for i in data[1:]:
        matrix[i][previous]    += 1.0
        previous = i
    
    total = matrix.sum()
    for element in alphabet:
        matrix[element] = matrix.div(total[element])[element]
    
    return matrix, alphabet


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



markov_matrix = pd.DataFrame(0.0, index=["E","F","G","a","b"], columns=["E","F","G","a","b"])
#create markov transition matrix order 1 (bigram)
for data in all_data:
	temp, _ = transition_matrix_order1(data)
	markov_matrix = markov_matrix.add(temp,  fill_value=0)


print(markov_matrix.div(len(all_data)))



