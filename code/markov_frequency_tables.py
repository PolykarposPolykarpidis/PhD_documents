# -*- coding: utf-8 -*-
import unittest
import pandas as pd

pd.set_option('display.precision', 3)


initial_count = 1.0 # βάζω 1.0 για να κάνω Laplace Smoothing
''''''
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def add_an_column(df, column_name):
	df[column_name] = list([initial_count for i in range(len(df))]) #πρόσθεσα τον type cast list
	df = df.sort_index(axis=1)
	return df


def add_an_index(df, index_name):
	df.loc[index_name] = list([initial_count for i in range(df.shape[1])]) #πρόσθεσα τον type cast list
	df = df.sort_index(ascending=True)
	return df


def dynamic_transition_matrix(data, order=1):
	
	if type(order) != int:
		raise TypeError('The order type must be int.') 
	if order<1:
		raise ValueError('The order value must be greater than 0.')
	if len(data) <= order:
		raise ValueError('The lenght of sequence of data must be greater than the order.')
	
	
	matrix = pd.DataFrame(
		[[initial_count],],
		index=[data[order+1]],
		columns= [tuple(data[:order])],
		dtype=float
		)
	
	
	for element in range(order,len(data)):	

		if data[element] not in matrix.index:
			matrix = add_an_index(matrix, data[element])
		
		if tuple(data[element-order:element]) not in matrix.columns:
			matrix = add_an_column(matrix, tuple(data[element-order:element]))

		matrix[tuple(data[element-order:element])][data[element]] += 1.0
	
	
	return matrix




















class TestTracker(unittest.TestCase):
	def test_markov_interval(self):
		
		#prepare the value for testing
		import numpy
		indexes = [-3,-2,-1,0,1,2,3,1000]
		columns_ = [(-3,) ,(-2,),  (-1,),  (0,),  (1,),  (2,),  (3,)]
		results = numpy.array(
			[
	[1.0,1.0,1.0,1.0,2.0,1.0,1.0],
	[1.0,1.0,3.0,1.0,3.0,1.0,1.0],
	[1.0,1.0,6.0,4.0,10.0,3.0,1.0],
	[1.0,1.0,4.0,8.0,3.0,1.0,2.0],
	[2.0,3.0,9.0,4.0,10.0,1.0,1.0],
	[1.0,2.0,1.0,2.0,1.0,1.0,1.0],
	[1.0,2.0,1.0,1.0,1.0,1.0,1.0],
	[1.0,1.0,2.0,1.0,1.0,1.0,1.0]
	]
	)
		results_of_piece_interval = pd.DataFrame(results, index=indexes, columns=columns_)
		
		
		
		
		#import some data
		piece_interval = [0, 0, 0, -1, 1, -1, -2, 1, 1, 1, 0, 0, -1, 1, 1, 1, 0, 1,
					-1, -1, 1, -1, -1, 1, 1, 1, -1, 0, -1, 1, -1, -1, 0, 0, 1, 1, -1,
					-1, 0, 0, 2, -1, -2, 3, 0, 0, 0, 1, -3, 1, 1, -1, 1, 1, -1, 1,
					-1, 1, -2, 1, -2, 2, -1, -1, 1000]
		test = dynamic_transition_matrix(piece_interval, 1)
		
		
		#test the data
		self.assertEqual(test.equals(results_of_piece_interval), True)

		


		piece_interval2 = [0, 0, 0, 1, 1, 0, -1, -1, -1, 2, 1, 1, -1, 0, 1, 1, -1, -1, 1,
		   -1, 1, -1, -1, -1, 4, 0, 0, -1, 1, -2, 1, -3, 1, 1, 1, 0, 0, -1, -1,
		   1, 1, -1, -1, -1, 2, 1, 1, 1, -1, -1, -1, 2, -1, -1, 0, 0, 1, -3, 1,
		   1, 0, -1, 0, -1, 0, 1000]
		test2 = dynamic_transition_matrix(piece_interval2, 1)
		print(test2)



if __name__ == '__main__':
	unittest.main()

