from scipy.integrate import quad


import math
l = []
# def raising(x):
#     return 0.01 * 0.1 * math.exp(0.00018 * int(x)) / (0.1 + 0.01 * (math.exp(0.00018 * int(x)) - 1))
#
# x = 1800
# p = quad(lambda x: (1 / 0.0975) * math.exp((-1 / 0.0975) * 0.2793 * (-1 + 0.03068 / (0.1 - 2 * x))), 0.01,
#                   0.04 - raising(x))[0]
# z = x*p
# print(z)
#
# print(1335*raising(1800)+0*raising(800))#1335
# print(708*raising(900)+708*raising(900))#1416
# print((1335*raising(1800))/1335)
# print((708*raising(900)+708*raising(900))/1416)
gene = [1075, 1279, 1082, 1018, 1054, 1231, 852, 1299]
ll = []
max = 0
nt = 0
for x in range(5000):
    raising = 0.01 * 0.1 * math.exp(0.000272 * int(x)) / (0.1 + 0.01 * (math.exp(0.000272 * int(x)) - 1))
    p = quad(lambda x: (1 / 0.0975) * math.exp((-1 / 0.0975) * 0.2793 * (-1 + 0.03068 / (0.1 - 2 * x))), 0.01,
                  0.04 - raising)[0]
    z = x*p
    if z>max:
        max = z
        nt = x
    if(z>0):
        l.append(p)

import matplotlib.pyplot as plt

print(nt)
print(max)
plt.plot([x for x in range(len(l))],l,c='black')
plt.xlabel('No. of SP bidding', fontsize=15)
plt.ylabel('Probability of successful bid', fontsize=15)
plt.show()
