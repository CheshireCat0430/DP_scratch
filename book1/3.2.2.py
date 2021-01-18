'''
계단 함수를 구현하기
'''

import numpy as np
import matplotlib.pylab as plt

def step_function(x) :
    return np.array(x>0, dtype=np.int)

#x = np.array([-1.0, 1.0, 2.0])
#print(step_function(x))

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
#plt.savefig("test.png")
plt.show()