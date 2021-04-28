from sympy import *
from sympy.plotting.plot import plot3d

x, y = symbols('x y')
f = 1/2*x + 3/2*y

plot3d(f, (x, 0, 1), (y, 0, 1),
       xlabel='x',
       ylabel='y',
       title='Hustota vektoru (X,Y)')
