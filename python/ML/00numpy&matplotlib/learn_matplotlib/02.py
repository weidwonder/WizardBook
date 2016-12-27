# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# Codes blew will show you What is the default setting in matplotlib.
# You can change it to explore their affect.

plt.figure(figsize=(8, 6), dpi=80)
# Create a figure of size 8 * 6 points, using 80 dpi.

plt.subplot(111)
# plt.subplot(222)
# Create a new subplot from a grid of 2 * 2.
# 2 * 2 is the first two '2's, and the third means the second grid

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
# Check 01.py

plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
# Plot cosine using blue color with a continuous line of width 1(pixels)

plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")
# Plot sine using green color with a continuous line of width 1(pixels)

plt.xlim(-4, 4)
# plt.xlim(X.min() * 1.1, X.max() * 1.1)
# Set x limits

# plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# Set x ticks. Divide range from -4 to 4 into 8 sections(9 points) as x-ticks(x轴标记)

plt.ylim(-1.0, 1.0)
# plt.ylim(C.min() * 1.1, C.max() * 1.1)
# Set y limits

plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
# Set y ticks.

plt.savefig('02config.png', dpi=72)
# Save figure using 72 dots per inch

plt.show()
# Show the figure.