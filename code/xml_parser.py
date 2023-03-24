# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import checker
import metadata
import tokenization
import byzTree



def xml_parser(files):
	corpus = []
	for counter, file in enumerate(files):
		data = ET.parse(file)
		xml_music_piece = data.find('musicalPiece').text
		
		root_cargo = metadata.metaParser(data)
		
		string_music_piece = tokenization.splitingData(xml_music_piece)
		music_piece = []
		for i in string_music_piece:
			tempSplit = i.split()
			if tempSplit != []:
				music_piece.append(tempSplit)
	
		#checks every list
		isCorrectPiece = True
		for num_line, line in enumerate(music_piece):
			isCorrectLine = checker.startFSM(line)
			isCorrectPiece = isCorrectPiece and isCorrectLine
			if not isCorrectLine:
				print("Check line:", num_line+1)
		
		if not checker.isEchos(music_piece[0][0]):
			print("The first Line have to be martyria.")
			isCorrectPiece = False
		
		
		if not isCorrectPiece:
			print("Rejected file: "+ file)
		else:
			corpus.append(byzTree.constructor(root_cargo, music_piece))
	
			#print("["+str(counter)+"]",file, "ok") #===================================
		#print("==========================================")
	return corpus