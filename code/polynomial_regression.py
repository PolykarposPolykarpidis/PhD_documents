# Regression with 2nd degree Polynomial

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from abcd import pitch_list
import os

def polynomial_regression(x_temp, y_temp):
	#font = {'size': 7}

	#plt.rc('font', **font)
	#plt.rcParams['figure.figsize'] = (2,2) # αυτή η γραμμή κώδικα μικραίνει το μέγεθος του plot
	# Importing the dataset
	x_t = list()
	x_t.append(x_temp)	
	X = np.transpose(np.array(x_t))
	y = np.array(y_temp)
	
	
	# Training the Polynomial Regression model on the whole dataset
	from sklearn.preprocessing import PolynomialFeatures
	poly_reg = PolynomialFeatures(degree = 2)
	X_poly = poly_reg.fit_transform(X)
	lin_reg_2 = LinearRegression()
	lin_reg_2.fit(X_poly, y)
	
	
	
	# Visualising the Polynomial Regression results
	X_grid = np.arange(min(X), max(X), 0.1)
	X_grid = X_grid.reshape((len(X_grid), 1))
	plt.plot(X, y, color = 'darkorange')
	model = lin_reg_2.predict(poly_reg.fit_transform(X_grid))
	plt.plot(X_grid, model, color = 'red')
	
	plt.xticks([i for i in X])
	
	y_ticks = list(range(min(y), max(y)+1))
	plt.yticks(y_ticks, pitch_list[y_ticks[0]: y_ticks[-1]+1])
	
	#plt.title('2nd degree Polynomial Regression')
	#plt.xlabel('Position level')
	#plt.ylabel('Pitches')
	
	
	
	plt.grid(True)
	
	
	#εναλλακτικώς κώδικας αν θέλουμε να αποθηκεύσουμε το κάθε διάγραμμα
	'''
	i = 0
	while True:
		temp = 'parabola'+str(i)+'.png'
		if os.path.isfile(temp):
			i+=1
			continue
		
		plt.savefig(temp, bbox_inches='tight', dpi=600)
		break
	'''
	#plt.savefig('parabola.png', bbox_inches='tight', dpi=600)
	
	
	
	
	
	plt.show()
	plt.clf()
	
	
	
	
	

	# Finding if the parabola  is concave or convex
	# Εύρεση της πρώτης και της δεύτερης παραγώγου της παραβολής που μας δίνει το regression.
	numpyDiff = np.diff(model)/np.diff(range(len(model)))             # η πρώτη παράγωγός
	numpyDiff2 = np.diff(numpyDiff)/np.diff(range(len(numpyDiff)))    # η δευτερη παράγωγός
	
	
	# Αφού η καμπύλη ΠΡΕΠΕΙ να είναι παραβολή 2ης τάξης δεν θα έχει σημείο καμπής
	# Άρα η παραβολή δεν μπορεί να έχει σημεία όπου η δεύτερη παράγωγος της να ισούτε με το μηδέν.
	# Αν έχει ΤΟΤΕ δεν είναι Παραβολή
	for i in numpyDiff2:
		if i == 0:
			return None
	
	
	if numpyDiff2[1] < 0:
		##print('+')
		return '+'
	elif numpyDiff2[1] > 0:
		##print('-')
		return '-'








#===========================================================
'''
print(polynomial_regression([10,11,12,13,14, 15,16],
							[ 4, 4, 4, 6, 6, 7, 6]))

print(polynomial_regression([10, 11, 12, 13, 14,15,16],
							[ 1,  2,  3,  5, 4,5,4]))

print(polynomial_regression([0, 1, 2,  3, 4],
							[5, 0, 5, 10, 5]))

print(polynomial_regression([0, 1, 2, 3,  4, 5],
							[5, 0, 5, 5, 10, 5]))

print(polynomial_regression([0, 1, 2],
							[5, 0, 5]))


print(polynomial_regression([0, 1, 2],
							[5, 5, 5]))




print(polynomial_regression([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
							[5, 5, 5, 5, 3, 6, 6, 3 ,3, 3, 3]))

print(polynomial_regression([4, 5, 6, 7, 8],
							[5, 3, 6, 6, 3]))


'''










