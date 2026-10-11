import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
  return np.sqrt(x**2 + y**2)


x = np.array([-1.532, 0.631 ,1.231, -0.715])
y = np.array([0.693, 1.366 ,-0.573, -1.325])
z = np.array([0])
u = np.array([0])
e = np.array([-0.142])
j = np.array([0.073])


for i in range(len(x)):
  r = f(x,y)

radio_promedio = np.sum(r)/4


fig1 = plt.figure(figsize=(10,10))
ax = fig1.add_subplot(1,1,1)
plt.scatter(x,y, marker = "o", color = "r", label = "Marte")
plt.scatter(z,u, marker = "o", color = "yellow", s=100, label = "Sol")
plt.scatter(z,u, marker = "o", color = "yellow", s=10009)
plt.scatter(e,j, marker = "o", color = "black", label = "Centro")

print(radio_promedio)

plt.xlim(-2, 2)
plt.ylim(-2, 2)


circle = plt.Circle((-0.142,0.073),radio_promedio,color='black',lw=2,fill=False)
ax.arrow(-0.142,0.073, -0.142,radio_promedio, head_width=0, head_length=0, label = "Radio Órbita de Marte = 1.512 ", color = "black")
ax.add_artist(circle)

plt.legend(loc = "upper right")
plt.show()