import matplotlib.pyplot as plt
import numpy as np
cint = 22.4
Range = cint/1.82
print Range

f=500
Fs=100*f
sample=1000+1

x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)
#std_dev = np.std(y)
std_dev = 0.6991

#plt.plot(x, y)
#plt.xlabel('voltage(V)')
#plt.ylabel('sample(n)')
#plt.show()

#print np.std(y)
#print(20*np.log10(Range/(std_dev/1000)))
#
#array = [-1.85]*10 + [1.85]*10

#print np.std(array)

