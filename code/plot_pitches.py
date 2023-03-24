# -*- coding: utf-8 -*-
import phrase
import numpy as np
from byzTree import getPosPitchList
import matplotlib.pyplot as plt
from abcd import pitch_list



def plot_lines(corpora, scalar_of_pieces, pieces_label, title='', figure_path='', simplified = False):
	
	
	list_of_pieces = dict()
	
	for piece in corpora:
		list_of_pieces[piece.cargo.composer] = [getPosPitchList(piece.child.pitch[-1])]
	
	t = dict()
	for k, v in list_of_pieces.items():
		t[k] = [0.0]
	
	
	for piece in corpora:
		temp_t = 0.0
		temp_composer = piece.cargo.composer
		for each_child in piece:
			if type(each_child.cargo) == phrase.Phrase:
				for each_syllable in each_child:
					if simplified == True:
						pitch_len = 1
						list_of_pieces[temp_composer].append(getPosPitchList(each_syllable.pitch[-1]))
					else:
						pitch_len = len(each_syllable.pitch)
						for i in each_syllable.pitch:
							list_of_pieces[temp_composer].append(getPosPitchList(i))
					
					
					temp_step = 1/pitch_len
					for i in range(pitch_len):
						temp_t += temp_step
						t[temp_composer].append(temp_t)
	
	
	
	
	
	list_of_piece_np_array = dict()
	list_of_t_np_array = dict()
	
	for k,v in list_of_pieces.items():
		if scalar_of_pieces.get(k) == None:
			list_of_piece_np_array[k] = np.array(v)
		else:
			list_of_piece_np_array[k] = np.array(v) + scalar_of_pieces[k]
		
	for k, v in list_of_pieces.items():
		list_of_t_np_array[k] = np.array(t[k])
		
	

	
	plt.rcParams['figure.figsize'] = (25,6)
	
	
	
	
	plt.subplots()
	
	ax = plt.gca()
	for k in list_of_pieces.keys():
		color = next(ax._get_lines.prop_cycler)['color']
		plt.plot(list_of_t_np_array[k], list_of_piece_np_array[k], marker='o', color = color,  linewidth=1, label=k)
		
		mean_list_of_piece_np_array = list_of_piece_np_array[k].mean()
		plt.plot(list_of_t_np_array[k], [mean_list_of_piece_np_array for i in range(len(list_of_t_np_array[k]))], linestyle='--', color = color, label='mean '+ k)
		
	

	#####
	plt.title(title)
	plt.legend()
	plt.tight_layout()
	

	range_of_syllables = np.arange(0, max([v[-1] for k, v in list_of_t_np_array.items()])+1, 1)
	
	plt.xticks(range_of_syllables)
	
	
	
	yticks_ = []
	
	
		
	range_of_pitches = np.arange(min([int(v.min()) for v in list_of_piece_np_array.values()]), max([int(v.max()) for v in list_of_piece_np_array.values()])+1,1)
	
	
	for i in range_of_pitches:
		yticks_.append(pitch_list[i])
	plt.yticks(range_of_pitches, yticks_)
	plt.grid(True)
	
	string = ''
	for i in pieces_label:
		string+= i
		string+= ' - '

	plt.savefig(figure_path+'/'+string[:-3]+'.png', bbox_inches='tight', dpi=600)
	
	plt.show()
	
	'''
	with open('echos_a_simplified_plot_x_y.txt', 'a') as f:
		f.write(str(ax.get_lines()[0].get_data()))
		f.write('\n\n-------------------------------------------------------------------------\n\n')
		f.write(str(ax.get_lines()[2].get_data()))
		f.write('\n\n-------------------------------------------------------------------------\n\n')
		f.write(str(ax.get_lines()[4].get_data()))
		f.write('\n\n-------------------------------------------------------------------------\n\n')
		f.write('\n\n=========================================================================\n\n')
	'''
	
	
	plt.clf()
	plt.close()













































	


	