# -*- coding: utf-8 -*-
import unittest

class Syllable:
	def __init__(self, syllable="?", end_word=False):
		self.syllable = syllable
		self.end_word = end_word


	@property
	def end_word(self):
		return self.__end_word
	
	
	@end_word.setter
	def end_word(self, new_end_word):
		if type(new_end_word) is not bool:
			print("end_word must be boolean type")
			print("You gave me this value'"+str(new_end_word)+"' with that type'" + str(new_end_word)+"'.")
			print("It parse the default value: 'False'.")
			self.__end_word = False
		else:		
			self.__end_word = new_end_word

	def __repr__(self):
		if self.end_word:
			str_end_word = "|"
		else:
			str_end_word = ""
		return self.syllable + str_end_word

class TestTracker(unittest.TestCase):
	def test_bitmap_testing(self):
		
		s1 = Syllable("Σου", True)
		self.assertEqual(s1.syllable, "Σου")
		self.assertEqual(s1.end_word, True)
		self.assertEqual(repr(s1), "Σου|")
		s2 = Syllable("τρο")
		self.assertEqual(repr(s2), "τρο")
		s3 = Syllable("τρο",False)
		self.assertEqual(repr(s3), "τρο")
		
		
		
		
		
		
if __name__ == '__main__':
	unittest.main()
	
	
	
	
	
