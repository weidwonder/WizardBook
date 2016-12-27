import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
S = np.sin(X)

plt.figure(figsize=(8, 6), dpi=80)
plt.plot(X, C, color='blue', linewidth=3.0, linestyle='-')
plt.plot(X, S, color='red', linewidth=3.0, linestyle='-')
plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.ylim(C.min() * 1.1, C.max() * 1.1)
plt.yticks([-1.0, 0, 1.0], ['$-1.0$', '0', '$+1.0$'])


ax = plt.gca()
# Spines are the lines connection the axis tick marks and noting the
# boundaries of the data area. By default. it settled around the data
# area. So, there are 4 spines: 'top' 'bottom' 'left' and 'right'
ax.spines['right'].set_color('none')
# make right spine disappear.
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
# set bottom spine ticks under the spine.
ax.spines['bottom'].set_position(('data', 0))
# if this ax is X-axis it will set at position of 0 on Y-axis.
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
# So does it.



plt.show()