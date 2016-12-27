import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
S = np.sin(X)

plt.figure(figsize=(8, 6), dpi=80)
plt.plot(X, C, color='blue', linewidth=3.0, linestyle='-', label="cosine")
plt.plot(X, S, color='red', linewidth=3.0, linestyle='-', label="sine")
# Should add label on each plot line.

plt.legend(loc='upper left', frameon=False)
# Adding a legend on left top.

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
# ATTENTION: ticks should be put after moved axis.
plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.ylim(C.min() * 1.1, C.max() * 1.1)
plt.yticks([-1.0, 0, 1.0], ['$-1.0$', '0', '$+1.0$'])


plt.show()