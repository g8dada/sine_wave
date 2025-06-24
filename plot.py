import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.tan(x)

plt.plot(x, y)
plt.title("Tangent Wave")
plt.xlabel("x")
plt.ylabel("tan(x)")
plt.grid(True)
plt.show()
