# Lagrange Interpolation

# Importing NumPy Library
import numpy as np

# Reading number of unknowns
n = int(input('Enter number of data points: '))


x = np.zeros((n))
y = np.zeros((n))


s
print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))


xp = float(input('Enter interpolation point: '))

# Set interpolated value initially to zero
yp = 0

for i in range(n):

    p = 1

    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])

    yp = yp + p * y[i]

# Displaying output
print('Interpolated value at %.3f is %.3f.' % (xp, yp))