import math
import numpy as np
a = 3000
raiseing = 0.01 * 0.1 * np.exp(0.000272 * int(a)) / (0.1 + 0.01 * (np.exp(0.000272 * int(a)) - 1))
print(raiseing)
from sympy import *
x = symbols('x')
# def func(x):
#     return
# print(integrate((1/0.0975)*exp((-1/0.0975)*0.2793*(-1+0.03068/(0.1-2*x))), (x, 0.01, 0.02)))
from scipy.integrate import tplquad,dblquad,quad


val1,err1=quad(lambda x:(1/0.0975)*math.exp((-1/0.0975)*0.2793*(-1+0.03068/(0.1-2*x))),0.01,0.02)
print ('积分结果：',val1)

