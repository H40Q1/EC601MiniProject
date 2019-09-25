import matplotlib.pyplot as plt
from google_module_3 import*

#deal with sentiment score
#classify scores

c1=0
c2=0
c3=0
c4=0

for s in scores:
    if s <=1 and s>=0.7:
        
        c1=c1+1
    elif s <0.7 and s>=0.3:
        
        c2=c2+1
    elif s<0.3 and s>=-0.3:
        
        c3=c3+1
    else:
        
        c4=c4+1



# Data to plot
labels = 'Very Happy', 'Happy', 'OK', 'Disatisfied'
sizes = [c1,c2,c3,c4]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0, 0, 0)  

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
