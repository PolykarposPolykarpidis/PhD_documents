# -*- coding: utf-8 -*-
import unittest

from abcd import echos_list, punctuation


class Martyria:
	def __init__(self, echos="?"):
		self.echos = echos


	@property
	def echos(self):
		return self.__echos
	
	
	@echos.setter
	def echos(self, new_echos):
		if new_echos not in echos_list:
			print("I cannot find this '"+str(new_echos)+"' in abcd.echos_list.")
			print("It parse the default value: '?'.")
			self.__arithmetic = "?"
		else:		
			self.__echos = new_echos

	def __repr__(self):
		return self.echos




class TestTracker(unittest.TestCase):
	def test_bitmap_testing(self):
		
		m1 = Martyria("mode_?")
		self.assertEqual(m1.echos, "mode_?")
		m1.arithmetic = "mode_c"
		self.assertEqual(m1.echos, "mode_c")
		
		m2 = Martyria("mode_pla")
		self.assertEqual(m2.echos, "mode_pla")
		m2.echos = 123456789
		self.assertEqual(m2.echos, "mode_?")
		
		m3 = Martyria("mode_a")
		self.assertEqual(m3.echos, "mode_a")
		m3.arithmetic = "mode_varys"
		self.assertEqual(m3.echos, "mode_varys")
		print(repr(m3))


if __name__ == '__main__':
	unittest.main()
	
	
	