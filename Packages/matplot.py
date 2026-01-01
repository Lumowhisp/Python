import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 25, 30])
plt.title("Class Size" ,fontsize="10",fontweight="10")
plt.xlabel("Number")
plt.ylabel("Rankers")


plt.plot(x, y,marker=".",markersize=20,markerfacecolor="#1cd3fc")
plt.xticks(x)
plt.yticks(y)

plt.show()