# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:53:35 2021

@author: polykarpos polykarpidis
"""

import numpy as np
import matplotlib.pyplot as plt

data_x = np.arange(-10.0, 10.0, 0.01)

plt.plot(data_x, data_x ** 2, label='f(x) = x^2')
plt.plot([-2,8], [4,64], marker='o', label='ευθύγραμμο τμήμα')
plt.title('Μία κυρτή συνάρτηση')
plt.legend()

plt.savefig('convex.png', bbox_inches='tight', dpi=600)
plt.close()



plt.plot(data_x, -(data_x ** 2), label='f(x) = -x^2')
plt.plot([-2,8], [-4,-64], marker='o', label='ευθύγραμμο τμήμα')
plt.title('Μία κοίλη συνάρτηση')
plt.legend()

plt.savefig('concave.png', bbox_inches='tight', dpi=600)
plt.close()




plt.plot(np.arange(-3* np.pi, 3*np.pi, 0.01), np.sin(np.arange(-3* np.pi, 3*np.pi, 0.01))/2, label='f(x) = sin(x)/2, [-3 * pi, 3* pi]')
for i in range(-3,4):
	plt.plot([i*np.pi,i*np.pi], [-1,1], color='black')
plt.title('Μία συνάρτηση κατά διαστήματα κυρτή και κοίλη')
plt.legend()

plt.savefig('concave-convex-d.png', bbox_inches='tight', dpi=600)
plt.close()








