# -*- coding: utf-8 -*-
import re
from abcd import punctuation

def tokenizer(string, delimiter=" "):
	li = list(string.split(delimiter)) 
	return li

def addSpaces(string, symbol):
	return string.replace(symbol, " "+symbol+" ")


def stripComments(string):
	m = re.sub(r'#.*',"", string)
	if m:
		return m
	return string


def splitingData(line):
	temp = addSpaces(line, punctuation["comment"])
	temp = stripComments(temp)
	temp = addSpaces(temp, punctuation["syllable"])
	temp = addSpaces(temp, punctuation["voiced_delimiter"])
	temp = addSpaces(temp, punctuation["end_phrase"])
	temp = addSpaces(temp, punctuation["end_word"])
	temp = re.sub('\|\s+\-', punctuation["end_phrase_and_word"], temp)
	return tokenizer(temp, "\n")