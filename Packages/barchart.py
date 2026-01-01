import matplotlib.pyplot as plt
import numpy as np
x=np.array(["Aditya","Ayush","Ankit","Manya"])
y=np.array([80,67,32,90])
plt.title("Marks Distribution")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.bar(x,y)
plt.show()