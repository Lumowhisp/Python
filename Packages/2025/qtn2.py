import matplotlib.pyplot as plt
import numpy as np
#Creating Data
Food=np.array(["Meat","Banana","Avacados","Sweet Potatoes","Spinach","Watermelon","Coconut Water","Beans","Legumes","Tomato"])
Calories=np.array([250,130,140,120,20,20,20,50,40,19])
Potassium=np.array([40,55,20,30,40,32,10,26,25,20])
fat=np.array([8,5,3,6,1,1.5,0,2,1.5,2.5])
plt.plot(Food,Calories,label="Calories")
plt.plot(Food,Potassium,label="Potassium")
plt.plot(Food,fat,label="Fat")
plt.xlabel("Food Items")
plt.ylabel("Nutritional Values")
plt.title("Food Items & Nutritional Values Distrubution")
plt.legend()
plt.show()
