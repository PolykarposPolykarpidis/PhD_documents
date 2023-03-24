# -*- coding: utf-8 -*-
import xml_parser
from collections import Counter
import pandas as pd



DELIMITER = '  '


def to_string(a_list): #Becareful the delimiter is a two spaces, so two characters!
	temp_str = ''
	for i in a_list:
		temp_str += str(i) + DELIMITER
	return temp_str[:-len(DELIMITER)]


def get_syllable_intervals(syllable):
	intervals = []
	for leaf in syllable:
		intervals.extend(leaf.cargo.interval)
	return to_string(intervals)

def get_syllable_pitches(syllable):
	return to_string(syllable.pitch)

def get_syllable_voiced_id(syllable):
	user_id = []
	for leaf in syllable:
		temp = leaf.cargo.user_value[-1]
		if -1 != temp.find('kk'):
			temp = temp.replace('kk', DELIMITER +'kk'+ DELIMITER)
			
		if DELIMITER == temp[0:2]:
			temp = temp[2:]
		
		if DELIMITER == temp[-2:]:
			temp = temp[:-2]

		user_id.append(temp)
	return to_string(user_id)


def find_tonoi(list_addresses, viewpoint):
	parsered_corpus = xml_parser.xml_parser(list_addresses)
	list_of_tonoi = []
	for piece in parsered_corpus:
		for phrase_or_martyria in piece:
			if phrase_or_martyria.cargo == 'martyria':
				continue
			for syllable in phrase_or_martyria:
				if "interval" == viewpoint:
					list_of_tonoi.append(get_syllable_intervals(syllable))
				if "pitch" == viewpoint:
					list_of_tonoi.append(get_syllable_pitches(syllable))
				if "voice_id" == viewpoint:
					list_of_tonoi.append(get_syllable_voiced_id(syllable))
	
	return list_of_tonoi








def tonoi_freq_by_words_num(tonoi_dataFrame):
	dataFrame_freq_by_words_num = pd.DataFrame(index= ['count', 'frequency', 'relative_frequency', 'relative_frequency %'], columns=['Total'])

	
	for an_index in tonoi_dataFrame.index:
		splited_index = an_index.split(DELIMITER)
		
		
		if not len(splited_index) in dataFrame_freq_by_words_num:
			dataFrame_freq_by_words_num.insert(0, len(splited_index), list([0.0 for i in dataFrame_freq_by_words_num.index])) 

		
		dataFrame_freq_by_words_num.at['count',len(splited_index)] += 1.0
		dataFrame_freq_by_words_num.at['frequency',len(splited_index)] += tonoi_dataFrame.at[an_index,'frequency']
	
	dataFrame_freq_by_words_num.at['count','Total'] = dataFrame_freq_by_words_num.loc['count'].sum(axis=0)
	dataFrame_freq_by_words_num.at['frequency','Total'] = dataFrame_freq_by_words_num.loc['frequency'].sum(axis=0)
	
	
	for a_column in dataFrame_freq_by_words_num.columns:
		dataFrame_freq_by_words_num.at['relative_frequency', a_column] = dataFrame_freq_by_words_num.at['frequency', a_column] / dataFrame_freq_by_words_num.at['frequency', 'Total']
		dataFrame_freq_by_words_num.at['relative_frequency %', a_column] = dataFrame_freq_by_words_num.at['relative_frequency', a_column] * 100
		dataFrame_freq_by_words_num = dataFrame_freq_by_words_num.reindex(sorted(dataFrame_freq_by_words_num.columns[:-1])+[dataFrame_freq_by_words_num.columns[-1]], axis=1)
	return dataFrame_freq_by_words_num







def find_melismaticity(tonoi_stats):
	melismaticity = 0.0
	
	for tonoi_num in tonoi_stats.columns:
		if str(tonoi_num).isnumeric():
			melismaticity += tonoi_stats.at['relative_frequency', tonoi_num] * float(tonoi_num)
	
	
	return melismaticity








def find_tonoi_frequency(list_addresses, viewpoint):
	tonoi_list = find_tonoi(list_addresses, viewpoint)
	tonoi_frequency = dict(Counter(tonoi_list))
	tonoi_dataFrame = pd.DataFrame(tonoi_frequency.values(),  tonoi_frequency.keys(), columns=['frequency'])
	total_syllables = tonoi_dataFrame['frequency'].sum()
	
	
	list_of_frequencies = []
	frequencies = tonoi_dataFrame["frequency"].to_numpy()
	for frequency in frequencies:
		list_of_frequencies.append(frequency/total_syllables)
	tonoi_dataFrame['relative_frequency'] = list_of_frequencies
	
	tonoi_dataFrame = tonoi_dataFrame.sort_values(by = ['frequency'], ascending = [False])
	
	
	
	tonoi_stats = tonoi_freq_by_words_num(tonoi_dataFrame)
	melismaticity = find_melismaticity(tonoi_stats)
	print(tonoi_stats)
	print('total_syllables =', total_syllables)
	print('\n\n')
	return tonoi_dataFrame, tonoi_stats, melismaticity




















