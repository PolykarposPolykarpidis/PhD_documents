# -*- coding: utf-8 -*-
def find_melismaticity_in_list_of_pieces(corpus):
	list_melismaticity_average = []
	#list_num_of_syllables = []
	list_num_pitch = []
	
	for pos, piece in enumerate(corpus):
		temp_melismaticity_average, temp_num_of_syllables, temp_pitch_list = find_melismaticity(piece)
		
		list_melismaticity_average.append(temp_melismaticity_average)
		
		list_num_pitch.extend(temp_pitch_list)
		
	return (sum(list_melismaticity_average)/len(corpus), list_melismaticity_average, list_num_pitch)
	
	
	




	
def find_melismaticity(a_piece):
	num_of_syllables = 0
	list_of_pitches = []

	for children in a_piece:

		if 'martyria' == children.cargo:
			continue
			
		for syllable in children:
			num_of_syllables += 1
			list_of_pitches.append(len(syllable.pitch))
	
	
	return (sum(list_of_pitches)/num_of_syllables, num_of_syllables, list_of_pitches)










		
			






