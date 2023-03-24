# -*- coding: utf-8 -*-
import tree
import metadata
import phrase
import voiceless
import pandas as pd
import abcd
import os



BLANK = " "
CONTINUE = "-"

def find_voiceless(each_vv, continue_list):
	temp = []
	i = 0
	while each_vv.voiceless.bitmap >= 2**i:
		if each_vv.voiceless.bitmap & 2**i != 0:
			voiceless_user_value = voiceless.getUserValueByUid(2**i)
			if voiceless_user_value in continue_list:
				temp.append(voiceless_user_value+CONTINUE)
				continue_list.remove(voiceless_user_value)
			else:
				temp.append(voiceless_user_value)	
		i += 1
	
	
	
	i = 0
	while each_vv.continue_.bitmap >= 2**i:
		if each_vv.continue_.bitmap & 2**i != 0:
			continue_list.append(voiceless.getUserValueByUid(2**i))
		i += 1
	return continue_list , temp







def find_vv_phrase(each_vv, continue_list):
	a_voiced_voiceless = []
	vv = dict()
	vv['voiced'] = each_vv.cargo.user_value[-1]
	
	temp_pitch_string = ''
	for a_pitch in each_vv.pitch:
		temp_pitch_string += a_pitch
	vv['pitch'] = temp_pitch_string
	
	continue_list , voiceless_list = find_voiceless(each_vv, continue_list)
	
	vv['voiceless'] = voiceless_list
	
	a_voiced_voiceless.append(vv)
	
	return continue_list, a_voiced_voiceless
	


def musical_phrase(a_phrase):
	list_of_syllables_with_vv = []
	
	continue_list = []
	for each_syllable in a_phrase:
		temp_dict = dict()
		voiced_voiceless_list = []
		temp_end_word = abcd.punctuation['end_word'] if each_syllable.cargo.end_word == True else ''
		temp_dict["syllable"] = each_syllable.cargo.syllable + temp_end_word
		
		for each_vv in each_syllable:
			continue_list, a_voiced_voiceless = find_vv_phrase(each_vv, continue_list)
			voiced_voiceless_list.extend(a_voiced_voiceless)
		
		
		
		temp_dict["voiced_voiceless_list"] = voiced_voiceless_list
		
		
		
		list_of_syllables_with_vv.append(temp_dict)
	return list_of_syllables_with_vv














def martyria_phrase(a_voiced, continue_list):
	temp_dict = dict()
	temp_dict["voiced"] = a_voiced.cargo.user_value[-1]
	
	temp = []
	i = 0
	while a_voiced.voiceless.bitmap >= 2**i:
		if a_voiced.voiceless.bitmap & 2**i != 0:
			voiceless_user_value = voiceless.getUserValueByUid(2**i)
			if voiceless_user_value in continue_list:
				temp.append(voiceless_user_value+CONTINUE)
				continue_list.remove(voiceless_user_value)
			else:
				temp.append(voiceless_user_value)	
		i += 1
	temp_dict["voiceless"] = temp
	
	del temp
	
	
	i = 0
	while a_voiced.continue_.bitmap >= 2**i:
		if a_voiced.continue_.bitmap & 2**i != 0:
			continue_list.append(voiceless.getUserValueByUid(2**i))
		i += 1
	return continue_list, temp_dict






def martyria(a_martyria):
	line = dict()
	for item in a_martyria:
		line['pitch'] =  item.pitch
		line['echos'] = item.cargo.echos
		voiced_voiceless_list = []
		continue_list = []
		for voiced_sign in item:
			voiced_voiceless = []
			
			continue_list, voiced_voiceless = martyria_phrase(voiced_sign, continue_list)
			voiced_voiceless_list.append(voiced_voiceless)
		line['voiced_voiceless_list'] = voiced_voiceless_list
	return line


def check_input(piece):
	if type(piece) == tree.Node and type(piece.cargo) == metadata.meta:
		return True
	elif type(piece) == list:
		for item in piece:
			if type(item) == tree.Node and (type(item.cargo) == phrase.Phrase or item.cargo == "martyria"):
				return True
	else:
		return False




def visualize(piece):
	if not check_input(piece):
		print('input_type =', type(piece))
		raise TypeError("Δέχεται είτε το Head-node ενός κομματιού είτε ένα list από phrases και martyria")
	temp_list = []
	for item in piece:
		
		if type(item.cargo) == phrase.Phrase:
			temp_list.append(musical_phrase(item))
			pass
		else:
			temp_list.append(martyria(item))
	
	#print(temp_list)
	
	
	
	x = 0
	while os.path.isfile('./visualization'+str(x)+'.csv') == True:
		x += 1
		
	
	
	
	with open('visualization'+str(x)+'.csv', 'w', encoding="utf-8-sig") as f:
		for line in temp_list:
			if type(line) == dict:
				if 'echos' in line.keys():
					f.write(line['echos'])
					for each_pitch in line['pitch']:
						f.write(',' + each_pitch)
					f.write('\n')
					
					
					
					len_column = len(line['voiced_voiceless_list'])
					
					
					len_row = 0
					for each_voiceless in line['voiced_voiceless_list']:
						if len(each_voiceless['voiceless']) > len_row:
							len_row = len(each_voiceless)
					len_row += 1
					
					
					temp = pd.DataFrame(data=BLANK, index=range(len_row), columns=range(len_column), dtype=str)
					
					for pos, each_vv in enumerate(line['voiced_voiceless_list']):
						temp[pos][0] = each_vv['voiced']
						for each_voiceless in each_vv['voiceless']:
							for j in range(len_row-1):
								
								if each_voiceless[-1] == '-':
									
									for z in range(len_column):
										if temp[pos-1][z] == each_voiceless[:-1]:
											break
										
									temp[pos][z] = each_voiceless
									break
								
								elif temp[pos][j+1] == BLANK:
									temp[pos][j+1] = each_voiceless
									break
					
					
					for x in temp.values:
						for y in x:
							f.write(y + ',')
						f.write('\n')
					del temp
			else:
				#θα πάει εδώ αν πρέπει να περάσει φράση, όχι μαρτυρία.
				len_column = 0
				
				len_row = 0
				
				for each_syllable in line:
					len_column += len(each_syllable['voiced_voiceless_list'])
					for each_voiced in each_syllable['voiced_voiceless_list']:
						if len(each_voiced['voiceless']) > len_row:
							len_row = len(each_voiced['voiceless'])
				len_row += 3
				
				#print('len_column =', len_column, "len_row =", len_row)
				
				temp = pd.DataFrame(data=BLANK, index=range(len_row), columns=range(len_column), dtype=str)
				
				j1 = 0
				for each_syllable in line:
					j2 = len(each_syllable['voiced_voiceless_list'])
					temp[j1][2] = each_syllable['syllable']
					
					
					for i in range(j1+1,j1+j2):
						
						temp[i][2] = CONTINUE
					
					
					
					
					for pos, vv in enumerate(each_syllable['voiced_voiceless_list']):
						temp[j1+pos][0] = each_syllable['voiced_voiceless_list'][pos]['pitch']
						temp[j1+pos][1] = each_syllable['voiced_voiceless_list'][pos]['voiced']
						
						for each_voiceless in vv['voiceless']:
							if each_voiceless[-1] == CONTINUE:
								for z in range(3, len_row):
									
									
									if temp[j1+pos-1][z] == each_voiceless[:-1]:
										temp[j1+pos][z] = CONTINUE
										break
								
							else:
								for z in range(3, len_row):
									if temp[j1+pos][z] == BLANK:
										temp[j1+pos][z] = each_voiceless
										break
								
					
					j1 += j2
					
				
				
				for x in temp.values:
					for y in x:
						f.write(y + ',')
					f.write('\n')
				del temp
				
				
				
				
			f.write('\n\n')
					
				
	return True



























