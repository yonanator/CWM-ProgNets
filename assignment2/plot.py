# !/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# parameters to modify
filename="iperf1.txt"
label='label'
xlabel = 'xlabel'
ylabel = 'ylabel'
title='Simple plot'
fig_name='test.png'


t = np.loadtxt(filename, delimiter=" ", dtype="float")

# sort

# get the probability


plt.plot(np.linspace(0,1,len(t)), t, label=label)  # Plot some data on the (implicit) axes.
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend()
plt.savefig(fig_name)
plt.show()
