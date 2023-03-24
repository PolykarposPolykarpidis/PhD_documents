# -*- coding: utf-8 -*-
import unittest

class Phrase:
	def __init__(self, class_id=-1, edit_distance=100):
		self.class_id = class_id
		self.edit_distance = edit_distance


	@property
	def class_id(self):
		return self.__class_id
	
	
	@class_id.setter
	def class_id(self, new_class_id):
		if type(new_class_id) != int and new_class_id != None:
			print("the class_id must be integer or the None value.")
			print("This is value is", type(new_class_id), 'type')
			self.__class_id = None
		else:		
			self.__class_id = new_class_id



	@property
	def edit_distance(self):
		return self.__edit_distance
	
	
	@edit_distance.setter
	def edit_distance(self, new_edit_distance):
		if type(new_edit_distance) != int and type(new_edit_distance) != float and new_edit_distance != None:
			print("the edit_distance must be integer or float or the None value.")
			print("This is value is", type(new_edit_distance), 'type')
			self.__edit_distance = None
		else:		
			self.__edit_distance = new_edit_distance

	def __repr__(self):
		return 'class_id=' + str(self.class_id) +" edit_distance=" + str(self.edit_distance) + '\t'



class TestTracker(unittest.TestCase):
	def test_Phrase_testing(self):
		print("-------------")
		p1 = Phrase(1,2)
		self.assertEqual(p1.class_id, 1)
		self.assertEqual(p1.edit_distance, 2)
		p1.class_id = 5
		self.assertEqual(p1.class_id, 5)
		p2 = Phrase()
		self.assertEqual(p2.class_id, None)
		print(repr(p1))


if __name__ == '__main__':
	unittest.main()
	