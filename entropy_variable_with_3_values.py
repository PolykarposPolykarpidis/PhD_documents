# -*- coding: utf-8 -*-

from itertools import product
import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits import mplot3d
import matplotlib.animation as animation


def a_term_of_entropy(p):
	if p == 0:
		return 0
	return p * math.log2(p) * (-1)


test = np.arange(0.0, 1.01, 0.01)
print(len(test))
product_test = list(product(test, test, test))
acceptable_triad = []

for i in product_test:
	if sum(i) == 1:
		acceptable_triad.append(i)
		
x = []
y = []
z = []

for i in acceptable_triad:
	x.append(i[0])
	y.append(i[1])
	z.append(a_term_of_entropy(i[0])+a_term_of_entropy(i[1])+a_term_of_entropy(i[2]))

ax = plt.axes(projection="3d")



#ax.plot3D(x,y,z, label='Εντροπία - Πιθανότητα')



#for colourfull scater diagram
#1 colored by value of `z`
ax.scatter(x, y, z, c = plt.cm.jet(z/max(z))) 


ax.set_xlabel('x = 1')
ax.set_ylabel('x = 2')
ax.set_zlabel('H(X)', rotation = 0)
plt.show()

