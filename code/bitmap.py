# -*- coding: utf-8 -*-
import unittest

NUM_OF_VOICELESS = 61

class Bitmap:
	def __init__(self, b = 0):
		self.bitmap = b
			
	@property
	def bitmap(self):
		return self.__bitmap
	
	@bitmap.setter
	def bitmap(self, new_b):
		if type(new_b) != int:
			print("The Type of bitmap must be int")
			print("the type of your parameter is", type(new_b))
			print("It assign the by-default value: 0.")
			self.__bitmap = 0
		elif new_b < 0 or new_b >= (2**(NUM_OF_VOICELESS+1)):
			print("Your parameter must be in range [0,2^"+str(NUM_OF_VOICELESS+1)+").")
			print("2**"+str(NUM_OF_VOICELESS+2)+" =", 2**(NUM_OF_VOICELESS+1))
			print("It assign the by-default value: 0.")
			print(new_b)
			self.__bitmap = 0
		else:		
			self.__bitmap = new_b


	
	
	def __repr__(self):
		return "{0:b}".format(self.bitmap)

	



	def __and__(self, bitmap):
		try:
			if type(self) is not Bitmap or type(bitmap) is not Bitmap:
				raise TypeError
			return Bitmap(bitmap.bitmap & self.bitmap)
		except TypeError:
			print("TypeError: The type of each operant must be Bitmap Class.")
			return None





	def __or__(self,bitmap):
		try:
			if type(self) is not Bitmap or type(bitmap) is not Bitmap:
				raise TypeError
			return Bitmap(bitmap.bitmap | self.bitmap)
		except TypeError:
			print("TypeError: The type of each operant must be Bitmap Class.")
			return None





	def __eq__(self,bitmap):
		try:
			if type(self) is not Bitmap or type(bitmap) is not Bitmap:
				raise TypeError
			if bitmap.bitmap == self.bitmap:
				return True
			else:
				return False
		except TypeError:
			print("TypeError: The type of each operant must be Bitmap Class.")
			return None



	def isBitmapSuperset(self, bitmap):
		try:
			if type(bitmap.bitmap) is not int:
				raise TypeError
			if (bitmap.bitmap & self.bitmap) == bitmap.bitmap:
				return True
			else:
				return False
		except TypeError:
			print("TypeError: The Type of bitmap.bitmap parameter is", type(bitmap.bitmap), "instead of int")
			return None

	def isBitmapTrue(self, bitmap):#bitmap
		try:
			if type(bitmap.bitmap) is not int:
				raise TypeError
			
			if bitmap.bitmap == self.bitmap:
				return True
			else:
				return False
		except TypeError:
			print("TypeError: The Type of bitmap.bitmap parameter is", type(bitmap.bitmap), "instead of int\n")
			return None


	def setZero(self):
		self.bitmap = 0

class TestTracker(unittest.TestCase):
	def test_bitmap_testing(self):
		t = Bitmap(0b1000101001)
		a = Bitmap(0b1000100101)
		#aa = Bitmap()
		#b = Bitmap(2**65)
		
		self.assertEqual(t.isBitmapSuperset(Bitmap(553)), True)
		self.assertEqual(t.isBitmapSuperset(Bitmap(9)), True)
		self.assertEqual(t.isBitmapSuperset(Bitmap(0b1000101001)), True)
		self.assertEqual(t.isBitmapSuperset(Bitmap(0b1000100001)), True)
		self.assertEqual(t.isBitmapSuperset(Bitmap(0b0000000000)), True)
		self.assertEqual(t.isBitmapSuperset(Bitmap()), True)
		self.assertEqual(t.isBitmapSuperset(Bitmap(0b1010101001)), False)
		self.assertEqual(t.isBitmapSuperset(Bitmap(0b0001000100001)), True)
		self.assertEqual(t.isBitmapSuperset(Bitmap(0b01)), True)
		self.assertEqual(t.isBitmapSuperset(Bitmap(0b1111111111111)), False)

		
		self.assertEqual(t.isBitmapTrue(Bitmap(0b1000101001)), True)
		self.assertEqual(t.isBitmapTrue(Bitmap(9)), False)
		self.assertEqual(t.isBitmapTrue(Bitmap(553)), True)
		self.assertEqual(t.isBitmapTrue(Bitmap(0b0000000000)), False)
		self.assertEqual(t.isBitmapTrue(Bitmap()), False)
		self.assertEqual(t.isBitmapTrue(Bitmap(0b1010101001)), False)
		self.assertEqual(t.isBitmapTrue(Bitmap(0b0001000100001)), False)
		self.assertEqual(t.isBitmapTrue(Bitmap(0b01)), False)
		self.assertEqual(t.isBitmapTrue(Bitmap(0b1111111111111)), False)
		

		q = Bitmap(0b1000100001)
		c = t | a
		self.assertEqual(c.bitmap, 0b1000101101)
		c = t & a
		self.assertEqual(c.bitmap, 0b1000100001)
		self.assertEqual(q==c, True)
		t.setZero()
		self.assertEqual(t == Bitmap(0),True)
		


if __name__ == '__main__':
	unittest.main()

