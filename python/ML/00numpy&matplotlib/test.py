# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
from itertools import product
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return x*2 + y*2 #(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 5
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)
print zip(X, Y)[:5]

plt.axes([0.025,0.025,0.95,0.95])

plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap=plt.cm.hot)
C = plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
x_range = np.max(X) - np.min(X)
y_range = np.max(Y) - np.min(Y)
plt.clabel(C, inline=1, fontsize=10)
for m, n in product(x, y):
    plt.text(m, n, str(f(m, n)))

plt.xticks([]), plt.yticks([])
# savefig('../figures/contour_ex.png',dpi=48)
plt.show()