from pylab import *
# This import sentence is same as
#   import numpy as np
#   import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# np.linspace method will get a array which has 256 values between -pi to pi.
C, S = np.cos(X), np.sin(X)
# C is a array of X's cos value and S is a array of X's sin value.

plot(X, C)
# X is X-axis coordinates array, and C is Y-coordinates array.
# So it draw a picture of curve of cos(x).
plot(X, S)
# This is curve of sin(x)

show()
# Show the picture.