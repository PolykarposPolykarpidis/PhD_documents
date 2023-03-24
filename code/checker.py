# -*- coding: utf-8 -*-
from abcd import punctuation, echos_list, pitch_list
import voiced
import voiceless
def isEchos(possible_echos):
	return possible_echos in echos_list

def isVoiced(possible_voiced):
	return voiced.voiced_units.get(possible_voiced)

def isVoiceless(possible_voiceless):
	return voiceless.voiceless.get(possible_voiceless)

def isSyllableSymbol(possible_syllable_symbol):
	return possible_syllable_symbol == punctuation["syllable"]

def isDelimiterSymbol(possible_voiced_delimiter):
	return possible_voiced_delimiter == punctuation["voiced_delimiter"]

def isAcceptedNumber(possible_accepted_number):
	if possible_accepted_number.isdigit():
		if int(possible_accepted_number) in [1,0]:
			return True
	return False

def isSpecialCharacter(possible_special_character):
	return possible_special_character in [punctuation["end_phrase"], punctuation["end_word"], punctuation["end_phrase_and_word"]]

def isAnyEndPhraseCharacter(possible_any_end_phrase):
	return possible_any_end_phrase in [punctuation["end_phrase"], punctuation["end_phrase_and_word"]]

def isEndPhraseCharacter(possible_end_phrase):
	return possible_end_phrase == punctuation["end_phrase"]

def isEndWordCharacter(possible_end_word):
	return possible_end_word  == punctuation["end_word"]


def isEmptylist(possible_empty_list):
	if possible_empty_list == []:
		print("Error: isEmptylist(subl)")
		print("Empty list error:", possible_empty_list)
		return True
	return False


def hasSyllableSymbol(l):
	return punctuation["syllable"] in l
	


def hasMartyriaSymbol(l):
	temp = []
	flag = False
	for i in l:
		if i == "=":
			flag = True
		if flag == True:
			temp.append(i)
	for i in pitch_list:
		if i in temp:
			return True
	return False








def startFSM(l):
	if isEmptylist(l):
		print("Emptylist Error")
		return False
	return checkMartyriaOrInterval(l)



def checkMartyriaOrInterval(subl):
	if isEchos(subl[0]) ^ hasMartyriaSymbol(subl):
		print("Error: Echos or MartyriaSymbol.")
		return False
	if isEchos(subl[0]) and hasMartyriaSymbol(subl):
		return checkVoiced(subl[1:])
	else:
		return checkVoiced(subl)




def checkVoiced(subl):
	if isEmptylist(subl):
		print("Emptylist Error")
		return False
	if isVoiced(subl[0]):
		return checkVoicelessOrDelimiterSymbolOrSyllableSymbol(subl[1:])
	else:
		print("Error: checkVoiced(subl)")
		print("subl[0] =", subl[0])
		print("I cannot find the Voiced sign.")
		return False



def checkVoicelessOrDelimiterSymbolOrSyllableSymbol(subl):
	if isEmptylist(subl):
		print("Emptylist Error")
		return False
	if isVoiceless(subl[0]):
		return checkNumberOrVoicelessOrDelimiterSymbolOrSyllableSymbol(subl[1:])
	elif isDelimiterSymbol(subl[0]):
		return checkVoiced(subl[1:])
	elif isSyllableSymbol(subl[0]):
		return checkAfterSyllableSymbol(subl[1:])
	else:
		print("Error: checkVoicelessOrDelimiterSymbolOrSyllableSymbol(subl)")
		print("Not accept value. Sublist:", subl)
		return False



def checkNumberOrVoicelessOrDelimiterSymbolOrSyllableSymbol(subl):
	if isEmptylist(subl):
		print("Emptylist Error")
		return False
	if isAcceptedNumber(subl[0]):
		return checkVoicelessOrDelimiterSymbolOrSyllableSymbol(subl[1:])
	elif isVoiceless(subl[0]):
		return checkNumberOrVoicelessOrDelimiterSymbolOrSyllableSymbol(subl[1:])
	elif isDelimiterSymbol(subl[0]):
		return checkVoiced(subl[1:])
	elif isSyllableSymbol(subl[0]):
		return checkAfterSyllableSymbol(subl[1:])
	else:
		print("Error: checkNumberOrVoicelessOrDelimiterSymbolOrSyllableSymbol(subl)")
		print("Not accept value. Sublist:", subl)
		return False




def checkAfterSyllableSymbol(subl):
	if len(subl) == 1:
		return True
	if len(subl) > 2:
		print("Error: checkAfterSyllableSymbol(subl)")
		return False
	if len(subl) == 2:
		if not isSpecialCharacter(subl[1]):
			print("Error: isSpecialCharacter(subl)")
			return False
		else:
			return True
