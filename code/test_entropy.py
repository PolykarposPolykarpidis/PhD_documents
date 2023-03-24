# -*- coding: utf-8 -*-

import markov_frequency_tables as mft
import copy
#import tonoi
from itertools import product
import math
from decimal import *
getcontext().prec = 6

initial_count = 1.0 # βάζω 1.0 για να κάνω Laplace Smoothing
piece_interval = [0, 0, 0, -1, 1, -1, -2, 1, 1, 1, 0, 0, -1, 1, 1, 1, 0, 1,
			-1, -1, 1, -1, -1, 1, 1, 1, -1, 0, -1, 1, -1, -1, 0, 0, 1, 1, -1,
			-1, 0, 0, 2, -1, -2, 3, 0, 0, 0, 1, -3, 1, 1, -1, 1, 1, -1, 1,
			-1, 1, -2, 1, -2, 2, -1, -1, 1000]

piece_interval2 = [0, 0, 0, 1, 1, 0, -1, -1, -1, 2, 1, 1, -1, 0, 1, 1, -1, -1, 1,
   -1, 1, -1, -1, -1, 4, 0, 0, -1, 1, -2, 1, -3, 1, 1, 1, 0, 0, -1, -1,
   1, 1, -1, -1, -1, 2, 1, 1, 1, -1, -1, -1, 2, -1, -1, 0, 0, 1, -3, 1,
   1, 0, -1, 0, -1, 0, 1000, 0, 0 , 0]



markov_corpora = dict()
markov_corpora['corpus1'] = mft.dynamic_transition_matrix(piece_interval, order=1)
markov_corpora['corpus2'] = mft.dynamic_transition_matrix(piece_interval2, order=1)
	
	
markov_corpora_same_set = dict()
markov_corpora_same_set['corpus1'] = None
markov_corpora_same_set['corpus2'] = None	



def cross_entropy_and_KL_divergence(m1, m2):
	total_sum_cross_entropy = 0.0
	total_sum_KL_divergence = 0.0
	for index in m1.index:
		for column in m1.columns:
			total_sum_cross_entropy += m1[column][index]* math.log(m2[column][index],2)
			total_sum_KL_divergence += m1[column][index]* math.log(m1[column][index]/m2[column][index],2)
	return (total_sum_cross_entropy * (-1), total_sum_KL_divergence)




print('========================================================================')

for pos, (k, v) in enumerate(markov_corpora.items()):
		
	temp = copy.deepcopy(list(markov_corpora.values()))
		
	del(temp[pos])
	for each_markov_d in temp:
			
			
		#Εδώ προσθέτω τις γραμμές και τις στήλες που δεν υπάρχουν σε κάθε corpus προκειμένου να κάνω smoothing
		for i in each_markov_d.columns.difference(v.columns):
			v[i] = [initial_count for j in range(len(v))]
			v = v.sort_index(axis=1)
				
				
		for i in each_markov_d.index.difference(v.index):
			v.loc[i] = [initial_count for j in range(v.shape[1])]
			v = v.sort_index(ascending=True)

		

		total = v.sum()
		for element in v.columns:
			v[element] = v.div(total[element])[element]
			
	markov_corpora_same_set[k] = copy.deepcopy(v)
	

print('========================================================================')

entropy_file = open('cross-entropy and kld.txt', 'a', encoding='utf-8')
temp_list = list(markov_corpora_same_set)
c_product = list(product(temp_list,temp_list))

for i in c_product:
	if i[0] == i[1]:
		continue
	print(i[0])
	print(markov_corpora_same_set[i[0]])
	print()
	print(i[1])
	print(markov_corpora_same_set[i[1]])
	print('\n\n========================================================================')
	cross_entropy, KL_divergence = cross_entropy_and_KL_divergence(markov_corpora_same_set[i[0]], markov_corpora_same_set[i[1]])



	#print('cross_entropy '+str(i)+'=', cross_entropy)
	print('KL_divergence'+str(i)+' =',KL_divergence)














