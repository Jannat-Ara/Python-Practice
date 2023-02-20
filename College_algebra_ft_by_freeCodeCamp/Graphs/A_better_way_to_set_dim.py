# a better way to set dimension
import matplotlib.pyplot as plt
 

xmin= -10
xmax= 10
ymin= -10
ymax= 10

fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0], [ymin,ymax],'b')
plt.show()