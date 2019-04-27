from Cloud_Schedual.Oprocess import *


class Vector():
    def __init__(self, x, y1, y2, y3, y4, y5, y6, y7, y8):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4
        self.y5 = y5
        self.y6 = y6
        self.y7 = y7
        self.y8 = y8

    def __add__(self, other):
        return Vector(self.x + other.x, self.y1 + other.y1, self.y2 + other.y2, self.y3 + other.y3, self.y4 + other.y4,
                      self.y5 + other.y5, self.y6 + other.y6, self.y7 + other.y7, self.y8 + other.y8)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y1 - other.y1, self.y2 - other.y2, self.y3 - other.y3, self.y4 - other.y4,
                      self.y5 - other.y5, self.y6 - other.y6, self.y7 - other.y7, self.y8 - other.y8)


class particle():
    def __init__(self, pos, max_pos, v, l, pn, pr, hour, ln, limite):
        self.pos = pos
        self.max_pos = max_pos
        self.v = v
        self.max_profit = 0
        self.l = l
        self.pn = pn
        self.pr = pr
        self.hour = hour
        self.ln = ln
        self.limite = limite

    def update(self, globle_max_pos, w):
        '''

        :param globle_max_pos:
        :param w: the weight
        :return:
        '''
        self.v = Vector(w * self.v.x, w * self.v.y1, w * self.v.y2, w * self.v.y3, w * self.v.y4, w * self.v.y5,
                        w * self.v.y6, w * self.v.y7, w * self.v.y8) + Vector(
            2 * random.uniform(0, 1) * (globle_max_pos - self.pos).x,
            2 * random.uniform(0, 1) * (globle_max_pos - self.pos).y1,
            2 * random.uniform(0, 1) * (globle_max_pos - self.pos).y2,
            2 * random.uniform(0, 1) * (globle_max_pos - self.pos).y3,
            2 * random.uniform(0, 1) * (globle_max_pos - self.pos).y4,
            2 * random.uniform(0, 1) * (globle_max_pos - self.pos).y5,
            2 * random.uniform(0, 1) * (globle_max_pos - self.pos).y6,
            2 * random.uniform(0, 1) * (globle_max_pos - self.pos).y7,
            2 * random.uniform(0, 1) * (globle_max_pos - self.pos).y8) + Vector(
            3 * random.uniform(0, 1) * (self.max_pos - self.pos).x,
            3 * random.uniform(0, 1) * (self.max_pos - self.pos).y1,
            3 * random.uniform(0, 1) * (self.max_pos - self.pos).y2,
            3 * random.uniform(0, 1) * (self.max_pos - self.pos).y3,
            3 * random.uniform(0, 1) * (self.max_pos - self.pos).y4,
            3 * random.uniform(0, 1) * (self.max_pos - self.pos).y5,
            3 * random.uniform(0, 1) * (self.max_pos - self.pos).y6,
            3 * random.uniform(0, 1) * (self.max_pos - self.pos).y7,
            3 * random.uniform(0, 1) * (self.max_pos - self.pos).y8)
        self.pos = self.pos + self.v
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y1 < 100:
            self.pos.y1 = 100
        if self.pos.y2 < 100:
            self.pos.y2 = 100
        if self.pos.y3 < 100:
            self.pos.y3 = 100
        if self.pos.y4 < 100:
            self.pos.y4 = 100
        if self.pos.y5 < 100:
            self.pos.y5 = 100
        if self.pos.y6 < 100:
            self.pos.y6 = 100
        if self.pos.y7 < 100:
            self.pos.y7 = 100
        if self.pos.y8 < 100:
            self.pos.y8 = 100
        if self.pos.x > self.limite[self.hour]:
            self.pos.x = self.limite[self.hour]
        if self.v.x > 100:
            self.v.x = 100
        if self.v.x < -100:
            self.v.x = -100
        if self.v.y1 > 100:
            self.v.y1 = 100
        if self.v.y1 < -100:
            self.v.y1 = -100
        if self.v.y2 > 100:
            self.v.y2 = 100
        if self.v.y2 < -100:
            self.v.y2 = -100
        if self.v.y3 > 100:
            self.v.y3 = 100
        if self.v.y3 < -100:
            self.v.y3 = -100
        if self.v.y4 > 100:
            self.v.y4 = 100
        if self.v.y4 < -100:
            self.v.y4 = -100
        if self.v.y5 > 100:
            self.v.y5 = 100
        if self.v.y5 < -100:
            self.v.y5 = -100
        if self.v.y6 > 100:
            self.v.y6 = 100
        if self.v.y6 < -100:
            self.v.y6 = -100
        if self.v.y7 > 100:
            self.v.y7 = 100
        if self.v.y7 < -100:
            self.v.y7 = -100
        if self.v.y8 > 100:
            self.v.y8 = 100
        if self.v.y8 < -100:
            self.v.y8 = -100

        self.get_self_profit()

    def get_self_profit(self):
        '''
        the profit func of the on-demand instance and the spot-instance number's profit
        :return:
        '''
        profit, xx, yy = ICOAO(self.l, self.hour, self.pn, self.pr, self.pos.x,
                               [self.pos.y1, self.pos.y2, self.pos.y3, self.pos.y4, self.pos.y5, self.pos.y6,
                                self.pos.y7, self.pos.y8], self.ln)
        if self.max_profit < profit:
            self.max_profit = profit
            self.max_pos = self.pos


class Particle_Pool():
    def __init__(self, ln):
        self.pool = []
        self.globle_max = 0
        self.globle_max_pos = Vector(0,0,0,0,0,0,0,0,0)
        self.ln = ln

    def init_first_max_pos_and_profiit(self):
        for index in self.pool:
            index.get_self_profit()
            if index.max_profit > self.globle_max:
                self.globle_max = index.max_profit
                self.globle_max_pos = index.max_pos

    def update(self, w):
        for index in self.pool:
            index.update(self.globle_max_pos, w)

        for index in self.pool:
            if index.max_profit > self.globle_max:
                self.globle_max = index.max_profit
                self.globle_max_pos = index.max_pos


def OPOS(l, hour, pn, pr, ln, limite):
    init_pos_OD = np.random.randint(100, 200, 10)
    init_pos_SI = np.random.randint(400, 500, 80)

    pp = Particle_Pool(ln)
    for num in range(len(init_pos_OD)):
        pp.pool.append(
            particle(Vector(init_pos_OD[num], init_pos_SI[num*8], init_pos_SI[num*8+1], init_pos_SI[num*8+2], init_pos_SI[num*8+3], init_pos_SI[num*8+4],
                            init_pos_SI[num*8+5],init_pos_SI[num*8+6],init_pos_SI[num*8+7]),
                     Vector(init_pos_OD[num], init_pos_SI[num*8], init_pos_SI[num*8+1], init_pos_SI[num*8+2], init_pos_SI[num*8+3], init_pos_SI[num*8+4],
                            init_pos_SI[num*8+5],init_pos_SI[num*8+6],init_pos_SI[num*8+7]),
                     Vector(0, 0,0,0,0,0,0,0,0),
                     l,
                     pn,
                     pr,
                     hour,
                     ln,
                     limite)
        )

    pp.init_first_max_pos_and_profiit()
    iter_time = 0
    max_iter_time = 50

    while iter_time <= max_iter_time:
        w = 1.0 - iter_time * (1.0 - 0.2) / 150

        pp.update(w)
        iter_time += 1
    print('============================================================')
    return pp.globle_max_pos, pp.globle_max


