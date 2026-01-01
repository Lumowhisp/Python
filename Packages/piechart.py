import matplotlib.pyplot as plt
import numpy as np
cat=["Aditya","Ankit","Ayush","Manya"]
val=np.array([70,20,40,90])
plt.title("Marks Distribution")
color=["red","purple","blue","pink"]
plt.pie(val,labels=cat,autopct="%1.1f", colors=color)
plt.show()