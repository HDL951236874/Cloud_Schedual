from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math
"""
this programme is to draw the pic of the probability dense which is changed with the price we give and the number of spot_instance bided in the last time slot
"""
# figure = plt.figure()
# # ax = Axes3D(figure)
# # def func(num,prcie):
# #     pd = 0
# #
# #     price_after = 0.012 * 0.1 * np.exp(0.0018 * num) / (
# #         0.1 + 0.012 * (np.exp(0.0018 * num) - 1))
# #
# #     pd = (1/math.sqrt(2*math.pi))*math.exp(-(prcie-price_after)**2/2)
# #     # if 0.01 + price_up_rate <= price <= 0.014 + price_up_rate:
# #     #     pd = 2 * (price - 0.01 - price_up_rate) / (0.01 * 0.004)
# #     # if 0.014 + price_up_rate <= price <= 0.02 + price_up_rate:
# #     #     pd = 2 * (0.02 + price_up_rate - price) / (0.01 * 0.006)
# #     return pd
# #
# # num_spot = np.arange(0,10000,10)
# # price = np.arange(0.01,0.1,0.0001)
# #
# # prob = np.zeros((np.size(price),np.size(num_spot)))
# # for n in range(len(num_spot)):
# #     for m in range(len(price)):
# #         prob[m][n] = func(num_spot[n],price[m])
# #
# # # prob = np.array(prob).reshape(len(price),len(num_spot))
# # print(np.size(prob))
# #
# # num_spot, price = np.meshgrid(num_spot, price)
# #
# # ax.plot_surface(num_spot, price,prob, rstride=1, cstride=1,cmap=cm.coolwarm,linewidth=0,antialiased=False)
# # ax.set_xlabel("number of bidding")
# # ax.set_ylabel("price given by Amazon")
# # ax.set_zlabel("probability")
# # # axs = plt.gca()
# # # axs.set_xlim(0, )
# # ax.view_init(elev=30, azim=120)
# # plt.savefig("fig")
# # plt.show()
# # plt.close()

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# 绘制一个余弦曲线
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
ax.plot(t, s, lw=2)

# 绘制一个黑色，两端缩进的箭头
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            xycoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05)
            )
ax.set_ylim(-2, 2)
plt.show()
