# CSE 101 - IP HW2
# K-Map Minimization 
# Name: AYUSH GOEL
# Roll Number: 2018029
# Section: A
# Group: 5
# Date: 17/10/2018

import unittest
from HW2_2018xxx import minFunc



class testpoint(unittest.TestCase):
	#test1
	def test_minFunc1(self):
		self.assertTrue("xy+w",minFunc(4,"(a6,a7,a8,a9) d(d10,d11,d12,d13,d14,d15)"))
	#test2
	def test_minFunc2(self):	
		self.assertTrue("x'",minFunc(3,"(a0,a1) d(d2,d3)"))
	#test3
	def test_minFunc3(self):	
		self.assertTrue("z'",minFunc(2,"(a2) d(d0)"))
	#test4
	def test_minFunc4(self):	
		self.assertTrue("z",minFunc(1,"(a1)"))
	#test5
	def test_minFunc5(self):	
		self.assertTrue("w'x'+x'y'z+xy'z'",minFunc(4,"(a0,a1,a2,a3,a9,a12) d(d4,d5,d6)"))
	#test6
	def test_minFunc6(self):
		self.assertTrue('1',minFunc(3,"(a0,a1,a2,a3,a4,a5) d(d6,d7)"))
	#test7
	def test_minFunc7(self):
		self.assertTrue('0',minFunc(3,"(-) d(-)"))
	


if __name__=='__main__':
	unittest.main()
