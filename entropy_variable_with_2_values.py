# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 12:47:28 2021

@author: polykarpos polykarpidis
"""
import matplotlib.pyplot as plt
import numpy as np
import math


def a_term_of_entropy(p):
	if p == 0:
		return 0
	return p * math.log2(p) * (-1)

test = list(np.arange(0.0, 1.01, 0.01))
pE = [a_term_of_entropy(x)+a_term_of_entropy(1-x) for x in test]

plt.plot(test, pE)
plt.title('Εντροπία - Πιθανότητα')
plt.ylabel('H(X)')
plt.xlabel('p(X=1)')
plt.tight_layout()
plt.savefig('entropy.png', bbox_inches='tight', dpi=600)
plt.show()
