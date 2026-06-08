import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sympy import symbols, sinh, cosh, limit, oo

import numpy as np
import matplotlib.pyplot as plt

def mu(T):
    return 1 + T*np.log(1 - np.exp(-1/T))

T = np.linspace(0.001, 3, 10000)

plt.plot(T, mu(T))
plt.xlabel(r'$k_BT/\epsilon_F$')
plt.ylabel(r'$\mu/\epsilon_F$')
plt.grid()
plt.savefig(f"figs/no2v.pdf")
plt.show()