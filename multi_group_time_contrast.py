import numpy as np
import matplotlib.pyplot as plt

x1 = [1,2,3,4,5,6,7,8,9,10]
single = [21.314,42.573,63.922,85.241,106.107,127.412,148.722,170.032,191.343,212.658]
x2 = [1,2,3,4,5,6,7,8,9,10]
multi = [21.326,55.548,54.235,52.982,55.063,59.871,62.999,85.377,106.564,101.499]


font1 = {
'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 28,
}

font2 = {
'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 20,
}

plt.title('processing time Analysis',font1)
l1, = plt.plot(x1,single,color='green',marker="o",label='single hadoop group')
l2, = plt.plot(x2,multi,color='red',marker="o",label='multi hadoop group')

# color: darkorange lightcoral darkgoldenrod yellow greenyellow springgreen darkslategrey deepskyblue fushsia blue

x_ticks = np.arange(1,11,1)
y_ticks = np.arange(0,230,20)

plt.legend(handles=[l1,l2,],labels=['single','multi'],loc="best")
plt.xlabel('hadoop task request numbers  unit(1)',font2)
plt.ylabel('processing time  unit(seconds)',font2)

plt.xticks(x_ticks)
plt.yticks(y_ticks)

plt.show()
