# -*- coding: utf-8 -*-
from abcd import pitch_list, punctuation
import tree
from checker import isEchos
import syllable
import voiced
import voiceless
import bitmap
import martyria
import phrase


def getSyllable(l):
	for pos, i in enumerate(l):
		if i == punctuation["syllable"]:
			return l[pos+1]
		
def getSyllablePhrase(l):
	for pos, i in enumerate(l):
		if i == punctuation["syllable"]:
			return l[pos+1:]


def isLastChildOfParent(l):
	return l[-1] in [punctuation["end_phrase"], punctuation["end_phrase_and_word"]]




def syllableConstructor(syl):
	if syl[-1] == punctuation["end_word"] or syl[-1] == punctuation["end_phrase_and_word"]:
		return syllable.Syllable(syl[0], True)
	else:
		return syllable.Syllable(syl[0], False)



def posRange(a_list):
	pos_range = []
	temp_l = []
	
	for i in a_list:
		if i == punctuation["syllable"]:
			pos_range.append(temp_l)
			break
		elif i == punctuation["voiced_delimiter"]:
			pos_range.append(temp_l)
			temp_l = []
		else:
			temp_l.append(i)
	
	return pos_range




def getPosPitchList(a_pitch):
	for pos, p in enumerate(pitch_list):
		if p == a_pitch:
			break
	return pos
#==============================================================================
#==============================================================================






def level1(is_martyria, subtree):
	if is_martyria:
		new_subtree = tree.Node("martyria")
		new_subtree.pitch = subtree.pitch
	else:
		new_subtree = tree.Node(phrase.Phrase())							#==code για το pitch
		
	new_subtree.voiceless = new_subtree.voiceless | subtree.voiceless
	new_subtree.continue_ = new_subtree.continue_ | subtree.continue_
	new_subtree.addChild(subtree)
	
	return new_subtree, True







#==============================================================================

def phrase_level2(leaf_node_list, a_list, newNode_boolean):
	subtree = tree.Node(syllableConstructor(getSyllablePhrase(a_list)))
	for i in leaf_node_list:
		subtree.addChild(i)
		subtree.voiceless = subtree.voiceless | i.voiceless
		subtree.continue_ = subtree.continue_ | i.continue_

	
	if newNode_boolean:
		return level1(False, subtree)
	else:
		return subtree, newNode_boolean
	
	
	


def martyria_level2(leaf_node_list, a_list, newNode_boolean):
	subtree = tree.Node(martyria.Martyria(a_list[0]))
	for i in leaf_node_list:
		subtree.addChild(i)
		subtree.voiceless = subtree.voiceless | i.voiceless
		subtree.continue_ = subtree.continue_ | i.continue_
	subtree.pitch = tree.PitchList([getSyllable(a_list)])
	 
	if newNode_boolean:
		return level1(True, subtree)
	else:
		return subtree, newNode_boolean





#==============================================================================
def phrase_level3(a_list, newNode_boolean):
	list_lists = posRange(a_list)	#ενδιάμεσο βήμα για την ευκρίνια του κώδικα
	leaf_node_list = createLeafNode(list_lists)
	
	return phrase_level2(leaf_node_list, a_list, newNode_boolean)
	
	

def martyria_level3(a_list, newNode_boolean):
	list_lists = posRange(a_list[1:]) #ενδιάμεσο βήμα για την ευκρίνια του κώδικα
	leaf_node_list = createLeafNode(list_lists)
	
	return martyria_level2(leaf_node_list, a_list, newNode_boolean)
	
	
	
#==============================================================================
def createLeafNode(lists_voiced_signs):
	voiced_node_list = []
	
	for voiced_voiceless in lists_voiced_signs:
		# parse voiced
		a_node = tree.Node(voiced.voiced_units.get(voiced_voiceless[0]))
		
		# parse voiced and voiceless
		voiceless_b, continue_b = parseVoicelesses(voiced_voiceless[1:])
		a_node.voiceless = voiceless_b
		a_node.continue_ = continue_b
		
		# append a voiced
		voiced_node_list.append(a_node)
	return voiced_node_list





def parseVoicelesses(voicelessContinueList):
	t_voiceless = bitmap.Bitmap(0)
	t_continue = bitmap.Bitmap(0)
	temp = bitmap.Bitmap(0)
	for i in voicelessContinueList:
		if i.isdigit():
			if int(i) == 1:
				t_continue = t_continue | temp
		else:
			t_voiceless = t_voiceless | bitmap.Bitmap(voiceless.voiceless.get(i))
			temp = bitmap.Bitmap(voiceless.voiceless.get(i))
	return t_voiceless, t_continue








#==============================================================================
def constructor(root_cargo, music_piece):
	root_node = tree.Node(root_cargo)
	lastNode_boolean = True
	newNode = True
	while len(music_piece) != 0:
		if isEchos(music_piece[0][0]):
			subtree, lastNode_boolean = martyria_level3(music_piece[0], newNode)
		else:
			subtree, lastNode_boolean = phrase_level3(music_piece[0], newNode)
		
		
		lastNode_boolean = isLastChildOfParent(music_piece[0])
		del(music_piece[0])
		
		
		if newNode:
			root_node.addChild(subtree)
			root_node.voiceless = root_node.voiceless | subtree.voiceless
			root_node.continue_ = root_node.continue_ | subtree.continue_
			newNode = False
		else:
			temp = root_node.getLastChild()
			temp.addChild(subtree)
			
			
			# ακολουθούν 2 γραμμές κώδικα για το pitch
			if temp.cargo == "martyria":
				temp.pitch = subtree.pitch
			
			
			
			temp.voiceless = temp.voiceless | subtree.voiceless
			temp.continue_ = temp.continue_ | subtree.continue_
			
			root_node.voiceless = root_node.voiceless | subtree.voiceless
			root_node.continue_ = root_node.continue_ | subtree.continue_
		
		if lastNode_boolean:
			lastNode_boolean = True
			newNode = True
	
	
	
	parsePitch(root_node)
	#print(repr(root_node))
	return root_node






def parsePitch(byz_tree):
	given_pos = -1

	for level1_node in byz_tree:
		if level1_node.cargo == "martyria":
			given_pos = getPosPitchList(level1_node.pitch[0])
			continue
		
		
		if given_pos < 0 or given_pos >= len(pitch_list):
			raise ValueError("I couldn't find martyria pitch!")
		
		
		for level2_node in level1_node:
			for level3_node in level2_node:
				temp = level3_node.cargo.interval
				for every_interval in temp:
					given_pos = given_pos + every_interval
					level3_node.pitch.append(tree.PitchList([pitch_list[given_pos]]))

				level2_node.pitch.append(level3_node.pitch)
			level1_node.pitch.append(level2_node.pitch)
		byz_tree.pitch.append(level1_node.pitch)
	return byz_tree













music_piece_example = [
['echos_a', 'aa', '=', 'D', '-'],
['i', '=', 'Σου', '|'],
['i', '=', 'η'],
['i', '=', 'τρο'],
['o', 'l', '1', '=', 'παι'],
['p', 'l', '1', '=', 'ού'],
['ae2', 'l', '=', 'χος', '|'],
['o', '=', 'δε'],
['o', 'g', '=', 'ξι'],
['o', 'ap', '=', 'ά', '|-'],
['echos_d', 'aa', ',', 'ooh4', ',', 'a', ',', 'a', ',', 'a', '=', 'G', '-'],
['a', '=', 'ο'],
['po', 'an', '1', '=', 'δόν', '|'],
['ae2', 'an', '=', 'βυ', '-'],
['echos_d', 'a', ',', 'a', ',', 'a', '=', 'F', '-'],
['ooi', 'ps', '=', 'θού', '|'],
['a', '=', 'και'],
['a', '=', 'νουρ'],
['pk3', 'ps', 'di', '1', ',', 'a', 'di', '=', 'γή'],
['i', 'l', '1', 'v', '1', 'di', '1', ',', 'a', 'l', '1', 'v', 'di', ',', 'pi', 'l', '1', 'di', '1', ',', 'a', 'l', 'di', '=', 'σα'],
['i', 'dd', '=', 'σα']]



#pol = constructor("some_root_cargo", music_piece_example)
#print(pol)




