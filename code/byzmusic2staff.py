# -*- coding: utf-8 -*-
import tree
import bitmap




lp_EOF = "\divisioMaior"
lp_notes_dictionary = {
 "`A":"b'''",
 "`B":"b'''",
 "`C":"c",
 "`D":"d",
 "`E'":"e",
 "`F":"f",
 "`G":"g",
 "A":"a",
 "B":"b",
 "C":"c'",
 "D":"d'",
 "E":"e'",
 "F":"f'",
 "G":"g'",
 "a":"a'",
 "b":"b'",
 "c":"c''",
 "d":"d''",
 "e":"e''",
 "f":"f''",
 "g":"g''",
 "a'":"a''",
 "b'":"b''",
 "c'":"c'''",
 "d'":"d'''",
 "e'":"e'''",
 "f'":"f'''",
 "g'":"g'''",
 
 "?":"b'''"
 }


def create_lilypond_score_string(notes, lyrics,header):
	return '''\\include "gregorian.ly"

	''' + header + '''

	chant = {
	 ''' +notes+  '''
	}

	verba = \\lyricmode {'''+lyrics+'''
	}


	\\score {
	  \\new Staff <<
	  \\new Voice = "melody" \\chant
	  \\new Lyrics = "one" \\lyricsto melody \\verba
	  >>
	  \\layout {
	    \\context {
	      \Staff
	      \\remove "Time_signature_engraver"
	      \\remove "Bar_engraver"
	    }
	    \\context {
	      \Voice
	      \\remove "Stem_engraver"
	    }
	  }
	}'''



def byzmusic2staff(a_tree):
	list_of_syllables = a_tree.syllableTraversal()
	lp_lyrics = ""
	lp_notes = ""
	
	for every_syllable in list_of_syllables:
		
		#print(type(every_syllable), every_syllable, every_syllable == 'EOPhrase')
		if every_syllable == 'EOPhrase':
			if lp_notes == "":
				continue
			lp_notes += " "+ lp_EOF + "\n"
			lp_lyrics += "\n"
		else:
			for every_pitch in every_syllable.pitch:
				lp_notes = lp_notes + " " + lp_notes_dictionary[every_pitch]+'4'
			
			if len(every_syllable.pitch)-1 > 0:
				lp_lyrics = lp_lyrics + every_syllable.cargo.syllable + (len(every_syllable.pitch)-1)*" - "
			else:
				lp_lyrics = lp_lyrics + every_syllable.cargo.syllable +" " 
	
	lp_notes += "\\finalis"
	
	
	metadata_obj = a_tree.cargo
	
	metadata = '\header {\n \
	  title = "' + metadata_obj.library + ' ' + metadata_obj.library_number + '"\n\
	  subtitle = "' + metadata_obj.file_name + '"\n\
	  composer = "Composer: '  + metadata_obj.composer + '"\n\
	  piece = "Mode ' + metadata_obj.mode + '"\n\
	}'
	
	
	return lp_notes, lp_lyrics, metadata
	











#==========================Code to export KR pieces to Volpiano string======================
#Constant values related with Volpiano standard

KRpitches_to_volpiano={
	"`F":["(","8"],
	"`G":[")","9"],
	"A":["A","a"],
	"B":["B","b"],
	"C":["C""c",],
	"D":["D","d"],
	"E":["E","e"],
	"F":["F","f"],
	"G":["G","g"],
	"a":["H","h"],
	"b":["J","j"],
	"c":["K","k"],
	"d":["L","l"],
	"e":["M","m"],
	"f":["N","n"],
	"g":["O","o"],
	"a'":["P","p"],
	"b'":["Q","q"],
	"c'":["R","r"],
	"d'":["S","s"]
}
style = 0

volpiano_EOPhrase = '7-'
volpiano_EOSyllable = '-'
volpiano_EOWord = '--'
space_of_non_standard_length = '---'
clef = '1---'
barline = ['--3', '--4']



def byzmusic_to_volpiano(a_piece):
	volpiano_string = ''
	volpiano_string += clef
	
	lyrics = ''
	
	for phrase_martyria in a_piece:
		if isinstance(phrase_martyria.cargo, str):
			continue
		for syllable in phrase_martyria:
			for each_pitch in syllable.pitch:
				temp_pitch = KRpitches_to_volpiano[each_pitch][style]
				
				volpiano_string += temp_pitch
			if syllable.cargo.end_word == True:
				volpiano_string += volpiano_EOWord
			else:
				volpiano_string += volpiano_EOSyllable
		volpiano_string += volpiano_EOPhrase
	return volpiano_string


















