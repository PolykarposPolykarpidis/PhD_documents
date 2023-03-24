# -*- coding: utf-8 -*-
import unittest

from melodicContour import melodic_contour, simplified_pitches
from polynomial_regression import polynomial_regression

def local_peaks(piece):
	
	position_counter = 0
	max_position = len(piece)
	
	list_of_peacks = []
	
	while position_counter < max_position:
		
		if piece[position_counter] == 0:
			position_counter += 1
		elif piece[position_counter] == '+':
			
			start_point = position_counter
			
			while position_counter < max_position and piece[position_counter] != '-':
				position_counter += 1
			a_peak = position_counter
			
			if position_counter == max_position:
				end_point = position_counter-1
			else:
				while position_counter < max_position and piece[position_counter] != '+':
					position_counter += 1
				end_point = position_counter
			
			list_of_peacks.append([start_point, a_peak, end_point, "+"])
			position_counter = a_peak
		elif piece[position_counter] == '-':
			
			start_point = position_counter
			
			while position_counter < max_position and piece[position_counter] != '+':
				position_counter += 1
			a_peak = position_counter

			if position_counter == max_position:
				end_point = position_counter-1
			else:
				while position_counter < max_position and piece[position_counter] != '-':
					position_counter += 1
				end_point = position_counter
			list_of_peacks.append([start_point, a_peak, end_point, "-"])
			
			position_counter = a_peak
	list_of_peacks.pop()	#αφαιρώ την τελευταία
	return list_of_peacks



def common_peaks(piece1, piece2):
	contour_piece1 = melodic_contour(piece1)
	contour_piece2 = melodic_contour(piece2)
	
	if len(contour_piece1) != len(contour_piece1):
		print("These two pieces have not the same lenght.")
		return None
	
	peack_list_piece1 = local_peaks(contour_piece1)
	#print(peack_list_piece1)
	peack_list_piece2 = local_peaks(contour_piece2)
	#print(peack_list_piece2)
	
	same_peak_in_area = 0
	not_same_peak_in_area = 0
	for i in peack_list_piece1:
		distance = 100
		same_trigles = []
		comparison_point = []
		for j in peack_list_piece2:
			
			
			if (i[0]>=j[0] and i[2]<=j[2]) or (j[0]>=i[0] and j[2]<=i[2]):
				same_trigles.append(j)
			
			
			
		del(j)
		for j in same_trigles:
			
			if abs(i[1]-j[1]) < distance:
				distance = abs(i[1]-j[1])
				comparison_point = [j]
			elif abs(i[1]-j[1]) == distance:
				comparison_point.append(j)
			
		temp_set = set()
		for z in comparison_point:
			temp_set.add(z[3])
			
		if len(temp_set) == 1: 
			if i[3]==comparison_point[0][3]:
				same_peak_in_area += 1
				#print(i)
				#print(comparison_point)
			else:
				#print(i)
				#print(comparison_point)
				not_same_peak_in_area += 1
					
				
	print('same_peak_in_area =',same_peak_in_area,
	   '\nnot_same_peak_in_area =', not_same_peak_in_area)
	
	'''
	same_peak_in_position = 0
	not_same_peak_in_position = 0
	for i in peack_list_piece1:
		for j in peack_list_piece2:
			if i[0]<j[1] and j[1]<i[2]:
				
				
				if i[1]==j[1] and i[3]==j[3]:
					same_peak_in_position += 1
					print(i)
					print(j)
				else:
					not_same_peak_in_position += 1
	print('same_peak_in_position =',same_peak_in_position,
	   '\nnot_same_peak_in_position =', not_same_peak_in_position)
	'''
	return same_peak_in_area, not_same_peak_in_area







def common_peaks_with_regression(piece1, piece2):
	
	same_peak_in_area = 0
	not_same_peak_in_area = 0
	none_counter = 0
	
	contour_piece1 = melodic_contour(piece1)
	peack_list_piece1 = local_peaks(contour_piece1)
	
	if peack_list_piece1[0][0] == 0:
		##print('=================')
		##print(peack_list_piece1[0])
		##print('=================')
		del(peack_list_piece1[0])
	
	
	list_piece2 = simplified_pitches(piece2)
	
	##print(peack_list_piece1)
	
	
	peack_list_piece2 = []
	
	for peak in peack_list_piece1:
		
		peack_list_piece2.append(
			polynomial_regression(
				list(range(peak[0]-1, peak[2])),
				list_piece2[peak[0]-1: peak[2]]
				)
			)  

		
		
	for i, j in zip(peack_list_piece1, peack_list_piece2):
		
		if j == None:
			none_counter += 1
			continue
		
		
		if i[-1] == j:
			same_peak_in_area += 1
		else:
			not_same_peak_in_area += 1
		
			
	return same_peak_in_area, not_same_peak_in_area, none_counter









































def common_peaks_with_regression_updated(piece1, piece2):
	
	
	#print(piece1.cargo.composer, ' <||> ', piece2.cargo.composer,'\n----------------------------------------------')
	
	contour_piece1 = melodic_contour(piece1)
	contour_piece2 = melodic_contour(piece2)
	
	peack_list_piece1 = local_peaks(contour_piece1)
	peack_list_piece2 = local_peaks(contour_piece2)
	
	
	list_piece1 = simplified_pitches(piece1)
	list_piece2 = simplified_pitches(piece2)
	
	
	if peack_list_piece1[0][0] == 0:
		#print('=================')
		#print(peack_list_piece1[0])
		#print('=================')
		del(peack_list_piece1[0])
	if peack_list_piece2[0][0] == 0:
		#print('=================')
		#print(peack_list_piece2[0])
		#print('=================')
		del(peack_list_piece2[0])
	
	
	#initialisation of result's variables
	not_corresponding_triangles1 = []
	not_corresponding_triangles2 = []
	
	similar_triangles = 0
	not_similar_triangles = 0
	
	
	total_triangles = len(peack_list_piece1) + len(peack_list_piece2)
	
	while peack_list_piece1 != [] and peack_list_piece2 != []:
		
		comparison_triangles_list = []
		
		
		
		#if------------------------------------------------------------------------------------------------------------------------------
		if peack_list_piece1[0][0] < peack_list_piece2[0][0] or \
			(peack_list_piece1[0][0] == peack_list_piece2[0][0] and peack_list_piece1[0][2] > peack_list_piece2[0][2]):
			
			
			counter_embedded_triangles = 0
			
			while peack_list_piece1[0][2] >= peack_list_piece2[counter_embedded_triangles][2]:
				counter_embedded_triangles += 1
				if len(peack_list_piece2)==counter_embedded_triangles:
					break
				
			
			if counter_embedded_triangles == 0:
				not_corresponding_triangles1.append(peack_list_piece1[0])
				del(peack_list_piece1[0])
				continue
			
			
			for i in range(counter_embedded_triangles):
				comparison_triangles_list.append(peack_list_piece2[0])
				del(peack_list_piece2[0])
			
			
			x_start = comparison_triangles_list[0][0]
			x_end = comparison_triangles_list[-1][2]
			
			y = list_piece2[x_start-1:x_end]
			
			prefix = [y[0] for i in range(abs(peack_list_piece1[0][0]-x_start))]
			suffix = [y[-1] for i in range(abs(peack_list_piece1[0][2]-x_end))]
			
			y = prefix + y + suffix
			
			
			
			result = polynomial_regression(
				list(range(peack_list_piece1[0][0],peack_list_piece1[0][2]+1)),
				y)
			
			if result == peack_list_piece1[0][3]:
				similar_triangles +=1
			else:
				not_similar_triangles += 1
			
			
			
			print(peack_list_piece1[0])
			del(peack_list_piece1[0])
			
			
			
		#elif----------------------------------------------------------------------------------------------------------------------------	
		elif peack_list_piece2[0][0] < peack_list_piece1[0][0] or \
			(peack_list_piece2[0][0] == peack_list_piece1[0][0] and peack_list_piece2[0][2] > peack_list_piece1[0][2]):
			
			
			counter_embedded_triangles = 0
			
			while peack_list_piece2[0][2] >= peack_list_piece1[counter_embedded_triangles][2]:
				counter_embedded_triangles += 1
				if len(peack_list_piece1)==counter_embedded_triangles:
					break
			
			if counter_embedded_triangles == 0:
				not_corresponding_triangles2.append(peack_list_piece2[0])
				del(peack_list_piece2[0])
				continue
			
			for i in range(counter_embedded_triangles):
				comparison_triangles_list.append(peack_list_piece1[0])
				del(peack_list_piece1[0])
			
			
			
			x_start = comparison_triangles_list[0][0]
			x_end = comparison_triangles_list[-1][2]
			
			y = list_piece1[x_start-1:x_end]
			
			prefix = [y[0] for i in range(abs(peack_list_piece2[0][0]-x_start))]
			suffix = [y[-1] for i in range(abs(peack_list_piece2[0][2]-x_end))]
			
			y = prefix + y + suffix
			
			
			
			result = polynomial_regression(
				list(range(peack_list_piece2[0][0],peack_list_piece2[0][2]+1)),
				y)
			
			
			
			if result == peack_list_piece2[0][3]:
				similar_triangles += 1
			else:
				not_similar_triangles += 1
			
			
			
			print(peack_list_piece2[0])
			del(peack_list_piece2[0])
			
		#else----------------------------------------------------------------------------------------------------------------------------
		else:
			if peack_list_piece1[0][3] == peack_list_piece2[0][3]:				
				similar_triangles += 1
			else:
				not_similar_triangles += 1
			
			##print(peack_list_piece1[0])
			##print(peack_list_piece2[0])
			del(peack_list_piece1[0])
			del(peack_list_piece2[0])
		#end-if-elif-else-statement------------------------------------------------------------------------------------------------------
	##print('****************************************************\n\n\n****************************************************')
	##print('Στις λίστες παρέμειναν τα ακόλουθα')
	##print('peack_list_piece1 =', peack_list_piece1)
	##print('peack_list_piece2 =', peack_list_piece2)
	##print('****************************************************\n\n\n****************************************************')
	#print(not_corresponding_triangles1)
	#print(not_corresponding_triangles2)
	if (not 0 == len(peack_list_piece1)) or (not 0 == len(peack_list_piece1))	:
		input('Πιθανό λάθος! τσέκαρε τη λίστα!')
	return similar_triangles, not_similar_triangles, {'used_triangles': total_triangles - len(not_corresponding_triangles1) - len(not_corresponding_triangles2), 
												   'not_used_triangles': len(not_corresponding_triangles1) + len(not_corresponding_triangles2)}





#=========================================================================================================================







class TestTracker(unittest.TestCase):
	def test_the_tree_constructor(self):
		import xml_parser
		path_corpus0 = "corpus_cut\echos_d\gr_iviron1101_50r_2.xml"
		path_corpus1 = "corpus_cut\echos_d\gr_iviron1167_64r_2.xml"
		
		#path_corpus0 = "corpus_cut\echos_a\gr_iviron1101_14v_4.xml"
		#path_corpus1 = "corpus_cut\echos_a\gr_iviron1167_10r_2.xml"
		
		corpus = xml_parser.xml_parser([path_corpus0,path_corpus1])
		
		common_peaks_results = common_peaks_with_regression_updated(corpus[0], corpus[1])
		print(common_peaks_results)
		
		'''
		common_peaks_results = common_peaks_with_regression_updated(corpus[1], corpus[0])
		print(common_peaks_results)
		'''


if __name__ == '__main__':
	unittest.main()
	









