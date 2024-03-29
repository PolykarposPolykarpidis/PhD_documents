# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 12:47:28 2021

@author: polykarpos polykarpidis
"""
#see also https://plotly.com/python/3d-axes/
from itertools import product
import numpy as np
import math
import plotly.graph_objects as go
import plotly.express as px

def a_term_of_entropy(p):
	if p == 0:
		return 0
	return p * math.log2(p) * (-1)


product_test = list(product(np.arange(0.0, 1.01, 0.01), np.arange(0.0, 1.01, 0.01), np.arange(0.0, 1.01, 0.01)))
acceptable_triad = []

for i in product_test:
	if np.float64(1.0) ==  np.round(i[0]+ i[1]+ i[2], 2):
		acceptable_triad.append(i)
	
x = []
y = []
z = []


for i in acceptable_triad:
	x.append(i[0])
	y.append(i[1])
	z.append(a_term_of_entropy(i[0])+a_term_of_entropy(i[1])+a_term_of_entropy(i[2]))


fig = go.Figure(data=[go.Scatter3d(
	x=x,
	y=y,
	z=z,
	mode='markers',
	marker=dict(
		size=5,
		color=z,                # set color to an array/list of desired values
		colorscale='Turbo',   # choose a colorscale
		opacity=0.8
	)
)])


# tight layout
fig.update_layout(title='Εντροπία - Πιθανότητα μεταβλητής X τριών ενδεχομένων',
				  scene = dict(
					  xaxis_title='X = 1',
					  yaxis_title='X = 2',
					  zaxis_title='H(X)'),
				 margin=dict(l=20, r=20, b=20, t=100))


fig.write_html("test.html") #Modifiy the html file
fig.show()


