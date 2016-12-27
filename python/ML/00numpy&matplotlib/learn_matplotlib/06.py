import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
S = np.sin(X)

plt.figure(figsize=(8, 6), dpi=80)
plt.plot(X, C, color='blue', linewidth=2.5, linestyle='-', label="cosine")
plt.plot(X, S, color='red', linewidth=2.5, linestyle='-', label="sine")
plt.legend(loc='upper left', frameon=False)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.ylim(C.min() * 1.3, C.max() * 1.3)
plt.yticks([-1.0, 0, 1.0], ['$-1.0$', '0', '$+1.0$'])



# The tick labels are now hardly visible because of the blue and red lines.
# We can make them bigger and we can also adjust their properties such that
# they'll be rendered on a semi-transparent white background. This will allow
# us to see both the data and the labels.

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(14)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))


t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$', xy=(t, np.sin(t)),
             xycoords='data', xytext=(+10, +30), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->',
                                          connectionstyle="arc3,rad=.2"))
plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle='--')
plt.scatter([t, ], [np.sin(t), ], 50, color='red')
plt.annotate(r'$\cos(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$', xy=(t, np.cos(t)),
             xycoords='data', xytext=(-90, -50), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->',
                                          connectionstyle="arc3, rad=.2")
             )

plt.show()