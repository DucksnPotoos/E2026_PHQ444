import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sympy import symbols, sinh, cosh, limit, oo

x = symbols('x')

expr = 2*sinh(x) / (1+2*cosh(x))
def expr_numpy (x):
    return 2*np.sinh(x) / (1+2*np.cosh(x))

T_0 = limit(expr, x, 0)
T_inf = limit(expr, x, oo)
T_char =expr_numpy(1)

print(T_0)
print(T_inf)
print(T_char)

def graph():
    x = np.linspace(-0.2,5, 1000)
    plt.plot(x, expr_numpy(x), label=r'$\frac{2\sinh(\beta\mu_B B)}{1 + 2\cosh(\beta\mu_B B)}$')
    plt.hlines(1, min(x), max(x), linestyles='--', color="#FC5800", zorder=0)
    plt.hlines(0, min(x), max(x), linestyles='--', color='#FC5800', zorder=0)
    plt.vlines(0, min(expr_numpy(x)), max(expr_numpy(x)), linestyles='--', color="#0EE6D7", zorder=0)
    
    plt.xlabel("x")
    plt.ylabel("y(x)")
    
    plt.legend()
    plt.savefig('figs/no2v.SVG')
    plt.show()
graph()