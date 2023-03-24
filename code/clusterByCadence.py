# -*- coding: utf-8 -*-
import phrase
from byzTree import getPosPitchList

def find_cadence_pitch(comparison_phrase):
	last_syllable = None
	
	for i in comparison_phrase:
		last_syllable = i
	
	return last_syllable.child.pitch[-1]


def nearest_to_cadence_pitch(syllable_pitch_list, cadence_pitch):
	distance = 100
	nearest_pitch = None
	
	for pitch in syllable_pitch_list:
		tested_distance = getPosPitchList(pitch)-getPosPitchList(cadence_pitch)
		if tested_distance < distance:
			distance = tested_distance
			nearest_pitch = pitch
					
	return nearest_pitch






def compare_phrases(comparison_phrase, phr, threshold):
	edit_distance = 0
	
	cadence_pitch = find_cadence_pitch(comparison_phrase)
	
	comparison_pitch_list = []
	omit = len(comparison_phrase)-threshold
	for i in comparison_phrase:
		if omit != 0:
			omit -= 1
		else:
			comparison_pitch_list.append(i.pitch)
	
	phr_pitch_list = []
	omit = len(phr)-threshold
	for i in phr:
		if omit != 0:
			omit -= 1
		else:
			phr_pitch_list.append(i.pitch)
	
	
	for i in range(threshold):
		comparison_pitch = nearest_to_cadence_pitch(comparison_pitch_list[i], cadence_pitch)
		test_pitch = nearest_to_cadence_pitch(phr_pitch_list[i], cadence_pitch)
		
		if comparison_pitch != test_pitch:
			edit_distance += 1
			
		
	return edit_distance










def sp(a_corpus, threshold = 6, edit_distance_threshold = 1):
	corpus_phrases_temp = []
	for piece in a_corpus:
		corpus_phrases_temp.extend(piece.getPhrasesNodes_list())
	
	#Αφαιρεί από τη λίστα όλες τις φράσεις που το πλήθος των συλλαβών είναι λιγότερο από το threshold
	corpus_phrases = []
	for phr in corpus_phrases_temp:
		if len(phr) >= threshold:
			corpus_phrases.append(phr)
	del(corpus_phrases_temp)
	
	
	#Ελέγχει αν υπάρχει τουλάχιστον δύο φράση που να έχουν πλήθος συλλαβών μεγάλυτερο από το threshold
	if len(corpus_phrases) < 2:
		print('Δεν υπάρχουν περισσότερες από 2 φράσεις που να έχουν περισσότερες συλλαβές από το threshold')
		return None
	
	
	
	class_id = 1
	comparison_phrase = corpus_phrases.pop()
	comparison_phrase.cargo.class_id = class_id
	
	while True:
		for phr in corpus_phrases:
			
			edit_distance = compare_phrases(comparison_phrase, phr, threshold)
			
			if phr.cargo.edit_distance > edit_distance and edit_distance <= edit_distance_threshold:
				phr.cargo.edit_distance = edit_distance
				phr.cargo.class_id = comparison_phrase.cargo.class_id
				
			
		if corpus_phrases != []:
			comparison_phrase = corpus_phrases.pop()
			if comparison_phrase.cargo.class_id == -1:
				class_id += 1
				comparison_phrase.cargo.class_id = class_id
			comparison_phrase.cargo.edit_distance = 100
		else:
			break
	
	
	
	
	
	
	
	#===========================================================
	'''
	Δεν είναι μέρος του αλγορίθμου.
	Απλά τυπώνει τις φράσεις ταξινομημένες κατά class_id.
	Αυτό το κομμάτι μπορεί να αφαιρεθεί.
	'''
	temp = []
	for piece in a_corpus:
		temp.extend(piece.getPhrasesNodes_list())
		
	sorted_list = sorted(temp, key=lambda x: x.cargo.class_id)
	for i in sorted_list:
		print(i)
	#=========================================================
	
	
	
	
	
	return sorted_list