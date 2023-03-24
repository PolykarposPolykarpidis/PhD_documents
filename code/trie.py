# -*- coding: utf-8 -*-
import unittest

class TrieNode:
	def __init__(self, cargo = None, frequency = 0, parent = None, child = None, sibling = None):
		self.__cargo = cargo
		self.frequency = frequency
		self.parent = parent
		self.child = child
		self.sibling = sibling
		self.__iteratorPointer = child


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



	def __repr__(self):
		ret = str(self.cargo)
		if self.hasChild():
			ret = ret + "~\n" + repr(self.child) + "\n"
		if self.hasSibling():
			ret = ret + "-->" + repr(self.sibling)
		return ret




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


	def findChild(self, a_node):
		for every_child in self:
			if every_child.cargo == a_node.cargo:
				return every_child
		return None



	def existPath(self, path_list):
		temp = self
		for element in path_list:
			temp = temp.findChild(element)
			if temp == None:
				return False
		return True










class TestTree(unittest.TestCase):
	def test_the_tree_constructor(self):
		T = TrieNode("Root")
		T.addChild(TrieNode("1"))
		T.addChild(TrieNode("2"))
		T.addChild(TrieNode("3"))
		T.addChild(TrieNode("4"))
		T.child.addChild(TrieNode("1.1"))
		T.child.sibling.addChild(TrieNode("2.1"))
		T.child.sibling.child.addChild(TrieNode("2.1.1"))
		print(repr(T))
		print(T.existPath([TrieNode("2"),TrieNode("2.1"),TrieNode("2.1.1")]))







if __name__ == '__main__':
	unittest.main()
