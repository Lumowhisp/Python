import matplotlib.pyplot as plt
import numpy as np
Lang=np.array(["Python","Java","C++","JavaScript","Ruby"])
Popularity=np.array([30,25,20,15,10])
plt.title("Languages & Popularity Distribution")
color=["Green","Blue","Grey","Yellow","Red"]
plt.pie(Popularity,labels=Lang,colors=color,autopct="%1.1f%%")
plt.axis("equal")
plt.show()