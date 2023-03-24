# -*- coding: utf-8 -*-
import unittest
import bitmap
import metadata
import syllable
from abcd import pitch_list
import phrase

class PitchList(list):
	def append(self, element):
		for every_pitch in element:
			if every_pitch not in pitch_list:
				print("This value", every_pitch, "is not valid pitch")
				raise ValueError("")
		return list.extend(self, element)


class Node:
	def __init__(self, cargo = None, pitch = None, parent = None, child = None,
			  sibling = None, voiceless = bitmap.Bitmap(0), continue_ = bitmap.Bitmap(0), duration = None):
		self.__cargo = cargo
		if pitch == None:
			self.__pitch = PitchList([])
		else:
			self.__pitch = PitchList(pitch)
		self.parent = parent
		self.child = child
		self.sibling = sibling
		self.__voiceless = voiceless 
		self.__continue_ = continue_
		self.duration = duration
		self.__iteratorPointer = child
		
	
	
	
	@property
	def pitch(self):
		return self.__pitch
	

	@pitch.setter
	def pitch(self, new_pitch):
		if type(new_pitch) != PitchList:
			print("type(new_pitch) =", type(new_pitch))
			raise TypeError("new_pitch must be PitchList type")
		for every_pitch in new_pitch:
			if every_pitch not in pitch_list:
				print("I cannot find this '"+str(every_pitch)+"' in abcd.echos_list.")
				print("It parse the default value: [].")
				self.__pitch = PitchList([])
			else:
				self.__pitch = new_pitch
	

	
	@property
	def voiceless(self):
		return self.__voiceless
	

	@voiceless.setter
	def voiceless(self, new_voiceless):
		if type(new_voiceless) != bitmap.Bitmap:
			print("voiceless is not Bitmap type.")
			self.__voiceless=  bitmap.Bitmap(0)
		else:		
			self.__voiceless = new_voiceless
	
	
	
	@property
	def continue_(self):
		return self.__continue_
	

	@continue_.setter
	def continue_(self, new_continue_):
		if type(new_continue_) != bitmap.Bitmap:
			print("continue_ is not Bitmap type.")
			self.__continue_=  bitmap.Bitmap(0)
		else:		
			self.__continue_ = new_continue_
	
	
	
	#============================να το έχω έτοιμο==================================
	@property
	def cargo(self):
		return self.__cargo
	
	@cargo.setter
	def cargo(self, new_cargo):	
		self.__cargo = new_cargo
	#==============================================================================
	#=========================εδώ το καλό το hasSomething==========================
	def hasChild(self):
		return self.child != None

	def hasSibling(self):
		return self.sibling != None

	def hasParent(self):
		return self.parent != None

	def isRoot(self):
		return not self.hasParent()

	def isLeaf(self):
		return not self.hasChild()
	#==============================================================================


	def getRoot(self):
		temp = self
		while temp.hasParent():
			temp = temp.parent
		return temp
	
	
	
	def getFirstLeafOfTree(self):
		temp = self.getRoot()
		while temp.hasChild():
			temp = temp.child
		return temp


	def getLeaf(self):
		temp = self
		while temp.hasChild():
			temp = temp.child
		return temp


	
	def getLastChild(self):
		temp = self
		if temp.hasChild():
			temp = temp.child
			while temp.hasSibling():
				temp = temp.sibling
			return temp
		else:
			print("This node is leaf. So, it has not child")
			return None

	'''
	def __repr__(self):
		ret = str(self.cargo)+" "+ str(self.pitch)
		if self.hasChild():
			ret = ret + "~\n" + repr(self.child) + "\n"
		if self.hasSibling():
			ret = ret + "-->" + repr(self.sibling)
		return ret
	
	'''
	def __repr__(self):
		return str(self.cargo)+" "+ str(self.pitch)
	
	
	
	
	
	'''
	Ως __len__ ενός node έχω ορίσει το πλήθος των παιδιών που έχει
	(μόνο των άμεσων παιδιών).
	
	Είναι one-based,
	δηλαδή αν len(NodeΑ) = 1 αυτό σημαίνει ότι το NodeΑ έχει 1 ένα παιδί.
	'''
	def __len__(self):
		num_of_children = 0
		for i in self:
			num_of_children += 1
		return num_of_children
	

	def addChild(self, node):
		if self.hasChild():
			temp = self.child
			while temp.hasSibling():
				temp = temp.sibling
			temp.sibling = node
		else:
			self.child = node
		node.parent = self


	
	
	def addSibling(self, node):
		temp = self
		while temp.hasSibling():
			temp = temp.sibling
		temp.sibling = node
		node.parent = self.parent
	
	
	

	def __iter__(self):# it wants the root of the tree
		if self.hasChild():
			self.__iteratorPointer = self.child
		else:
			self.__iter = None
		return self



	def __next__(self):
		if self.__iteratorPointer != None:
			node = self.__iteratorPointer
			self.__iteratorPointer = self.__iteratorPointer.sibling
			return node
		else:
			raise StopIteration




#==============================================================================
	def postorderTraversal(self, list_nodes = None):
		
		if list_nodes is None:
			list_nodes = []
		
		
		if self.hasChild():
			self.child.postorderTraversal(list_nodes)
		
		list_nodes.append(self.cargo)
		if self.hasSibling():
			self.sibling.postorderTraversal(list_nodes)

		return list_nodes







	def preorderTraversal(self, list_nodes = None):
		
		if list_nodes is None:
			list_nodes = []
			
		list_nodes.append(self)
		
		
		if self.hasChild():
			self.child.preorderTraversal(list_nodes)
		
		
		if self.hasSibling():
			self.sibling.preorderTraversal(list_nodes)

		return list_nodes







	def traversalVoicedLeaf(self, list_nodes = None):
		if list_nodes is None:
			list_nodes = []
		
		if type(self.cargo) == metadata.meta:
			self.child.traversalVoicedLeaf(list_nodes)
		
		if self.cargo == "martyria":
			self.sibling.traversalVoicedLeaf(list_nodes)
		
		if type(self.cargo) == phrase.Phrase:
			self.child.traversalVoicedLeaf(list_nodes)
			if self.hasSibling():
				self.sibling.traversalVoicedLeaf(list_nodes)
		
		if type(self.cargo) == syllable.Syllable:
			temp_list = []
			for a_child in self:
				temp_list.append(a_child.cargo)
			list_nodes.append(temp_list)
			if self.hasSibling():
				self.sibling.traversalVoicedLeaf(list_nodes)
		
		return list_nodes
	
	
	def markovTraversal(self, list_nodes = None):
		if list_nodes is None:
			list_nodes = []
		
		if type(self.cargo) == metadata.meta:
			self.child.markovTraversal(list_nodes)

		if self.cargo == "martyria":
			self.sibling.markovTraversal(list_nodes)

		if type(self.cargo) == phrase.Phrase:
			list_nodes.append("-")
			self.child.markovTraversal(list_nodes)
			if self.hasSibling():
				self.sibling.markovTraversal(list_nodes)
		
		if type(self.cargo) == syllable.Syllable:

			for a_child in self:
				list_nodes.append(a_child.cargo.user_value)

			if self.hasSibling():
				self.sibling.markovTraversal(list_nodes)
		return list_nodes
	
	
	
	
	def getPhrasesLeavesNodes(self, list_nodes = None):
		if list_nodes is None:
			list_nodes = []
		
		if type(self.cargo) == metadata.meta:
			self.child.getPhrasesLeavesNodes(list_nodes)
		
		if self.cargo == "martyria":
			self.sibling.getPhrasesLeavesNodes(list_nodes)
		
		if type(self.cargo) == phrase.Phrase:
			self.child.getPhrasesLeavesNodes(list_nodes)
			if self.hasSibling():
				self.sibling.getPhrasesLeavesNodes(list_nodes)
		
		if type(self.cargo) == syllable.Syllable:
			temp_list = []
			for a_child in self:
				temp_list.append(a_child)
			list_nodes.append(temp_list)
			if self.hasSibling():
				self.sibling.getPhrasesLeavesNodes(list_nodes)
		
		return list_nodes
	
	
	def traversalVoicedLeaf_Phrased(self, list_nodes = None):
		if list_nodes is None:
			list_nodes = []
		
		if type(self.cargo) == metadata.meta:
			self.child.traversalVoicedLeaf_Phrased(list_nodes)
		
		if self.cargo == "martyria":
			self.sibling.traversalVoicedLeaf_Phrased(list_nodes)
		
		if type(self.cargo) == phrase.Phrase:
			phrase_list = []
			for every_syllable in self:
				if type(every_syllable.cargo) != syllable.Syllable:
					raise TypeError("Phrase child must be 'Syllable' object")
				temp_list = []
				for a_child in every_syllable:
					temp_list.append(a_child)
				phrase_list.extend(temp_list)
			list_nodes.append(phrase_list)
		if self.hasSibling():
			self.sibling.traversalVoicedLeaf_Phrased(list_nodes)
		return list_nodes
	
	
	
	def syllableTraversal(self, list_nodes = None):
		if list_nodes is None:
			list_nodes = []
		#input(type(self))
		if type(self.cargo) == syllable.Syllable:
			list_nodes.append(self)
			
		if type(self.cargo) == phrase.Phrase:
			list_nodes.append('EOPhrase')
		
		if self.hasChild():
			self.child.syllableTraversal(list_nodes)
		
		if self.hasSibling():
			self.sibling.syllableTraversal(list_nodes)

		return list_nodes
	
	
	
	
	#I create that for the sp function
	def getPhrasesNodes_list(self, list_nodes = None):
		if list_nodes is None:
			list_nodes = []
		
		if type(self.cargo) == metadata.meta:
			self.child.getPhrasesNodes_list(list_nodes)
		
		if self.cargo == "martyria":
			self.sibling.getPhrasesNodes_list(list_nodes)
		
		if type(self.cargo) == phrase.Phrase:
			list_nodes.append(self)
			if self.hasSibling():
				self.sibling.getPhrasesNodes_list(list_nodes)
			
		
		return list_nodes
#==============================================================================








class TestTree(unittest.TestCase):
	def test_the_tree_constructor(self):
		T = Node("Root")
		print(T.pitch)
		
		'''
		T.addChild(Node("F_1"))
		T.child.addSibling(Node("F_2"))
		T.child.addSibling(Node("F_3"))
		T.child.addSibling(Node("F_4"))
		
		T.child.addChild(Node("S_1.1"))
		T.child.addChild(Node("S_1.2"))
		T.child.child.addSibling(Node("S_1.3"))
		T.child.addChild(Node("S_1.4"))
		T.child.sibling.addChild(Node("S_2.1"))
		T.child.sibling.addChild(Node("S_2.2"))
		T.child.sibling.addChild(Node("S_2.3"))
		T.child.sibling.addChild(Node("S_2.4"))
		T.child.sibling.sibling.addChild(Node("S_3.1"))
		
		
		T.child.child.sibling.addChild(Node("T_1.2.1"))
		T.child.sibling.sibling.child.addChild(Node("T_3.1.1"))
		print(repr(T))
		
		
		self.assertEqual(T.child.sibling.sibling.child.cargo, "S_3.1")
		self.assertEqual(T.child.sibling.sibling.child.child.cargo, "T_3.1.1")

		self.assertEqual(T.child.sibling.sibling.child.child.parent.cargo, "S_3.1")
		self.assertEqual(T.child.sibling.sibling.child.child.parent.parent.cargo, "F_3")
		self.assertEqual(T.child.sibling.sibling.child.child.parent.parent.parent.cargo, "Root")

		self.assertEqual(T.sibling, None)
		self.assertEqual(T.parent, None)
		self.assertEqual(T.child.child.sibling.getLastChild().cargo, "T_1.2.1")
		
		
		self.assertEqual(T.child.sibling.sibling.child.child.parent.parent.parent.cargo, "Root")
		self.assertEqual(T.child.sibling.sibling.child.child.getRoot().cargo,"Root")
		self.assertEqual(T.getRoot(), T)
		self.assertEqual(T.getRoot().cargo, "Root")
		
		
		self.assertEqual(T.isLeaf(), False)
		self.assertEqual(T.child.isLeaf(), False)
		self.assertEqual(T.child.child.isLeaf(), True)
		
		self.assertEqual(T.child.child.sibling.isLeaf(), False)
		self.assertEqual(T.child.child.sibling.child.isLeaf(), True)
		
		self.assertEqual(T.child.sibling.isLeaf(), False)
		self.assertEqual(T.child.sibling.child.isLeaf(), True)
		self.assertEqual(T.child.sibling.child.sibling.isLeaf(), True)
		self.assertEqual(T.child.sibling.sibling.child.isLeaf(), False)
		self.assertEqual(T.child.sibling.sibling.child.child.isLeaf(), True)

		self.assertEqual(T.child.sibling.sibling.child.child.getFirstLeafOfTree().cargo, "S_1.1")

		
		self.assertEqual(T.child.sibling.sibling.getLeaf().cargo,"T_3.1.1")
		'''
		
		
if __name__ == '__main__':
	unittest.main()
