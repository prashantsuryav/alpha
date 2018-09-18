import numpy as np
import matplotlib.pyplot as plt

# a = np.array([1,2,3])
# print(type(a))

x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()

