# -*- coding: utf-8 -*-

from abcd import pitch_list


class meta:
	def __init__(self,
	file_name,
	library,
	library_number,
	catalogue,
	starting_folio,
	initium,
	mode,
	kind,
	num_line,
	starting_pitch,
	composer,
	lyrics_lang,
	alphabet,
	more_details,
	orthography):
		self.file_name = file_name
		self.library = library
		self.library_number = library_number
		self.catalogue = catalogue
		self.starting_folio = starting_folio
		self.initium = initium
		self.mode = mode
		self.kind = kind
		self.num_line = num_line
		self.starting_pitch = starting_pitch
		self.composer = composer
		self.lyrics_lang = lyrics_lang
		self.alphabet = alphabet
		self.more_details = more_details
		self.orthography = orthography



def metaParser(data):
	root = data.getroot()
	for child in root:
		if child.tag == "head":
			name_file = child.find('nameFile').text
			library = child.find('library').text
			library_number = child.find('libraryΝumber').text
			catalogue = child.find('catalogue').text
			starting_folio = child.find('startingFolio').text
			initium = child.find('initium').text
			mode = child.find('mode').text
			kind = child.find('kind').text
			num_line = child.find('numLine').text
			starting_pitch = child.find('startingPitch').text
			composer = child.find('composer').text
			lyrics_lang = child.find('lyricsLang').text
			alphabet = child.find('alphabet').text
			more_details = child.find('moreDetails').text
			orthography = child.find('orthography').text
			if starting_pitch not in pitch_list:
				print("Warning in xml: The startingPitch text not abcd.pitch_list.")
			return meta(name_file,
					 library,
					 library_number,
					 catalogue,
					 starting_folio,
					 initium,
					 mode,
					 kind,
					 num_line,
					 starting_pitch,
					 composer,
					 lyrics_lang,
					 alphabet,
					 more_details,
					 orthography)
		
		
		
		
		
	def __repr__(self):
		return self.file_name	
		
		
		
		
		
		
		