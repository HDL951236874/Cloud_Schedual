import pickle
import math
from scipy.integrate import quad
import random

CPUmax = 4
MEMmax = 4

def finish_by_time(l,num_l):
    ll = [l[i][num_l[i]+1:] for i in range(len(l))]
    Sum = []
    for i in ll:
        s = sum([x[2] for x in i])
        Sum.append(s)

    num = [int(x/5) for x in Sum]
    print(num)
    prof = [num[i]*5*(0.48-0.01-0.01375)/60 for i in range(len(num))]
    print(sum(prof))
    print(1)





class Cloud_computing_System():
    def __init__(self,l):
        self.CPUMAX = 4
        self.MEMMAX = 4
        self.B = 2
        self.time_slot_number = 8
        self.hour_number = 6
        self.group_size = 50
        self.generation = 100
        self.population_pool = []
        self.l = l
        self.num_l = self.private_cloud(self.l)
        self.best_pool = []
        self.best_for_all = []


    class population_templete():
        def __init__(self, val):
            self.binary_list = val
            self.solution = []
            self.score = 0


    def run(self):
        private_task = [self.l[x][:self.num_l[x]+1] for x in range(self.hour_number*self.time_slot_number)]
        private_time = [sum([x[2] for x in private_task[j]]) for j in range(self.hour_number*self.time_slot_number)]
        for i in range(self.hour_number):
            l = self.l[i*8:i*8+8]
            num_l = self.num_l[i*8:i*8+8]

            self.population_pool = self.population_init(self.group_size)
            for j in range(self.generation):
                self.GAengine(l,num_l)

            max_score = 0
            max_score_pop = None
            for pop in self.best_pool:
                if pop.score > max_score:
                    max_score = pop.score
                    max_score_pop = pop
            self.best_for_all.append(max_score_pop)
            self.best_pool = []
            print(sum(private_time[i*8:i*8+8])*0.48/60)
            print(max_score)
            print([int(x,2) for x in max_score_pop.binary_list])
            print("=============================================")

    def GAengine(self,l,num_l):
        # self.population_pool = self.population_init(self.group_size)
        # here need a fitness function
        self.group_fitness(l,num_l)
        self.update_solution()
        temp_population = self.selection()
        self.population_pool = temp_population
        self.crossover(temp_population)
        self.mutation()
        # self.update_solution()




    def population_init(self, group_size):
        import random
        return [self.population_templete([bin(random.randint(0,1500))[2:] for _ in range(self.time_slot_number+1)]) for __ in range(group_size)]

    def group_fitness(self,l,num_l):
        for i in range(len(self.population_pool)):
            gene = [int(x,2) for x in self.population_pool[i].binary_list]
            self.population_pool[i].score = self.fitness(gene,l,num_l,self.B)

        max_score = 0
        max_pop = None
        for pop in self.population_pool:
            if pop.score>=max_score:
                max_score = pop.score
                max_pop = pop

        self.best_pool.append(max_pop)



    def selection(self):
        score_sum = sum([gene.score for gene in self.population_pool])
        prob_list = [gene.score/score_sum for gene in self.population_pool]
        accumulation_prob_list = [sum(prob_list[:i+1]) for i in range(len(prob_list))]
        import random
        random_number_list = [random.random() for _ in range(int(self.group_size/2))]

        pop_select = []
        for rand_num in random_number_list:
            for i in range(len(accumulation_prob_list)):
                if rand_num <= accumulation_prob_list[i]:
                    pop_select.append(i)
                    break

        temp_population = [self.population_pool[x] for x in pop_select]

        return temp_population


    def crossover(self,temp_pop):
        import random
        random.shuffle(temp_pop)
        for i in range(0,len(temp_pop),2):
            if i+1 >= len(temp_pop):
                continue
            list_A = []
            list_B = []
            for j in range(self.time_slot_number+1):

                string_A = temp_pop[i].binary_list[j]

                string_B = temp_pop[i+1].binary_list[j]
                if len(string_A)>len(string_B):
                    add = ''.join(['0' for _ in range(len(string_A)-len(string_B))])
                    string_B = add+string_B
                if len(string_B)>len(string_A):
                    add = ''.join(['0' for _ in range(len(string_B)-len(string_A))])
                    string_A = add+string_A

                pos = random.randint(1,len(string_A))
                list_A.append(string_A[:pos+1]+string_B[pos+1:])
                list_B.append(string_B[:pos+1]+string_A[pos+1:])

            new_indv_A = self.population_templete(list_A)
            new_indv_B = self.population_templete(list_B)
            self.population_pool.append(new_indv_A)
            self.population_pool.append(new_indv_B)

    def mutation(self):
        random_num_list = [random.random() for _ in range(len(self.population_pool))]
        for i in range(len(random_num_list)):
            if random_num_list[i] < 0.01:
                time_slot = random.randint(0,self.time_slot_number-1)
                # pos = random.randint(0,len(self.population_pool[i].binary_list[time_slot]))
                string = self.population_pool[i].binary_list[time_slot]
                pos = random.randint(0,len(string)-1)
                muta = '0' if string[pos] == '1' else '1'
                string = string[:pos]+muta+string[pos+1:]
                self.population_pool[i].binary_list[time_slot] = string

    def update_solution(self):
        for member in self.population_pool:
            member.solution = []
            for index in member.binary_list:

                member.solution.append(int(index,2))

    def private_cloud(self, l):
        '''
        返回每个区间私有云处理的任务数量
        :param l:
        :return:
        '''
        num_l = []
        for i in l:
            cpu, mem, num = 0, 0, 0
            for j in i:
                if cpu >= self.CPUMAX or mem >= self.MEMMAX:
                    break
                cpu += j[0]
                mem += j[1]
                num += 1
            num_l.append(num)

        return num_l

    def fitness(self,gene, l, num_l, B):
        instance_l = [l[x][num_l[x] + 1:] for x in range(len(num_l))]
        od = gene[0]
        sp = gene[1:]

        '''process by od'''
        OD_TIME_MAX = od * 7.5
        od_time_list = []
        od_number_list = []
        for i in instance_l:
            time, num = 0, 0
            for j in i:
                if time >= OD_TIME_MAX:
                    break
                time += j[2]
                num += 1
            od_time_list.append(time)
            od_number_list.append(num)

        '''process by sp'''
        price_up_rate = [0.01 * 0.1 * math.exp(0.000272 * int(x)) / (0.1 + 0.01 * (math.exp(0.000272 * int(x)) - 1)) for
                         x in
                         sp]
        p = [quad(lambda x: (1 / 0.0975) * math.exp((-1 / 0.0975) * 0.2793 * (-1 + 0.03068 / (0.1 - 2 * x))), 0.01,
                  0.04 - price_up_rate[x])[0] for x in range(len(price_up_rate))]
        sp_successfully_bid = [p[x] * sp[x] for x in range(len(sp))]
        instance_sp = [instance_l[x][od_number_list[x] + 1:] for x in range(len(od_number_list))]
        SP_TIME_MAX = [x * 5 for x in sp_successfully_bid]
        sp_time_list = []
        sp_num_list = []
        sp_pool = []
        for i in range(len(instance_sp)):
            sp_pool.append(instance_sp[i])
            if len(sp_pool) > B:
                sp_pool = sp_pool[-B:]
            time = 0
            num = 0
            finish = False
            for j in sp_pool:
                for k in j:
                    if time > SP_TIME_MAX[i]:
                        finish = True
                        break
                    time += k[2]
                    num += 1
                if finish == True:
                    break

            sp_time_list.append(time)
            sp_num_list.append(num)
        # print(sp_time_list)
        # print(sp_num_list)
        # print(sp_successfully_bid)
        od_cost = sum(od_time_list) * 0.1
        sp_cost = sum([sp_successfully_bid[x] * (0.01 + price_up_rate[x]) for x in range(len(price_up_rate))])

        profit = 0.48 * (sum(od_time_list) + sum(sp_time_list))
        # print('profit'+str(profit))
        # print('od'+str(od_cost))
        # print('sp'+str(sp_cost))
        return (profit - od_cost - sp_cost)/60

    def make_the_instance_number_plot(self):
        import matplotlib.pyplot as plt
        od_ = []
        sp_ = []
        score = []
        for pop in self.best_for_all:
            od_ += [int(pop.binary_list[0],2) for _ in range(self.time_slot_number)]
            sp_ += [int(x,2) for x in pop.binary_list[1:]]
            score.append(pop.score)
        plt.plot([x for x in range(len(od_))],od_,marker='o')
        plt.plot([x for x in range(len(sp_))],sp_,marker='o')
        # plt.bar([], score, width=0.4, color='b')
        print(score)
        plt.show()

# 374.98470058373977,368.20129987048836,395.63622721275453,382.22204657668095,381.2339864359745,372.59091593095917
if __name__ == '__main__':
    import os
    # print(os.getcwd())
    pkl_file = open('data_middle.pkl', 'rb')
    LIST = pickle.load(pkl_file)
    SYS = Cloud_computing_System(LIST)
    SYS.run()
    SYS.make_the_instance_number_plot()
    # finish_by_time(SYS.l[0:8],SYS.num_l)
    # gene = [0, 1075, 1279, 1082, 1018, 1054, 1231, 852, 1299]
    gene = [0, 1512, 1750, 1600, 1664, 1512, 1670, 1680, 1770]
    # gene = [0,1410, 1713, 1420, 1328, 1379, 1380, 1640, 1096, 1744]
    up_gene = [0,1508, 1911, 1520, 1409, 1471, 1807, 1141, 1957]
    down_gene = [0,4101, 3813, 4092, 4167, 4125, 3890, 4338, 3778]
    import matplotlib.pyplot as plt
    # plt.plot([x for x in range(8)],gene[1:9])
    # plt.plot([x for x in range(8)],up_gene[1:9])
    # plt.plot([x for x in range(8)],down_gene[1:9])
    # plt.show()


    print(SYS.fitness(down_gene,SYS.l[0:8],SYS.num_l[0:8],2))
    print(SYS.fitness(up_gene,SYS.l[0:8],SYS.num_l[0:8],2))
    print(SYS.fitness(gene,SYS.l[0:8],SYS.num_l[0:8],2))
    # print(SYS.fitness(up_gene,SYS.l[0:8],SYS.num_l[0:8],2))