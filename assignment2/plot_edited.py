# !/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# parameters to modify
filename="ping_end3.txt"
label='label'
xlabel = 'xlabel'
ylabel = 'ylabel'
title='Simple plot'
fig_name='test.png'


t = np.loadtxt(filename, delimiter=" ", dtype="float")

# sort
n = sorted(t)
# get the probability
p = 1. * np.arange(len(n))/(len(n)-1)


plt.plot(n, p, label=label)  # Plot some data on the (implicit) axes.
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend()
plt.savefig(fig_name)
plt.show()
