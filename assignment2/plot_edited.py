# !/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# parameters to modify
filename="ping_end2.txt"

xlabel = 'time(ms)'
ylabel = 'probability'
title='CDF for 0.001 interval'
fig_name='test.png'


t = np.loadtxt(filename, delimiter=" ", dtype="float")

# sort
n = sorted(t)
# get the probability
p = 1. * np.arange(len(n))/(len(n)-1)


plt.plot(n, p)  # Plot some data on the (implicit) axes.
plt.xlabel('time(ms)')
plt.ylabel('probability')
plt.title('CDF for 0.001 interval')
plt.legend()
plt.savefig(fig_name)
plt.show()
