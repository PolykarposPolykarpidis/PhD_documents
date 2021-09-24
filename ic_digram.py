# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 12:47:28 2021

@author: polykarpos polykarpidis
"""


import matplotlib.pyplot as plt
import numpy as np
import math
infinity = 10 #we consider as 10 the infinity

def ic(p):
	#We know that when p(X=x) = 0 then IC value is + infinity. But here we are putting a 'large' constant value to represent the infiity and we show only a part of y to give the sence of infinity
	if p == 0:
		return infinity
	return math.log2(p) * (-1)

test = list(np.arange(0.0, 1.01, 0.01))
information_content_x = [ic(x) for x in test]

plt.plot(test, information_content_x)
plt.title('IC - πιθανότητα')
plt.ylabel('IC')
plt.xlabel('p(X=x)')
plt.tight_layout()
plt.ylim([0.0, 8.0]) #we show only a part of y to give the sence of infinity



plt.savefig('ic.png', bbox_inches='tight', dpi=600)
plt.show()
