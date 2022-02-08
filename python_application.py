import numpy as np
from math import factorial
import matplotlib.pyplot as plt

"""

Amir Salehi
Computing Method
Electrical Engineering Faculty
Napier with McLorain Series


"""

def __Napier__(itr):
    i = 0
    _sum_ = 0
    while i <= itr:
        _sum_ += (1/factorial(i))
        i += 1
    return _sum_
##########
e = []
space = ' '
x = []
calc = []
diff = []
for i in range(1 , 11):
    x.append(i)
    calc.append(__Napier__(i))
    e.append(np.e)
    diff.append(np.e - __Napier__(i))
plt.plot(x , calc , c='r' , marker='*')
plt.plot(x , e , c='blue', marker='o')
plt.plot(x , diff , c='green',marker='+')
plt.grid(True)
plt.show()