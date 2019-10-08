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
for x in range(5000):
    raising = 0.01 * 0.1 * math.exp(0.000272 * int(x)) / (0.1 + 0.01 * (math.exp(0.000272 * int(x)) - 1))
    p = quad(lambda x: (1 / 0.0975) * math.exp((-1 / 0.0975) * 0.2793 * (-1 + 0.03068 / (0.1 - 2 * x))), 0.01,
                  0.04 - raising)[0]
    z = x*p
    if(z>0):
        l.append(z)
        ll.append(x)
import matplotlib.pyplot as plt

plt.plot([x for x in range(len(l))],l)
plt.show()

down = []
up = []
for index in gene:
    for i in range(len(l)-1):
        if l[i]>index and l[i+1]<index:
            down.append(ll[i])
        if l[i]<index and l[i+1]>index:
            up.append(ll[i])

print(up)
print(down)

# import matplotlib.pyplot as plt
#
# plt.plot([x for x in range(len(l))],l)
# plt.show()
#
# print(' '.jo  in(['1','a']))
