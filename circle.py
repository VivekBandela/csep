import matplotlib.pyplot as plt
import numpy as np
r=0.4
pi=3.14
x=np.linspace(-r,r,1000)
plt.xlim(-r,r)
plt.ylim(-r,r)
y=np.sqrt(r**2-x**2)
plt.plot(x,y)
plt.plot(x,-y)
plt.show()
