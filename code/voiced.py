import unittest

class VoicedUnit:
	def __init__(self, voiced_signs=[], interval=[], user_value=[]):
		self.voiced_signs = voiced_signs
		self.interval = interval
		self.user_value = user_value


	def __repr__(self):
		return str(self.user_value[-1])


temp_single_voiced = [
	VoicedUnit(["i"], [0], ["i", "0"]),
	VoicedUnit(["e"], [-2], ["e"]), # VoicedUnit(["e"], [-2], ["e", '-2']),
	VoicedUnit(["c"], [-4], ["c"])	# VoicedUnit(["c"], [-4], ["c", '-4'])
			]

container = {
	"i": temp_single_voiced[0],
	"0": temp_single_voiced[0],
	"o": VoicedUnit(["o"], [1], ["o"]),
	"oo": VoicedUnit(["oo"], [1], ["oo"]),
	"p": VoicedUnit(["p"], [1], ["p"]),
	"pp": VoicedUnit(["pp"], [1], ["pp"]),
	"ppp": VoicedUnit(["ppp"], [1], ["ppp"]),
	"k": VoicedUnit(["k"],[2], ["k"]),
	"h": VoicedUnit(["h"], [4], ["h"]),
	"a": VoicedUnit(["a"], [-1], ["a"]),
	"aa": VoicedUnit(["aa"], [-1], ["aa"]),
	"e": temp_single_voiced[1],
	"-2": temp_single_voiced[1],
	"c": temp_single_voiced[2],
	"-4": temp_single_voiced[2],
	
	"s": VoicedUnit(["s"], [-1,-1], ["s"]),
	"kk": VoicedUnit(["kk"], [1], ["kk"]),
}



del(temp_single_voiced)




oligon_type = dict()
for k, v in container.items():
	if k == "o" or k == "oo":
		oligon_type[k] = v

petasthe_type = dict()
for k, v in container.items():
	if k == "p" or k == "pp" or k == "ppp":
		petasthe_type[k] = v

apostrophos_type = dict()
for k, v in container.items():	
	if k == "a" or k ==  "aa":
			apostrophos_type[k] = v
			
down = dict()	
for k, v in container.items():
	if k == "a" or k == "aa" or k == "e" or k == "c":
		down[k] = v






'''
Κατασκευάζει από τα διαστήματα [-5, -2] με σώμα a και τα ίδια με σώμα aa.
ae2 ae3 aae2 aae3 ac4 ac5 aac4 aac5
'''
interval_m5_m2 = dict()	#temp variable. ποιο μετά θα συχωνευτεί και θα σβηστεί
for downPneuma in [container["e"], container["c"]]:
	for downSoma in [container["a"], container["aa"]]:
		keys = []
		keys.append(downSoma.user_value[0] + downPneuma.user_value[0] + str(abs(downPneuma.interval[0])))
		keys.append(downSoma.user_value[0] + str(abs(downPneuma.interval[0])))
		VoicedUnit_obj = VoicedUnit(downSoma.voiced_signs + downPneuma.voiced_signs,[downPneuma.interval[0]], keys)
		for key in keys:
			interval_m5_m2[key] = VoicedUnit_obj
		
			
			
		keys = []
		keys.append(downSoma.user_value[0] + downPneuma.user_value[0] + str(abs(downPneuma.interval[0] -1)))
		keys.append(downSoma.user_value[0] + str(abs(downPneuma.interval[0] -1)))
		VoicedUnit_obj = VoicedUnit(downSoma.voiced_signs + downPneuma.voiced_signs,[downPneuma.interval[0] -1], keys)
		for key in keys:
			interval_m5_m2[key] = VoicedUnit_obj
	
	
	
'''
Κατασκευάζει από τα διαστήματα [-13, -6] με σώμα a και τα ίδια με σώμα aa.
aec6 aecc10 aec7 aecc11 aaec6 aaecc10 aaec7 aaecc11 acc8 accc12 acc9 accc13 aacc8 aaccc12 aacc9 aaccc13
'''
interval_m13_m6 = dict()	#temp variable. ποιο μετά θα συχωνευτεί και θα σβηστεί
for k, v in interval_m5_m2.items():
	
	keys = []
	keys.append(	v.user_value[0][0:-1] + container["c"].user_value[0] + str(abs(v.interval[0]-4))		)
	keys.append(	v.user_value[-1][0:-1] + str(abs(v.interval[0]-4))		)
	VoicedUnit_obj = VoicedUnit(v.voiced_signs + container["c"].voiced_signs,[v.interval[0] -4],keys)
	for key in keys:
		interval_m13_m6[key] = VoicedUnit_obj
		
		
	keys = []
	keys.append(	v.user_value[0][0:-1] + container["c"].user_value[0] + container["c"].user_value[0] + str(abs(v.interval[0]-8))		)
	keys.append(	v.user_value[-1][0:-1] + str(abs(v.interval[0]-8))		)
	VoicedUnit_obj = VoicedUnit(v.voiced_signs + container["c"].voiced_signs + container["c"].voiced_signs,[v.interval[0] -8],keys)
	for key in keys:
		interval_m13_m6[key] = VoicedUnit_obj
	
	
	
	
	
#merger and delete the previous one variables
interval_m13_m2 = dict()	#temp variable. ποιο μετά θα συχωνευτεί και θα σβηστεί
	
for k,v in interval_m5_m2.items():
	interval_m13_m2[k] = v
		
for k,v in interval_m13_m6.items():
	interval_m13_m2[k] = v
	
del(interval_m5_m2)
del(interval_m13_m6)
	
	
	
	
	

temp_list  = [
	VoicedUnit(['e', 'c'],[-6],['-6', 'ec']),
	VoicedUnit(['e', 'c', 'c'],[-10],['-10', 'ecc']),
	VoicedUnit(['c', 'c'],[-8],['-8', 'cc']),
	VoicedUnit(['c', 'c', 'c'],[-12],['-12', 'ccc'])
	]
	
	
downPneumaWSoma = dict()
for temp_voiced_unit in temp_list:
	for key in temp_voiced_unit.user_value:
		downPneumaWSoma[key] = temp_voiced_unit
	
	
	
	
#merger and delete the previous one variables
interval_m13_m2_and_without_soma = {**interval_m13_m2 , **downPneumaWSoma}
del(interval_m13_m2)
del(downPneumaWSoma)
	
	
		
	
	
	
interval_p2_p5 = dict()
temp1 = {**oligon_type, **petasthe_type}#temp variable
temp2 = {container["k"], container["h"]}#temp variable

for k1,v1 in temp1.items():
	for v2 in temp2:
		t1 = [
			v1.user_value[0] + v2.user_value[0] + str(v2.interval[0]),
			v1.user_value[0] + str(v2.interval[0])
		]	#temp variable
			
		if t1[-1] in ['p2', 'pp2', 'ppp2']:
			del(t1[-1])
		
		t2 = [
			v1.user_value[0] + v2.user_value[0] + str(v2.interval[0]+1),
			v1.user_value[0] + str(v2.interval[0]+1)
		]	#temp variable
			
		
		VoicedUnit_obj = VoicedUnit(v1.voiced_signs + v2.voiced_signs, v2.interval, t1)
		for key in VoicedUnit_obj.user_value:
			interval_p2_p5[key] = VoicedUnit_obj
		
		VoicedUnit_obj = VoicedUnit(v1.voiced_signs + v2.voiced_signs, [v2.interval[0]+1], t2)
		for key in VoicedUnit_obj.user_value:
			interval_p2_p5[key] = VoicedUnit_obj
				

del(temp1)
del(temp2)
del(t1)
del(t2)
	
	
	
	
	
temp_list = [] #temp variable
temp_list.append( VoicedUnit(["k","h"], [6], ["kh6", '6']) )
temp_list.append( VoicedUnit(["k","h"], [7], ["kh7", '7']) )
temp_list.append( VoicedUnit(["h","h"], [8], ["hh", '8']) )
temp_list.append( VoicedUnit(["kk","h","h"], [9], ["kkhh", '9']) )
temp_list.append( VoicedUnit(["k","h","h"], [10], ["khh", '10']) )
temp_list.append( VoicedUnit(["h","k","h"], [11], ["hkh", '11']) )
temp_list.append( VoicedUnit(["h","h","h"], [12], ["hhh", '12']) )


interval_p6_p12_without_soma = dict() #temp variable
for temp_voiced_unit in temp_list:
	for key in temp_voiced_unit.user_value:
		interval_p6_p12_without_soma[key] = temp_voiced_unit


interval_p6_p12 = dict()#temp variable
temp1 = {**oligon_type, **petasthe_type}#temp variable
for k1,v1 in temp1.items():
	for k2,v2 in interval_p6_p12_without_soma.items():
		temp2 = [v1.user_value[0] + v2.user_value[0], v1.user_value[0] + v2.user_value[1]]
		
		VoicedUnit_obj = VoicedUnit(v1.voiced_signs+v2.voiced_signs, v2.interval, temp2)
		for key in VoicedUnit_obj.user_value:
			interval_p6_p12[key] = VoicedUnit_obj
	
del(temp1)
del(temp2)
	
	
#merger and delete the previous one variables
interval_p2_p12 = {**interval_p2_p5, **interval_p6_p12}
del(interval_p2_p5)
del(interval_p6_p12)
	
	
	
	
	
petasthe_type_with_oligon_type = dict()
for k, v in petasthe_type.items():
	t1 = [v.user_value[0] + container["o"].user_value[0], v.user_value[0] + '2']		#temp variable
	
	VoicedUnit_obj = VoicedUnit(v.voiced_signs + container["o"].voiced_signs, [v.interval[0] + container["o"].interval[0]], t1)
	for key in VoicedUnit_obj.user_value:
		petasthe_type_with_oligon_type[key] = VoicedUnit_obj
del(t1)
	
	
	
	
	
	
	
	
	
	
# oh4kk oh5kk ok2kk ok3kk ooh4kk ooh5kk ook2kk ook3kk ph4kk ph5kk pk2kk
# pk3kk pph4kk pph5kk ppk2kk ppk3kk ppph4kk ppph5kk pppk2kk pppk3kk pokk
# pookk ppokk ppookk pppokk pppookk
up_interval_with_kk = dict()
t1 = {**interval_p2_p12, **petasthe_type_with_oligon_type}
for k, v in t1.items():
	lenName = len(v.voiced_signs)
	if lenName < 3:
		t2 = []
		for every_user_value in v.user_value:
			t2 .append(every_user_value + container["kk"].user_value[0])
			
			
			
		VoicedUnit_obj = VoicedUnit(v.voiced_signs + container["kk"].voiced_signs, v.interval+[1], t2)
		for key in VoicedUnit_obj.user_value:
			up_interval_with_kk[key] = VoicedUnit_obj
	
	
	
	
	inteval_m13_m2_under_up_soma = dict()
	temp1 = {**oligon_type, **petasthe_type}#temp variable
	temp2 = {**down, **interval_m13_m2_and_without_soma}
	for k1, v1 in temp1.items():
		for k2, v2 in temp2.items():
			temp3 = []
			for every_user_value in v2.user_value:
				temp3.append(v1.user_value[0] + every_user_value)
				
				
			VoicedUnit_obj = VoicedUnit(v1.voiced_signs + v2.voiced_signs, v2.interval, temp3)
			for key in VoicedUnit_obj.user_value:
				inteval_m13_m2_under_up_soma[key] = VoicedUnit_obj
del(temp1)
del(temp2)
del(temp3)
	
	
	
	
	
	
isonUnderUpSoma = dict()
temp1 = {**oligon_type, **petasthe_type}		#temp variable
for k, v in temp1.items():
	temp2 = [
		v.user_value[0] + container["i"].user_value[0],
		v.user_value[0] + '0'
		]
	VoicedUnit_obj = VoicedUnit(v.voiced_signs + container["i"].voiced_signs, container["i"].interval, temp2)
	for key in VoicedUnit_obj.user_value:
		isonUnderUpSoma[key] = VoicedUnit_obj




del(temp1)
del(temp2)
	
	
	
	
downNeumeUnderUpSomaPluskk = dict()
temp1 = {**inteval_m13_m2_under_up_soma, **oligon_type, **petasthe_type, **apostrophos_type, **down}
for k, v in temp1.items():
	temp2 = []
	for every_user_value in v.user_value:
		temp2.append(every_user_value + container["kk"].user_value[0])
	
	VoicedUnit_obj = VoicedUnit(v.voiced_signs + container["kk"].voiced_signs, v.interval + container["kk"].interval, temp2)
	for key in VoicedUnit_obj.user_value:
		downNeumeUnderUpSomaPluskk[key] = VoicedUnit_obj
		
del(temp1)
del(temp2)
	
	
temp_rest = [
	VoicedUnit(["o","i","kk"], [0,1], ["oikk", 'o0kk']),
	VoicedUnit(["oo","i","kk"], [0,1], ["ooikk", 'oo0kk']),
	VoicedUnit(["p","i","kk"], [0,1], ["pikk", 'p0kk']),
	VoicedUnit(["pp","i","kk"], [0,1], ["ppikk", 'pp0kk']),
	VoicedUnit(["ppp","i","kk"], [0,1], ["pppikk", 'ppp0kk']),
	VoicedUnit(["kk","oo","i"], [1,0], ["kkooi", "kkoo0"]),
	VoicedUnit(["kk","o","i"], [1,0], ["kkoi", "kko0"])
	]
	

rest =  {
	"oikk": temp_rest[0],
	"o0kk": temp_rest[0],
	"ooikk": temp_rest[1],
	"oo0kk": temp_rest[1],
	"pikk": temp_rest[2],
	"p0kk": temp_rest[2],
	"ppikk": temp_rest[3],
	"pp0kk": temp_rest[3],
	"pppikk": temp_rest[4],
	"ppp0kk": temp_rest[4],
	
	"kkoo": VoicedUnit(["kk","oo"], [1,1], ["kkoo"]),
	"kko": VoicedUnit(["kk","o"], [1,1], ["kko"]),
	
	"kkooi": temp_rest[5],	#δεν ξέρω αν η μετροφωνία είναι αυτή που γράφω
	"kkoo0": temp_rest[5],
	"kkoi": temp_rest[6], #δεν ξέρω αν η μετροφωνία είναι αυτή που γράφω
	"kko0": temp_rest[6]
	}
	
	
	
del(temp_rest)

voiced_units = {
	**container,
	**isonUnderUpSoma,
	**container,
	**interval_m13_m2_and_without_soma,
	**interval_p2_p12,
	**petasthe_type_with_oligon_type,
	**up_interval_with_kk,
	**inteval_m13_m2_under_up_soma,
	**downNeumeUnderUpSomaPluskk,
	**rest
	}
del(interval_m13_m2_and_without_soma)
del(interval_p2_p12)
del(petasthe_type_with_oligon_type)
del(up_interval_with_kk)
del(inteval_m13_m2_under_up_soma)
del(downNeumeUnderUpSomaPluskk)
del(isonUnderUpSoma)
del(rest)


'''

f = open('all_the_voiced_units2.txt', 'w')
for key, value in voiced_units.items():
	f.write(str(value) + "\n")
f.close()
'''




	

#==============================================================================
class TestTracker(unittest.TestCase):
	def test_the_tree_constructor(self):
		self.assertEqual(voiced_units.get('oikk'), voiced_units.get( 'o0kk'))
		self.assertEqual(voiced_units.get('ooikk'), voiced_units.get( 'oo0kk'))
		self.assertEqual(voiced_units.get('pikk'), voiced_units.get( 'p0kk'))
		self.assertEqual(voiced_units.get('ppikk'), voiced_units.get( 'pp0kk'))
		self.assertEqual(voiced_units.get('pppikk'), voiced_units.get( 'ppp0kk'))

		
		
		
		self.assertEqual("i" in voiced_units.get("i").user_value, True)
		self.assertEqual("oo" in voiced_units.get("oo").user_value, True)
		self.assertEqual("ooh5" in voiced_units.get("ooh5").user_value, True)
		self.assertEqual("oo5" in voiced_units.get("ooh5").user_value, True)
		self.assertEqual("ooakk" in voiced_units.get("ooakk").user_value, True)
		self.assertEqual("kkoo" in voiced_units.get("kkoo").user_value, True)
		self.assertEqual("ookk" in voiced_units.get("ookk").user_value, True)
		self.assertEqual("s" in voiced_units.get("s").user_value, True)

		self.assertEqual(voiced_units.get('oi'), voiced_units.get('o0'))
		self.assertEqual(voiced_units.get('ooi'), voiced_units.get('oo0'))
		self.assertEqual(voiced_units.get('pi'), voiced_units.get('p0'))
		self.assertEqual(voiced_units.get('ppi'), voiced_units.get('pp0'))
		self.assertEqual(voiced_units.get('pppi'), voiced_units.get('ppp0'))
		self.assertEqual(voiced_units.get('e'), voiced_units.get('-2'))
		self.assertEqual(voiced_units.get('c'), voiced_units.get('-4'))
		self.assertEqual(voiced_units.get('ae2'), voiced_units.get('a2'))
		self.assertEqual(voiced_units.get('ae3'), voiced_units.get('a3'))
		self.assertEqual(voiced_units.get('aae2'), voiced_units.get('aa2'))
		self.assertEqual(voiced_units.get('aae3'), voiced_units.get('aa3'))
		self.assertEqual(voiced_units.get('ac4'), voiced_units.get('a4'))
		self.assertEqual(voiced_units.get('ac5'), voiced_units.get('a5'))
		self.assertEqual(voiced_units.get('aac4'), voiced_units.get('aa4'))
		self.assertEqual(voiced_units.get('aac5'), voiced_units.get('aa5'))
		self.assertEqual(voiced_units.get('aec6'), voiced_units.get('a6'))
		self.assertEqual(voiced_units.get('aecc10'), voiced_units.get('a10'))
		self.assertEqual(voiced_units.get('aec7'), voiced_units.get('a7'))
		self.assertEqual(voiced_units.get('aecc11'), voiced_units.get('a11'))
		self.assertEqual(voiced_units.get('aaec6'), voiced_units.get('aa6'))
		self.assertEqual(voiced_units.get('aaecc10'), voiced_units.get('aa10'))
		self.assertEqual(voiced_units.get('aaec7'), voiced_units.get('aa7'))
		self.assertEqual(voiced_units.get('aaecc11'), voiced_units.get('aa11'))
		self.assertEqual(voiced_units.get('acc8'), voiced_units.get('a8'))
		self.assertEqual(voiced_units.get('accc12'), voiced_units.get('a12'))
		self.assertEqual(voiced_units.get('acc9'), voiced_units.get('a9'))
		self.assertEqual(voiced_units.get('accc13'), voiced_units.get('a13'))
		self.assertEqual(voiced_units.get('aacc8'), voiced_units.get('aa8'))
		self.assertEqual(voiced_units.get('aaccc12'), voiced_units.get('aa12'))
		self.assertEqual(voiced_units.get('aacc9'), voiced_units.get('aa9'))
		self.assertEqual(voiced_units.get('aaccc13'), voiced_units.get('aa13'))
		self.assertEqual(voiced_units.get('-6'), voiced_units.get('ec'))
		self.assertEqual(voiced_units.get('-10'), voiced_units.get('ecc'))
		self.assertEqual(voiced_units.get('-8'), voiced_units.get('cc'))
		self.assertEqual(voiced_units.get('-12'), voiced_units.get('ccc'))
		self.assertEqual(voiced_units.get('oh4'), voiced_units.get('o4'))
		self.assertEqual(voiced_units.get('oh5'), voiced_units.get('o5'))
		self.assertEqual(voiced_units.get('ok2'), voiced_units.get('o2'))
		self.assertEqual(voiced_units.get('ok3'), voiced_units.get('o3'))
		self.assertEqual(voiced_units.get('ooh4'), voiced_units.get('oo4'))
		self.assertEqual(voiced_units.get('ooh5'), voiced_units.get('oo5'))
		self.assertEqual(voiced_units.get('ook2'), voiced_units.get('oo2'))
		self.assertEqual(voiced_units.get('ook3'), voiced_units.get('oo3'))
		self.assertEqual(voiced_units.get('ph4'), voiced_units.get('p4'))
		self.assertEqual(voiced_units.get('ph5'), voiced_units.get('p5'))
		self.assertEqual(voiced_units.get('pk3'), voiced_units.get('p3'))
		self.assertEqual(voiced_units.get('pph4'), voiced_units.get('pp4'))
		self.assertEqual(voiced_units.get('pph5'), voiced_units.get('pp5'))
		self.assertEqual(voiced_units.get('ppk3'), voiced_units.get('pp3'))
		self.assertEqual(voiced_units.get('ppph4'), voiced_units.get('ppp4'))
		self.assertEqual(voiced_units.get('ppph5'), voiced_units.get('ppp5'))
		self.assertEqual(voiced_units.get('pppk3'), voiced_units.get('ppp3'))
		self.assertEqual(voiced_units.get('okh6'), voiced_units.get('o6'))
		self.assertEqual(voiced_units.get('okh7'), voiced_units.get('o7'))
		self.assertEqual(voiced_units.get('ohh'), voiced_units.get('o8'))
		self.assertEqual(voiced_units.get('okkhh'), voiced_units.get('o9'))
		self.assertEqual(voiced_units.get('okhh'), voiced_units.get('o10'))
		self.assertEqual(voiced_units.get('ohkh'), voiced_units.get('o11'))
		self.assertEqual(voiced_units.get('ohhh'), voiced_units.get('o12'))
		self.assertEqual(voiced_units.get('ookh6'), voiced_units.get('oo6'))
		self.assertEqual(voiced_units.get('ookh7'), voiced_units.get('oo7'))
		self.assertEqual(voiced_units.get('oohh'), voiced_units.get('oo8'))
		self.assertEqual(voiced_units.get('ookkhh'), voiced_units.get('oo9'))
		self.assertEqual(voiced_units.get('ookhh'), voiced_units.get('oo10'))
		self.assertEqual(voiced_units.get('oohkh'), voiced_units.get('oo11'))
		self.assertEqual(voiced_units.get('oohhh'), voiced_units.get('oo12'))
		self.assertEqual(voiced_units.get('pkh6'), voiced_units.get('p6'))
		self.assertEqual(voiced_units.get('pkh7'), voiced_units.get('p7'))
		self.assertEqual(voiced_units.get('phh'), voiced_units.get('p8'))
		self.assertEqual(voiced_units.get('pkkhh'), voiced_units.get('p9'))
		self.assertEqual(voiced_units.get('pkhh'), voiced_units.get('p10'))
		self.assertEqual(voiced_units.get('phkh'), voiced_units.get('p11'))
		self.assertEqual(voiced_units.get('phhh'), voiced_units.get('p12'))
		self.assertEqual(voiced_units.get('ppkh6'), voiced_units.get('pp6'))
		self.assertEqual(voiced_units.get('ppkh7'), voiced_units.get('pp7'))
		self.assertEqual(voiced_units.get('pphh'), voiced_units.get('pp8'))
		self.assertEqual(voiced_units.get('ppkkhh'), voiced_units.get('pp9'))
		self.assertEqual(voiced_units.get('ppkhh'), voiced_units.get('pp10'))
		self.assertEqual(voiced_units.get('pphkh'), voiced_units.get('pp11'))
		self.assertEqual(voiced_units.get('pphhh'), voiced_units.get('pp12'))
		self.assertEqual(voiced_units.get('pppkh6'), voiced_units.get('ppp6'))
		self.assertEqual(voiced_units.get('pppkh7'), voiced_units.get('ppp7'))
		self.assertEqual(voiced_units.get('ppphh'), voiced_units.get('ppp8'))
		self.assertEqual(voiced_units.get('pppkkhh'), voiced_units.get('ppp9'))
		self.assertEqual(voiced_units.get('pppkhh'), voiced_units.get('ppp10'))
		self.assertEqual(voiced_units.get('ppphkh'), voiced_units.get('ppp11'))
		self.assertEqual(voiced_units.get('ppphhh'), voiced_units.get('ppp12'))
		self.assertEqual(voiced_units.get('po'), voiced_units.get('p2'))
		self.assertEqual(voiced_units.get('ppo'), voiced_units.get('pp2'))
		self.assertEqual(voiced_units.get('pppo'), voiced_units.get('ppp2'))
		self.assertEqual(voiced_units.get('oh4kk'), voiced_units.get('o4kk'))
		self.assertEqual(voiced_units.get('oh5kk'), voiced_units.get('o5kk'))
		self.assertEqual(voiced_units.get('ok2kk'), voiced_units.get('o2kk'))
		self.assertEqual(voiced_units.get('ok3kk'), voiced_units.get('o3kk'))
		self.assertEqual(voiced_units.get('ooh4kk'), voiced_units.get('oo4kk'))
		self.assertEqual(voiced_units.get('ooh5kk'), voiced_units.get('oo5kk'))
		self.assertEqual(voiced_units.get('ook2kk'), voiced_units.get('oo2kk'))
		self.assertEqual(voiced_units.get('ook3kk'), voiced_units.get('oo3kk'))
		self.assertEqual(voiced_units.get('ph4kk'), voiced_units.get('p4kk'))
		self.assertEqual(voiced_units.get('ph5kk'), voiced_units.get('p5kk'))
		self.assertEqual(voiced_units.get('pk3kk'), voiced_units.get('p3kk'))
		self.assertEqual(voiced_units.get('pph4kk'), voiced_units.get('pp4kk'))
		self.assertEqual(voiced_units.get('pph5kk'), voiced_units.get('pp5kk'))
		self.assertEqual(voiced_units.get('ppk3kk'), voiced_units.get('pp3kk'))
		self.assertEqual(voiced_units.get('ppph4kk'), voiced_units.get('ppp4kk'))
		self.assertEqual(voiced_units.get('ppph5kk'), voiced_units.get('ppp5kk'))
		self.assertEqual(voiced_units.get('pppk3kk'), voiced_units.get('ppp3kk'))
		self.assertEqual(voiced_units.get('pokk'), voiced_units.get('p2kk'))
		self.assertEqual(voiced_units.get('ppokk'), voiced_units.get('pp2kk'))
		self.assertEqual(voiced_units.get('pppokk'), voiced_units.get('ppp2kk'))
		self.assertEqual(voiced_units.get('oe'), voiced_units.get('o-2'))
		self.assertEqual(voiced_units.get('oc'), voiced_units.get('o-4'))
		self.assertEqual(voiced_units.get('oae2'), voiced_units.get('oa2'))
		self.assertEqual(voiced_units.get('oae3'), voiced_units.get('oa3'))
		self.assertEqual(voiced_units.get('oaae2'), voiced_units.get('oaa2'))
		self.assertEqual(voiced_units.get('oaae3'), voiced_units.get('oaa3'))
		self.assertEqual(voiced_units.get('oac4'), voiced_units.get('oa4'))
		self.assertEqual(voiced_units.get('oac5'), voiced_units.get('oa5'))
		self.assertEqual(voiced_units.get('oaac4'), voiced_units.get('oaa4'))
		self.assertEqual(voiced_units.get('oaac5'), voiced_units.get('oaa5'))
		self.assertEqual(voiced_units.get('oaec6'), voiced_units.get('oa6'))
		self.assertEqual(voiced_units.get('oaecc10'), voiced_units.get('oa10'))
		self.assertEqual(voiced_units.get('oaec7'), voiced_units.get('oa7'))
		self.assertEqual(voiced_units.get('oaecc11'), voiced_units.get('oa11'))
		self.assertEqual(voiced_units.get('oaaec6'), voiced_units.get('oaa6'))
		self.assertEqual(voiced_units.get('oaaecc10'), voiced_units.get('oaa10'))
		self.assertEqual(voiced_units.get('oaaec7'), voiced_units.get('oaa7'))
		self.assertEqual(voiced_units.get('oaaecc11'), voiced_units.get('oaa11'))
		self.assertEqual(voiced_units.get('oacc8'), voiced_units.get('oa8'))
		self.assertEqual(voiced_units.get('oaccc12'), voiced_units.get('oa12'))
		self.assertEqual(voiced_units.get('oacc9'), voiced_units.get('oa9'))
		self.assertEqual(voiced_units.get('oaccc13'), voiced_units.get('oa13'))
		self.assertEqual(voiced_units.get('oaacc8'), voiced_units.get('oaa8'))
		self.assertEqual(voiced_units.get('oaaccc12'), voiced_units.get('oaa12'))
		self.assertEqual(voiced_units.get('oaacc9'), voiced_units.get('oaa9'))
		self.assertEqual(voiced_units.get('oaaccc13'), voiced_units.get('oaa13'))
		self.assertEqual(voiced_units.get('o-6'), voiced_units.get('oec'))
		self.assertEqual(voiced_units.get('o-10'), voiced_units.get('oecc'))
		self.assertEqual(voiced_units.get('o-8'), voiced_units.get('occ'))
		self.assertEqual(voiced_units.get('o-12'), voiced_units.get('occc'))
		self.assertEqual(voiced_units.get('ooe'), voiced_units.get('oo-2'))
		self.assertEqual(voiced_units.get('ooc'), voiced_units.get('oo-4'))
		self.assertEqual(voiced_units.get('ooae2'), voiced_units.get('ooa2'))
		self.assertEqual(voiced_units.get('ooae3'), voiced_units.get('ooa3'))
		self.assertEqual(voiced_units.get('ooaae2'), voiced_units.get('ooaa2'))
		self.assertEqual(voiced_units.get('ooaae3'), voiced_units.get('ooaa3'))
		self.assertEqual(voiced_units.get('ooac4'), voiced_units.get('ooa4'))
		self.assertEqual(voiced_units.get('ooac5'), voiced_units.get('ooa5'))
		self.assertEqual(voiced_units.get('ooaac4'), voiced_units.get('ooaa4'))
		self.assertEqual(voiced_units.get('ooaac5'), voiced_units.get('ooaa5'))
		self.assertEqual(voiced_units.get('ooaec6'), voiced_units.get('ooa6'))
		self.assertEqual(voiced_units.get('ooaecc10'), voiced_units.get('ooa10'))
		self.assertEqual(voiced_units.get('ooaec7'), voiced_units.get('ooa7'))
		self.assertEqual(voiced_units.get('ooaecc11'), voiced_units.get('ooa11'))
		self.assertEqual(voiced_units.get('ooaaec6'), voiced_units.get('ooaa6'))
		self.assertEqual(voiced_units.get('ooaaecc10'), voiced_units.get('ooaa10'))
		self.assertEqual(voiced_units.get('ooaaec7'), voiced_units.get('ooaa7'))
		self.assertEqual(voiced_units.get('ooaaecc11'), voiced_units.get('ooaa11'))
		self.assertEqual(voiced_units.get('ooacc8'), voiced_units.get('ooa8'))
		self.assertEqual(voiced_units.get('ooaccc12'), voiced_units.get('ooa12'))
		self.assertEqual(voiced_units.get('ooacc9'), voiced_units.get('ooa9'))
		self.assertEqual(voiced_units.get('ooaccc13'), voiced_units.get('ooa13'))
		self.assertEqual(voiced_units.get('ooaacc8'), voiced_units.get('ooaa8'))
		self.assertEqual(voiced_units.get('ooaaccc12'), voiced_units.get('ooaa12'))
		self.assertEqual(voiced_units.get('ooaacc9'), voiced_units.get('ooaa9'))
		self.assertEqual(voiced_units.get('ooaaccc13'), voiced_units.get('ooaa13'))
		self.assertEqual(voiced_units.get('oo-6'), voiced_units.get('ooec'))
		self.assertEqual(voiced_units.get('oo-10'), voiced_units.get('ooecc'))
		self.assertEqual(voiced_units.get('oo-8'), voiced_units.get('oocc'))
		self.assertEqual(voiced_units.get('oo-12'), voiced_units.get('ooccc'))
		self.assertEqual(voiced_units.get('pe'), voiced_units.get('p-2'))
		self.assertEqual(voiced_units.get('pc'), voiced_units.get('p-4'))
		self.assertEqual(voiced_units.get('pae2'), voiced_units.get('pa2'))
		self.assertEqual(voiced_units.get('pae3'), voiced_units.get('pa3'))
		self.assertEqual(voiced_units.get('paae2'), voiced_units.get('paa2'))
		self.assertEqual(voiced_units.get('paae3'), voiced_units.get('paa3'))
		self.assertEqual(voiced_units.get('pac4'), voiced_units.get('pa4'))
		self.assertEqual(voiced_units.get('pac5'), voiced_units.get('pa5'))
		self.assertEqual(voiced_units.get('paac4'), voiced_units.get('paa4'))
		self.assertEqual(voiced_units.get('paac5'), voiced_units.get('paa5'))
		self.assertEqual(voiced_units.get('paec6'), voiced_units.get('pa6'))
		self.assertEqual(voiced_units.get('paecc10'), voiced_units.get('pa10'))
		self.assertEqual(voiced_units.get('paec7'), voiced_units.get('pa7'))
		self.assertEqual(voiced_units.get('paecc11'), voiced_units.get('pa11'))
		self.assertEqual(voiced_units.get('paaec6'), voiced_units.get('paa6'))
		self.assertEqual(voiced_units.get('paaecc10'), voiced_units.get('paa10'))
		self.assertEqual(voiced_units.get('paaec7'), voiced_units.get('paa7'))
		self.assertEqual(voiced_units.get('paaecc11'), voiced_units.get('paa11'))
		self.assertEqual(voiced_units.get('pacc8'), voiced_units.get('pa8'))
		self.assertEqual(voiced_units.get('paccc12'), voiced_units.get('pa12'))
		self.assertEqual(voiced_units.get('pacc9'), voiced_units.get('pa9'))
		self.assertEqual(voiced_units.get('paccc13'), voiced_units.get('pa13'))
		self.assertEqual(voiced_units.get('paacc8'), voiced_units.get('paa8'))
		self.assertEqual(voiced_units.get('paaccc12'), voiced_units.get('paa12'))
		self.assertEqual(voiced_units.get('paacc9'), voiced_units.get('paa9'))
		self.assertEqual(voiced_units.get('paaccc13'), voiced_units.get('paa13'))
		self.assertEqual(voiced_units.get('p-6'), voiced_units.get('pec'))
		self.assertEqual(voiced_units.get('p-10'), voiced_units.get('pecc'))
		self.assertEqual(voiced_units.get('p-8'), voiced_units.get('pcc'))
		self.assertEqual(voiced_units.get('p-12'), voiced_units.get('pccc'))
		self.assertEqual(voiced_units.get('ppe'), voiced_units.get('pp-2'))
		self.assertEqual(voiced_units.get('ppc'), voiced_units.get('pp-4'))
		self.assertEqual(voiced_units.get('ppae2'), voiced_units.get('ppa2'))
		self.assertEqual(voiced_units.get('ppae3'), voiced_units.get('ppa3'))
		self.assertEqual(voiced_units.get('ppaae2'), voiced_units.get('ppaa2'))
		self.assertEqual(voiced_units.get('ppaae3'), voiced_units.get('ppaa3'))
		self.assertEqual(voiced_units.get('ppac4'), voiced_units.get('ppa4'))
		self.assertEqual(voiced_units.get('ppac5'), voiced_units.get('ppa5'))
		self.assertEqual(voiced_units.get('ppaac4'), voiced_units.get('ppaa4'))
		self.assertEqual(voiced_units.get('ppaac5'), voiced_units.get('ppaa5'))
		self.assertEqual(voiced_units.get('ppaec6'), voiced_units.get('ppa6'))
		self.assertEqual(voiced_units.get('ppaecc10'), voiced_units.get('ppa10'))
		self.assertEqual(voiced_units.get('ppaec7'), voiced_units.get('ppa7'))
		self.assertEqual(voiced_units.get('ppaecc11'), voiced_units.get('ppa11'))
		self.assertEqual(voiced_units.get('ppaaec6'), voiced_units.get('ppaa6'))
		self.assertEqual(voiced_units.get('ppaaecc10'), voiced_units.get('ppaa10'))
		self.assertEqual(voiced_units.get('ppaaec7'), voiced_units.get('ppaa7'))
		self.assertEqual(voiced_units.get('ppaaecc11'), voiced_units.get('ppaa11'))
		self.assertEqual(voiced_units.get('ppacc8'), voiced_units.get('ppa8'))
		self.assertEqual(voiced_units.get('ppaccc12'), voiced_units.get('ppa12'))
		self.assertEqual(voiced_units.get('ppacc9'), voiced_units.get('ppa9'))
		self.assertEqual(voiced_units.get('ppaccc13'), voiced_units.get('ppa13'))
		self.assertEqual(voiced_units.get('ppaacc8'), voiced_units.get('ppaa8'))
		self.assertEqual(voiced_units.get('ppaaccc12'), voiced_units.get('ppaa12'))
		self.assertEqual(voiced_units.get('ppaacc9'), voiced_units.get('ppaa9'))
		self.assertEqual(voiced_units.get('ppaaccc13'), voiced_units.get('ppaa13'))
		self.assertEqual(voiced_units.get('pp-6'), voiced_units.get('ppec'))
		self.assertEqual(voiced_units.get('pp-10'), voiced_units.get('ppecc'))
		self.assertEqual(voiced_units.get('pp-8'), voiced_units.get('ppcc'))
		self.assertEqual(voiced_units.get('pp-12'), voiced_units.get('ppccc'))
		self.assertEqual(voiced_units.get('pppe'), voiced_units.get('ppp-2'))
		self.assertEqual(voiced_units.get('pppc'), voiced_units.get('ppp-4'))
		self.assertEqual(voiced_units.get('pppae2'), voiced_units.get('pppa2'))
		self.assertEqual(voiced_units.get('pppae3'), voiced_units.get('pppa3'))
		self.assertEqual(voiced_units.get('pppaae2'), voiced_units.get('pppaa2'))
		self.assertEqual(voiced_units.get('pppaae3'), voiced_units.get('pppaa3'))
		self.assertEqual(voiced_units.get('pppac4'), voiced_units.get('pppa4'))
		self.assertEqual(voiced_units.get('pppac5'), voiced_units.get('pppa5'))
		self.assertEqual(voiced_units.get('pppaac4'), voiced_units.get('pppaa4'))
		self.assertEqual(voiced_units.get('pppaac5'), voiced_units.get('pppaa5'))
		self.assertEqual(voiced_units.get('pppaec6'), voiced_units.get('pppa6'))
		self.assertEqual(voiced_units.get('pppaecc10'), voiced_units.get('pppa10'))
		self.assertEqual(voiced_units.get('pppaec7'), voiced_units.get('pppa7'))
		self.assertEqual(voiced_units.get('pppaecc11'), voiced_units.get('pppa11'))
		self.assertEqual(voiced_units.get('pppaaec6'), voiced_units.get('pppaa6'))
		self.assertEqual(voiced_units.get('pppaaecc10'), voiced_units.get('pppaa10'))
		self.assertEqual(voiced_units.get('pppaaec7'), voiced_units.get('pppaa7'))
		self.assertEqual(voiced_units.get('pppaaecc11'), voiced_units.get('pppaa11'))
		self.assertEqual(voiced_units.get('pppacc8'), voiced_units.get('pppa8'))
		self.assertEqual(voiced_units.get('pppaccc12'), voiced_units.get('pppa12'))
		self.assertEqual(voiced_units.get('pppacc9'), voiced_units.get('pppa9'))
		self.assertEqual(voiced_units.get('pppaccc13'), voiced_units.get('pppa13'))
		self.assertEqual(voiced_units.get('pppaacc8'), voiced_units.get('pppaa8'))
		self.assertEqual(voiced_units.get('pppaaccc12'), voiced_units.get('pppaa12'))
		self.assertEqual(voiced_units.get('pppaacc9'), voiced_units.get('pppaa9'))
		self.assertEqual(voiced_units.get('pppaaccc13'), voiced_units.get('pppaa13'))
		self.assertEqual(voiced_units.get('ppp-6'), voiced_units.get('pppec'))
		self.assertEqual(voiced_units.get('ppp-10'), voiced_units.get('pppecc'))
		self.assertEqual(voiced_units.get('ppp-8'), voiced_units.get('pppcc'))
		self.assertEqual(voiced_units.get('ppp-12'), voiced_units.get('pppccc'))
		self.assertEqual(voiced_units.get('oekk'), voiced_units.get('o-2kk'))
		self.assertEqual(voiced_units.get('ockk'), voiced_units.get('o-4kk'))
		self.assertEqual(voiced_units.get('oae2kk'), voiced_units.get('oa2kk'))
		self.assertEqual(voiced_units.get('oae3kk'), voiced_units.get('oa3kk'))
		self.assertEqual(voiced_units.get('oaae2kk'), voiced_units.get('oaa2kk'))
		self.assertEqual(voiced_units.get('oaae3kk'), voiced_units.get('oaa3kk'))
		self.assertEqual(voiced_units.get('oac4kk'), voiced_units.get('oa4kk'))
		self.assertEqual(voiced_units.get('oac5kk'), voiced_units.get('oa5kk'))
		self.assertEqual(voiced_units.get('oaac4kk'), voiced_units.get('oaa4kk'))
		self.assertEqual(voiced_units.get('oaac5kk'), voiced_units.get('oaa5kk'))
		self.assertEqual(voiced_units.get('oaec6kk'), voiced_units.get('oa6kk'))
		self.assertEqual(voiced_units.get('oaecc10kk'), voiced_units.get('oa10kk'))
		self.assertEqual(voiced_units.get('oaec7kk'), voiced_units.get('oa7kk'))
		self.assertEqual(voiced_units.get('oaecc11kk'), voiced_units.get('oa11kk'))
		self.assertEqual(voiced_units.get('oaaec6kk'), voiced_units.get('oaa6kk'))
		self.assertEqual(voiced_units.get('oaaecc10kk'), voiced_units.get('oaa10kk'))
		self.assertEqual(voiced_units.get('oaaec7kk'), voiced_units.get('oaa7kk'))
		self.assertEqual(voiced_units.get('oaaecc11kk'), voiced_units.get('oaa11kk'))
		self.assertEqual(voiced_units.get('oacc8kk'), voiced_units.get('oa8kk'))
		self.assertEqual(voiced_units.get('oaccc12kk'), voiced_units.get('oa12kk'))
		self.assertEqual(voiced_units.get('oacc9kk'), voiced_units.get('oa9kk'))
		self.assertEqual(voiced_units.get('oaccc13kk'), voiced_units.get('oa13kk'))
		self.assertEqual(voiced_units.get('oaacc8kk'), voiced_units.get('oaa8kk'))
		self.assertEqual(voiced_units.get('oaaccc12kk'), voiced_units.get('oaa12kk'))
		self.assertEqual(voiced_units.get('oaacc9kk'), voiced_units.get('oaa9kk'))
		self.assertEqual(voiced_units.get('oaaccc13kk'), voiced_units.get('oaa13kk'))
		self.assertEqual(voiced_units.get('o-6kk'), voiced_units.get('oeckk'))
		self.assertEqual(voiced_units.get('o-10kk'), voiced_units.get('oecckk'))
		self.assertEqual(voiced_units.get('o-8kk'), voiced_units.get('occkk'))
		self.assertEqual(voiced_units.get('o-12kk'), voiced_units.get('occckk'))
		self.assertEqual(voiced_units.get('ooekk'), voiced_units.get('oo-2kk'))
		self.assertEqual(voiced_units.get('oockk'), voiced_units.get('oo-4kk'))
		self.assertEqual(voiced_units.get('ooae2kk'), voiced_units.get('ooa2kk'))
		self.assertEqual(voiced_units.get('ooae3kk'), voiced_units.get('ooa3kk'))
		self.assertEqual(voiced_units.get('ooaae2kk'), voiced_units.get('ooaa2kk'))
		self.assertEqual(voiced_units.get('ooaae3kk'), voiced_units.get('ooaa3kk'))
		self.assertEqual(voiced_units.get('ooac4kk'), voiced_units.get('ooa4kk'))
		self.assertEqual(voiced_units.get('ooac5kk'), voiced_units.get('ooa5kk'))
		self.assertEqual(voiced_units.get('ooaac4kk'), voiced_units.get('ooaa4kk'))
		self.assertEqual(voiced_units.get('ooaac5kk'), voiced_units.get('ooaa5kk'))
		self.assertEqual(voiced_units.get('ooaec6kk'), voiced_units.get('ooa6kk'))
		self.assertEqual(voiced_units.get('ooaecc10kk'), voiced_units.get('ooa10kk'))
		self.assertEqual(voiced_units.get('ooaec7kk'), voiced_units.get('ooa7kk'))
		self.assertEqual(voiced_units.get('ooaecc11kk'), voiced_units.get('ooa11kk'))
		self.assertEqual(voiced_units.get('ooaaec6kk'), voiced_units.get('ooaa6kk'))
		self.assertEqual(voiced_units.get('ooaaecc10kk'), voiced_units.get('ooaa10kk'))
		self.assertEqual(voiced_units.get('ooaaec7kk'), voiced_units.get('ooaa7kk'))
		self.assertEqual(voiced_units.get('ooaaecc11kk'), voiced_units.get('ooaa11kk'))
		self.assertEqual(voiced_units.get('ooacc8kk'), voiced_units.get('ooa8kk'))
		self.assertEqual(voiced_units.get('ooaccc12kk'), voiced_units.get('ooa12kk'))
		self.assertEqual(voiced_units.get('ooacc9kk'), voiced_units.get('ooa9kk'))
		self.assertEqual(voiced_units.get('ooaccc13kk'), voiced_units.get('ooa13kk'))
		self.assertEqual(voiced_units.get('ooaacc8kk'), voiced_units.get('ooaa8kk'))
		self.assertEqual(voiced_units.get('ooaaccc12kk'), voiced_units.get('ooaa12kk'))
		self.assertEqual(voiced_units.get('ooaacc9kk'), voiced_units.get('ooaa9kk'))
		self.assertEqual(voiced_units.get('ooaaccc13kk'), voiced_units.get('ooaa13kk'))
		self.assertEqual(voiced_units.get('oo-6kk'), voiced_units.get('ooeckk'))
		self.assertEqual(voiced_units.get('oo-10kk'), voiced_units.get('ooecckk'))
		self.assertEqual(voiced_units.get('oo-8kk'), voiced_units.get('oocckk'))
		self.assertEqual(voiced_units.get('oo-12kk'), voiced_units.get('ooccckk'))
		self.assertEqual(voiced_units.get('pekk'), voiced_units.get('p-2kk'))
		self.assertEqual(voiced_units.get('pckk'), voiced_units.get('p-4kk'))
		self.assertEqual(voiced_units.get('pae2kk'), voiced_units.get('pa2kk'))
		self.assertEqual(voiced_units.get('pae3kk'), voiced_units.get('pa3kk'))
		self.assertEqual(voiced_units.get('paae2kk'), voiced_units.get('paa2kk'))
		self.assertEqual(voiced_units.get('paae3kk'), voiced_units.get('paa3kk'))
		self.assertEqual(voiced_units.get('pac4kk'), voiced_units.get('pa4kk'))
		self.assertEqual(voiced_units.get('pac5kk'), voiced_units.get('pa5kk'))
		self.assertEqual(voiced_units.get('paac4kk'), voiced_units.get('paa4kk'))
		self.assertEqual(voiced_units.get('paac5kk'), voiced_units.get('paa5kk'))
		self.assertEqual(voiced_units.get('paec6kk'), voiced_units.get('pa6kk'))
		self.assertEqual(voiced_units.get('paecc10kk'), voiced_units.get('pa10kk'))
		self.assertEqual(voiced_units.get('paec7kk'), voiced_units.get('pa7kk'))
		self.assertEqual(voiced_units.get('paecc11kk'), voiced_units.get('pa11kk'))
		self.assertEqual(voiced_units.get('paaec6kk'), voiced_units.get('paa6kk'))
		self.assertEqual(voiced_units.get('paaecc10kk'), voiced_units.get('paa10kk'))
		self.assertEqual(voiced_units.get('paaec7kk'), voiced_units.get('paa7kk'))
		self.assertEqual(voiced_units.get('paaecc11kk'), voiced_units.get('paa11kk'))
		self.assertEqual(voiced_units.get('pacc8kk'), voiced_units.get('pa8kk'))
		self.assertEqual(voiced_units.get('paccc12kk'), voiced_units.get('pa12kk'))
		self.assertEqual(voiced_units.get('pacc9kk'), voiced_units.get('pa9kk'))
		self.assertEqual(voiced_units.get('paccc13kk'), voiced_units.get('pa13kk'))
		self.assertEqual(voiced_units.get('paacc8kk'), voiced_units.get('paa8kk'))
		self.assertEqual(voiced_units.get('paaccc12kk'), voiced_units.get('paa12kk'))
		self.assertEqual(voiced_units.get('paacc9kk'), voiced_units.get('paa9kk'))
		self.assertEqual(voiced_units.get('paaccc13kk'), voiced_units.get('paa13kk'))
		self.assertEqual(voiced_units.get('p-6kk'), voiced_units.get('peckk'))
		self.assertEqual(voiced_units.get('p-10kk'), voiced_units.get('pecckk'))
		self.assertEqual(voiced_units.get('p-8kk'), voiced_units.get('pcckk'))
		self.assertEqual(voiced_units.get('p-12kk'), voiced_units.get('pccckk'))
		self.assertEqual(voiced_units.get('ppekk'), voiced_units.get('pp-2kk'))
		self.assertEqual(voiced_units.get('ppckk'), voiced_units.get('pp-4kk'))
		self.assertEqual(voiced_units.get('ppae2kk'), voiced_units.get('ppa2kk'))
		self.assertEqual(voiced_units.get('ppae3kk'), voiced_units.get('ppa3kk'))
		self.assertEqual(voiced_units.get('ppaae2kk'), voiced_units.get('ppaa2kk'))
		self.assertEqual(voiced_units.get('ppaae3kk'), voiced_units.get('ppaa3kk'))
		self.assertEqual(voiced_units.get('ppac4kk'), voiced_units.get('ppa4kk'))
		self.assertEqual(voiced_units.get('ppac5kk'), voiced_units.get('ppa5kk'))
		self.assertEqual(voiced_units.get('ppaac4kk'), voiced_units.get('ppaa4kk'))
		self.assertEqual(voiced_units.get('ppaac5kk'), voiced_units.get('ppaa5kk'))
		self.assertEqual(voiced_units.get('ppaec6kk'), voiced_units.get('ppa6kk'))
		self.assertEqual(voiced_units.get('ppaecc10kk'), voiced_units.get('ppa10kk'))
		self.assertEqual(voiced_units.get('ppaec7kk'), voiced_units.get('ppa7kk'))
		self.assertEqual(voiced_units.get('ppaecc11kk'), voiced_units.get('ppa11kk'))
		self.assertEqual(voiced_units.get('ppaaec6kk'), voiced_units.get('ppaa6kk'))
		self.assertEqual(voiced_units.get('ppaaecc10kk'), voiced_units.get('ppaa10kk'))
		self.assertEqual(voiced_units.get('ppaaec7kk'), voiced_units.get('ppaa7kk'))
		self.assertEqual(voiced_units.get('ppaaecc11kk'), voiced_units.get('ppaa11kk'))
		self.assertEqual(voiced_units.get('ppacc8kk'), voiced_units.get('ppa8kk'))
		self.assertEqual(voiced_units.get('ppaccc12kk'), voiced_units.get('ppa12kk'))
		self.assertEqual(voiced_units.get('ppacc9kk'), voiced_units.get('ppa9kk'))
		self.assertEqual(voiced_units.get('ppaccc13kk'), voiced_units.get('ppa13kk'))
		self.assertEqual(voiced_units.get('ppaacc8kk'), voiced_units.get('ppaa8kk'))
		self.assertEqual(voiced_units.get('ppaaccc12kk'), voiced_units.get('ppaa12kk'))
		self.assertEqual(voiced_units.get('ppaacc9kk'), voiced_units.get('ppaa9kk'))
		self.assertEqual(voiced_units.get('ppaaccc13kk'), voiced_units.get('ppaa13kk'))
		self.assertEqual(voiced_units.get('pp-6kk'), voiced_units.get('ppeckk'))
		self.assertEqual(voiced_units.get('pp-10kk'), voiced_units.get('ppecckk'))
		self.assertEqual(voiced_units.get('pp-8kk'), voiced_units.get('ppcckk'))
		self.assertEqual(voiced_units.get('pp-12kk'), voiced_units.get('ppccckk'))
		self.assertEqual(voiced_units.get('pppekk'), voiced_units.get('ppp-2kk'))
		self.assertEqual(voiced_units.get('pppckk'), voiced_units.get('ppp-4kk'))
		self.assertEqual(voiced_units.get('pppae2kk'), voiced_units.get('pppa2kk'))
		self.assertEqual(voiced_units.get('pppae3kk'), voiced_units.get('pppa3kk'))
		self.assertEqual(voiced_units.get('pppaae2kk'), voiced_units.get('pppaa2kk'))
		self.assertEqual(voiced_units.get('pppaae3kk'), voiced_units.get('pppaa3kk'))
		self.assertEqual(voiced_units.get('pppac4kk'), voiced_units.get('pppa4kk'))
		self.assertEqual(voiced_units.get('pppac5kk'), voiced_units.get('pppa5kk'))
		self.assertEqual(voiced_units.get('pppaac4kk'), voiced_units.get('pppaa4kk'))
		self.assertEqual(voiced_units.get('pppaac5kk'), voiced_units.get('pppaa5kk'))
		self.assertEqual(voiced_units.get('pppaec6kk'), voiced_units.get('pppa6kk'))
		self.assertEqual(voiced_units.get('pppaecc10kk'), voiced_units.get('pppa10kk'))
		self.assertEqual(voiced_units.get('pppaec7kk'), voiced_units.get('pppa7kk'))
		self.assertEqual(voiced_units.get('pppaecc11kk'), voiced_units.get('pppa11kk'))
		self.assertEqual(voiced_units.get('pppaaec6kk'), voiced_units.get('pppaa6kk'))
		self.assertEqual(voiced_units.get('pppaaecc10kk'), voiced_units.get('pppaa10kk'))
		self.assertEqual(voiced_units.get('pppaaec7kk'), voiced_units.get('pppaa7kk'))
		self.assertEqual(voiced_units.get('pppaaecc11kk'), voiced_units.get('pppaa11kk'))
		self.assertEqual(voiced_units.get('pppacc8kk'), voiced_units.get('pppa8kk'))
		self.assertEqual(voiced_units.get('pppaccc12kk'), voiced_units.get('pppa12kk'))
		self.assertEqual(voiced_units.get('pppacc9kk'), voiced_units.get('pppa9kk'))
		self.assertEqual(voiced_units.get('pppaccc13kk'), voiced_units.get('pppa13kk'))
		self.assertEqual(voiced_units.get('pppaacc8kk'), voiced_units.get('pppaa8kk'))
		self.assertEqual(voiced_units.get('pppaaccc12kk'), voiced_units.get('pppaa12kk'))
		self.assertEqual(voiced_units.get('pppaacc9kk'), voiced_units.get('pppaa9kk'))
		self.assertEqual(voiced_units.get('pppaaccc13kk'), voiced_units.get('pppaa13kk'))
		self.assertEqual(voiced_units.get('ppp-6kk'), voiced_units.get('pppeckk'))
		self.assertEqual(voiced_units.get('ppp-10kk'), voiced_units.get('pppecckk'))
		self.assertEqual(voiced_units.get('ppp-8kk'), voiced_units.get('pppcckk'))
		self.assertEqual(voiced_units.get('ppp-12kk'), voiced_units.get('pppccckk'))
		self.assertEqual(voiced_units.get('ekk'), voiced_units.get('-2kk'))
		self.assertEqual(voiced_units.get('ckk'), voiced_units.get('-4kk'))


if __name__ == '__main__':
	unittest.main()


