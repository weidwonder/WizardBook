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
plt.xlim(X.min() * 1.3, X.max() * 1.3)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.ylim(C.min() * 1.3, C.max() * 1.3)
plt.yticks([-1.0, 0, 1.0], ['$-1.0$', '0', '$+1.0$'])


# Let's annotate some interesting points using the annotate command. We
# chose the 2pi/3 value and we want to annotate both the sine and the cosine
# we'll first draw a marker on the curve as well as a straight dotted line
# Then, we'll use the annotate command to display some text with a arrow.

t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
# Draw a dotted line between X-axis and cosine curve.
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
# Add scatter point on cosine curve. The 500 is the point size.
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$', xy=(t, np.sin(t)),
             xycoords='data', xytext=(+10, +30), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->',
                                          connectionstyle="arc3,rad=.2"))
# xytext is offset from xy.
plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle='--')
plt.scatter([t, ], [np.sin(t), ], 50, color='red')
plt.annotate(r'$\cos(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$', xy=(t, np.cos(t)),
             xycoords='data', xytext=(-90, -50), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->',
                                          connectionstyle="arc3, rad=.2")
             )

plt.show()