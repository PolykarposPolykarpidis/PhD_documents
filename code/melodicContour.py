# -*- coding: utf-8 -*-
import phrase
from byzTree import getPosPitchList





def melodic_contour(piece):
	
	piece_contour = []
	
	for p1 in piece:
		if type(p1.cargo) != phrase.Phrase:
			continue
		
		for each_syllable in p1:
			
			
			ultimate_interval = 0
			for each_sign in each_syllable:
				ultimate_interval += sum(each_sign.cargo.interval)
			
			
			if ultimate_interval == 0:
				piece_contour.append(ultimate_interval)
			elif ultimate_interval > 0:
				piece_contour.append('+')
			elif ultimate_interval < 0:
				piece_contour.append('-')
			else:
				raise ValueError("Περίεργη τιμή στο ultimate_interval")
	return piece_contour




def measure_melodic_contour(piece1, piece2):
	
	similar = 0
	not_similar = 0
	piece1_contour = melodic_contour(piece1)
	piece2_contour = melodic_contour(piece2)

	if len(piece1_contour) == len(piece2_contour):
		for pc1, pc2 in zip(piece1_contour, piece2_contour):
			if pc1 == pc2:
				similar += 1
			else:
				not_similar += 1
		return [similar, not_similar]
	else:
		print('These two pieces have no the same lenght!')
		return None
			
			



	
def melodic_intervals(piece):
	
	piece_melodic_interval = []
	
	for p1 in piece:
		if type(p1.cargo) != phrase.Phrase:
			continue
		
		for each_syllable in p1:
			
			
			ultimate_interval = 0
			for each_sign in each_syllable:
				ultimate_interval += sum(each_sign.cargo.interval)
			

			piece_melodic_interval.append(ultimate_interval)
	return piece_melodic_interval




def measure_melodic_intervals(piece1, piece2):
	
	similar = 0
	not_similar = 0
	piece1_intervals = melodic_intervals(piece1)
	piece2_intervals = melodic_intervals(piece2)

	if len(piece1_intervals) == len(piece2_intervals):
		for pc1, pc2 in zip(piece1_intervals, piece2_intervals):
			if pc1 == pc2:
				similar += 1
			else:
				not_similar += 1
		return [similar, not_similar]
	else:
		print('These two pieces have no the same lenght!')
		return None		
			
			
			
	
	
	
	
def simplified_pitches(piece): #άλλαξα το όνομα αυτής της συνάρτησης από ultimate_pitches σε simplified_pitches
	ultimate_interval_list = []
	last_pitch = getPosPitchList(piece.child.pitch[-1])
	for phrases in piece:
		if type(phrases.cargo) != phrase.Phrase:
			continue
		
		for each_syllable in phrases:
			
			total_interval = 0
			for each_sign in each_syllable:
				total_interval += sum(each_sign.cargo.interval)
			
			last_pitch += total_interval
			ultimate_interval_list.append(last_pitch)
				
	
	return ultimate_interval_list












			
			