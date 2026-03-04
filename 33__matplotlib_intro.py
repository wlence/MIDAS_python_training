import matplotlib.pyplot as plt
import numpy as np

x_values = range(1, 5)
y_values = np.random.randint(1, 20, size=4)

#No dependency plot
for i in range(len(x_values)):
    print(f"{x_values[i]:5}", "*" * y_values[i])

for i, v in enumerate(y_values):
    print(f"{x_values[i]:5}", "*" * v)

plt.plot(x_values, y_values, marker='o')
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Plot Intro")
plt.show()



