#Robert Genega 
#cs471 project 2 

#local_search


import sys
import random


import numpy as np

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import axes3d, Axes3D

matplotlib.matplotlib_fname()
x = matplotlib.matplotlib_fname()


def graph(func, xmin, ymin, xmax, ymax, points=[]):
	try:
		fig = plt.figure()
		# ax = fig.gca(projection='3d')
	
		ax = Axes3D(fig)

		# Make data.
		X = np.arange(xmin, xmax, 0.25)
		Y = np.arange(ymin, ymax, 0.25)
		X, Y = np.meshgrid(X, Y)

		Z = func(X,Y)
		# Plot the surface.
		surf = ax.plot_surface(X, Y, Z, #cmap=cm.coolwarm,
		linewidth=0, antialiased=False)

		# Customize the z axis.
		ax.set_zlim(-1.01, 1.01)
		ax.zaxis.set_major_locator(ticker.LinearLocator(10))
		ax.zaxis.set_major_formatter(ticker.FormatStrFormatter('%.02f'))

		# Add a color bar which maps values to colors.
		#fig.colorbar(surf, shrink=0.5, aspect=5)
		for i in points:
			ax.plot([i[0]], [i[1]], [i[2]], '.', color=(i[3]/1000,0,0)) 
		plt.show()
	except Exception as e:
		pass
		#print(e)
	
	



#read command line arguments
input_file = sys.argv[1]
xmin = int(sys.argv[2])
ymin = int(sys.argv[3])
xmax = int(sys.argv[4])
ymax = int(sys.argv[5])


file = open(input_file, 'r')
data = file.read()

exec(data)

finalx = random.randint(xmin, xmax)
x = finalx

finaly = random.randint(ymin, ymax)
y = finaly

finalmax = my_func(x, y)
max = finalmax



count = 0

while count < 1000:
	
	maxima = False
	
	while maxima != True:
		
		
		
		z1 = my_func(x+1, y)
		z2 = my_func(x-1, y)
		z3 = my_func(x, y+1)
		z4 = my_func(x, y-1)
		
		x2 = x
		y2 = y
		
		maxima = True
		
		if (z1 > max) and (x+1 <= xmax):
			max = z1
			x2 = x + 1
			maxima = False
		if (z2 > max) and (x-1 >= xmin):
			max = z2
			x2 = x - 1
			maxima = False
		if (z3 > max) and (y+1 <= ymax):
			max = z3
			x2 = x
			y2 = y+1
			maxima = False
		if (z4 > max) and (y-1 >= ymin):
			max = z4
			x2 = x
			y2 = y - 1
			maxima = False

		
		x = x2
		y = y2
			
			
		if maxima == True:
			if finalmax < max:
				finalmax = max
				finalx = x
				finaly = y
				
	x = random.randint(xmin, xmax)
	y = random.randint(ymin, ymax)
	max = my_func(x, y)
	count += 1
				


val = []


val.append(finalx)
val.append(finaly)

print(val)

#ANNEALING CODE (MODIFICATION OF PREVIOUS HILL CLIMBING CODE)

numsteps = 10000
step = 0.1

finalx = random.randint(xmin, xmax)
x = finalx

finaly = random.randint(ymin, ymax)
y = finaly

finalmax = my_func(x, y)
max = finalmax

p = []

count = numsteps

e = 2.71828182846


while count > 0:
    
    x2 = x
    y2 = y

    z1 = my_func(x+step, y)
    z2 = my_func(x-step, y)
    z3 = my_func(x, y+step)
    z4 = my_func(x, y-step)

    guess = random.randint(1, 4)

    prob = 0

    if guess == 1:
        guess = z1
        x2 += step
    elif guess == 2:
        guess = z2
        x2 -= step
    elif guess == 3:
        guess = z3
        y2 += step
    else:
        guess = z4
        y2 -= step

    if guess > max:
        max = guess
        x = x2
        y = y2
    else:
        prob = e ** ((guess - max)/(count/numsteps))
        rand = random.random()

        if prob > rand:
            max = guess
            x = x2
            y = y2
    p.append((x, y, max, 1000-(count*1000/numsteps)))


    count -= 1


#p array
#each element is point on simulated annealing function
#(x, y, z, step number)
#step 0 is black and step 1000 is fully red


#p = [(finalx, finaly, finalmax, 0), (0, 0, 1, 1000)]



graph(my_func, xmin, ymin, xmax, ymax, p)





		
		
	
	