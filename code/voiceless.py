# -*- coding: utf-8 -*-
import unittest


voiceless = {
	"di":2**0,
	"ve":2**1,
	"an":2**2,
	"anll":2**3,
	"anr":2**4, #αντικένωμα κόκκινο
	"ap":2**5,
	"apr":2**6, #απόδομα κόκκινο
	"ch":2**7,
	"dd":2**8,
	"ddr":2**9, #διπλή κόκκινη
	"en":2**10,
	"ep":2**11,
	"g":2**12,
	"g_s":2**13,
	"gg":2**14,
	"gs":2**15,
	"imif":2**16,
	"imifp":2**17,
	"is":2**18,	#ισάκι
	"kl":2**19,
	"klr":2**20, #κλάσμα κόκκινο
	"kr":2**21,
	"krr":2**22, #κράτημα κόκκινο
	"l":2**23,
	"ll":2**24,
	"nenano":2**25,
	"om":2**26,
	"omr":2**27, #ομαλόν κόκκινο
	"ou":2**28,
	"para":2**29,
	"para_":2**30,
	"pht1": 2**31,
	"pht2": 2**32,
	"pht3": 2**33,
	"pht4": 2**34,
	"pht5": 2**35,
	"pht6": 2**36,
	"pht8": 2**37,
	"ps": 2**38,
	"pspara":2**39,
	"psr":2**40, #ψηφιστόν κόκκινο
	"pssy":2**41,
	"st":2**42,
	"sy":2**43,
	"tr":2**44,
	"tr_":2**45,
	"tr_r":2**46, #στρεπτόν κόκκινο
	"trpara":2**47,
	"trr":2**48, #τρομικόν κόκκινο
	"trsy":2**49,
	"u":2**50, # θ
	"ues":2**51,    # εσω
	"uex":2**52,    # εξω
	"ua":2**53,     # θεμα απλούν
	"uu":2**54,     # θες απόθες
	"v":2**55,
	"vr":2**56, #βαρεία κόκκινη
	"vv":2**57,
	"xkl":2**58,
	"xklr":2**59, #ξηρόν κλάσμα κόκκινο
	"z":2**60,
	"zr":2**61 #παρακλητική κόκκινο
}




def getUserValueByUid(uid):
	try:
		if (type(uid) != int) and (type(uid) != float):
			raise TypeError

		for key, value in voiceless.items():
			if value == uid:
				return key
		return None
	except TypeError:
		print("TypeError: The Type of uid parameter is", type(uid), "instead of int or float\n")
		return None





class TestTracker(unittest.TestCase):
	def test_the_tree_constructor(self):
		self.assertEqual(getUserValueByUid(2**58), "xkl")
		self.assertEqual(voiceless.get(2**57), None)
		self.assertEqual(voiceless.get("tr_"), 2**45)


if __name__ == '__main__':
	unittest.main()

