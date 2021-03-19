import matplotlib.pyplot as plt
import numpy as np

X = np.arange(0,10)
Y = 0.05*X*X

plt.ylim(0, 5)
plt.plot(X, Y, color='turquoise')
plt.show()
plt.savefig("saveImage.png")