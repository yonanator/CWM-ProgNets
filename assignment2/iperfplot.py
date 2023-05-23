# !/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# parameters to modify
filename="TCP_iperf3_edited.txt"
label=''
xlabel = 'time(s)'
ylabel = 'bandwidth(Mbits/sec)'
title='Bandwidth with Raspberry Pi as iperf3 server'
fig_name='test.png'


t = np.loadtxt(filename, dtype="float")
x = [1,2,3,4,5,6,7,8,9,10]

# sort

# get the probability


plt.plot(x, t)  # Plot some data on the (implicit) axes.
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend()
plt.savefig(fig_name)
plt.show()
