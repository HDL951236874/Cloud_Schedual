from Cloud_Schedual.OPOS import *
from Cloud_Schedual.caculation_process import *
import mpl_toolkits.axisartist.axislines as axislines

_a_ = [314.53113724288517, 250.18034032240138, 360.1674216036105, 522.271708753746, 369.7092364762528,
       379.9671709364375]

_b_ = [
    [194.9308796587644, 633.8682682974578, 991.9894930869377, 246.20781969209705, 602.159403132434, 818.1245523037857,
     803.8545641799062, 831.8546635933892],
    [100.0, 863.3707580148779, 695.1690992740544, 567.1870392302833, 666.5441076472395, 835.6777643696155,
     558.870955736481, 962.3196557625798],
    [186.0578241020075, 509.76665525248103, 528.8051412870569, 469.8803347544075, 761.1215389175708, 582.1754875635711,
     688.7954353038984, 542.6480900412521],
    [421.60282643398864, 100, 469.8148603564696, 587.0673675234175, 138.62703661391362, 245.4508922259405,
     569.5710982465911, 511.59472584213023],
    [272.3419031208225, 473.7448720966742, 374.799160037802, 769.7802347068023, 618.8238817877309, 543.9829450040743,
     660.9598448433705, 553.5333689458909],
    [100.0, 334.5068106676668, 608.5374214096161, 754.5450313411786, 747.0026261957021, 499.25547973577045,
     541.6117410631483, 578.7057182103983]]


def pic1():
    pkl_file = open('data_middle.pkl', 'rb')

    LIST = pickle.load(pkl_file)

    a = [x * 7.5 for x in range(48)]
    b = [len(x) for x in LIST]

    b.insert(0, 0)
    b.insert(len(b), 0)
    a.insert(len(a), 360.0)
    a.insert(len(a), 367.5)

    plt.plot(a, b, color='r', marker='o', mec='r', mfc='r')
    plt.xlabel('time(min)')
    plt.ylabel('number of arrival tasks per 7.5 mins')
    plt.savefig('number_pic')
    plt.show()
    plt.close()


def pic2(_a_, _b_):
    pkl_file = open('data_middle.pkl', 'rb')

    LIST = pickle.load(pkl_file)

    pn, prn = private_cloud(LIST)
    # _a_ = [668.6937549860297, 939.9092129163337, 848.526420934258, 629.6561072513375, 668.692955356629, 927.7781983613288]
    # _b_ = [5462.519910837557, 12792.009686189911, 4786.366765714456, 5452.009824866729, 6127.0120683630175, 4187.488011342355]
    a = [668, 5462]
    b = [0, 30000]
    # TODO:此处要做一个辨识函数
    OD_task = []
    SP_task = []
    for num in range(6):
        if num == 0:
            ln = 0
        profit, task_OD, task_SP = ICOAO(LIST, num, pn, prn, _a_[num], _b_[num], ln)
        OD_task += task_OD
        SP_task += task_SP
        ln = max(_b_[num])
    print(len(OD_task))
    print(len(SP_task))
    reject = [0 for x in range(50)]

    x = [x * 7.5 for x in range(48)]
    print(len(x))
    x.insert(len(x), 360.0)
    x.insert(len(x), 367.5)
    OD_task.insert(0, 0)
    OD_task.insert(len(OD_task), 0)
    SP_task.insert(0, 0)
    SP_task.insert(len(SP_task), 0)
    pn.insert(0, 0)
    pn.insert(len(pn), 0)
    print(OD_task)
    print(SP_task)
    plt.plot(x, reject, color='y', marker='o', mec='y', mfc='y', label='rejected')
    plt.plot(x, OD_task, color='r', marker='o', mec='r', mfc='r', label='on demand instance')
    plt.plot(x, SP_task, color='blue', marker='o', mec='blue', mfc='blue', label='spot instance')
    plt.plot(x, pn, color='green', marker='o', mec='green', mfc='green', label='private cloud')
    plt.xlabel('time(min)', fontsize=20)
    plt.ylabel('number of scheduled tasks per 7.5 mins', fontsize=15)
    axs = plt.gca()
    axs.set_ylim(0, 2500)
    plt.legend()
    plt.savefig('test')
    plt.show()
    # plt.savefig('number_pic')
    plt.close()


def pic3():
    x = np.linspace(0, 50000, 1000)
    y = np.linspace(0.00, 0.06, 12)
    plt.ylim(0, 0.1)
    plt.xlim(0, 50000)
    # ax = axislines.Subplot(fig)
    # ax.axis["left"].set_axis_direction("left")
    # ax.axis["bottom"].set_axis_direction("bottom")
    # ax.axis["right"].set_axis_direction("right")
    # ax.axis["top"].set_axis_direction("top")
    # y1 = [0.1 * 0.017 * exp(0.0017 * x) / (0.1 + 0.017 * (exp(0.0017 * x) - 1)) for x in x]
    # y2 = [0.1 * 0.0144 * exp(0.00023 * x) / (0.1 + 0.0144 * (exp(0.00023 * x) - 1)) for x in x]
    # y3 = [0.1 * 0.0121 * exp(0.00018 * x) / (0.1 + 0.0121 * (exp(0.00018 * x) - 1)) for x in x]
    # y4 = [0.1 * 0.0119 * exp(0.00015 * x) / (0.1 + 0.0119 * (exp(0.00015 * x) - 1)) for x in x]
    # y5 = [0.1 * 0.0117 * exp(0.00024 * x) / (0.1 + 0.0117 * (exp(0.00024 * x) - 1)) for x in x]
    # y6 = [0.1 * 0.012 * exp(0.00022 * x) / (0.1 + 0.012 * (exp(0.00022 * x) - 1)) for x in x]
    # y7 = [0.1 * 0.016 * exp(0.00018 * x) / (0.1 + 0.016 * (exp(0.00018 * x) - 1)) for x in x]
    # y8 = [0.1 * 0.017 * exp(0.00001 * x) / (0.1 + 0.017 * (exp(0.00001 * x) - 1)) for x in x]
    # y9 = [0.1 * 0.0175 * exp(0.00006 * x) / (0.1 + 0.0175 * (exp(0.00006 * x) - 1)) for x in x]
    # y10 = [0.1 * 0.0176 * exp(0.00001 * x) / (0.1 + 0.0176 * (exp(0.00001 * x) - 1)) for x in x]
    # y11 = [0.1 * 0.0284 * exp(0.00002 * x) / (0.1 + 0.0284 * (exp(0.00002 * x) - 1)) for x in x]
    y12 = [0.1 * 0.0284 * exp(0.000272 * x) / (0.1 + 0.0284 * (exp(0.000272 * x) - 1)) for x in x]

    # plt.plot([1531 for i in range(len(y))], y, c='black', linestyle="--", linewidth=1)
    # plt.plot([11316 for i in range(len(y))], y, c='black', linestyle="--", linewidth=1)
    # plt.plot([14459 for i in range(len(y))], y, c='black', linestyle="--", linewidth=1)
    # plt.plot([17351 for i in range(len(y))], y, c='black', linestyle="--", linewidth=1)
    # plt.plot([10844 for i in range(len(y))], y, c='black', linestyle="--", linewidth=1)
    # plt.plot([14459 for i in range(len(y))], y, c='black', linestyle="--", linewidth=1)
    # plt.plot([11830 for i in range(len(y))], y, c='black', linestyle="--", linewidth=1)
    # plt.plot([260268 for i in range(len(y))],y, c='black',linestyle = "--")
    # plt.plot([43378 for i in range(len(y))], y, c='black', linestyle="--", linewidth=1)
    # plt.plot([260268 for i in range(len(y))],y, c='black',linestyle = "--")
    # plt.plot([130134 for i in range(len(y))],y, c='black',linestyle = "--")
    # plt.plot([1531 for i in range(len(y))],y, c='black',linestyle = "--")
    # plt.plot(x, y1, c='blue', label='trial 8')
    # plt.plot(x, y2, c='yellow', label='trial 1')
    # plt.plot(x, y3, c='green', label='trial 2')
    # plt.plot(x, y4, c='red', label='trial 3')
    # plt.plot(x, y5, c='brown', label='trial 4')
    # plt.plot(x, y6, c='orange', label='trial 5')
    # plt.plot(x, y7, c='pink', label='trial 6')
    # plt.plot(x, y8, c='purple', label='trial 7')
    # plt.plot(x, y9, c='grey', label='trial 9')
    # plt.plot(x, y10, c='black', label='trial 10')
    # plt.plot(x, y11, c='blue', label='trial 11')
    plt.plot(x, y12, c='black', label='average')
    # plt.plot(x, [0.06 for i in range(len(x))], c='black', linewidth=2, linestyle="--")
    # plt.scatter(200, 0.0268 - 0.017 - 0.005, c='r', s=100, marker='8', label='Eighth test data')
    plt.xlabel('No. of SP bided', fontsize=15)
    plt.ylabel('SP price($/H)', fontsize=15)
    plt.legend(fontsize=12, loc=5)
    # plt.annotate('lowest \nnumber', xy=(1531, 0), xytext=(5000, 0.002), arrowprops=dict(facecolor='red', shrink=0.05))
    plt.savefig('Fig1')
    plt.show()


def pic4(_a_, _b_):
    pkl_file = open('data_middle.pkl', 'rb')

    LIST = pickle.load(pkl_file)

    pn, prn = private_cloud(LIST)
    # _a_ = [668.6937549860297, 939.9092129163337, 848.526420934258, 629.6561072513375, 668.692955356629,
    #        927.7781983613288]
    # _b_ = [5462.519910837557, 12792.009686189911, 4786.366765714456, 5452.009824866729, 6127.0120683630175,
    #        4187.488011342355]
    OD_task = []
    SP_task = []
    for num in range(6):
        if num == 0:
            ln = 0
        profit, task_OD, task_SP = ICOAO(LIST, num, pn, prn, _a_[num], _b_[num], ln)
        OD_task += task_OD
        SP_task += task_SP
        ln = max(_b_[num])

    x = [x * 7.5 for x in range(48)]
    pn = [sum(pn[:n]) for n in [x for x in range(len(pn))]]
    OD_task = [sum(OD_task[:n]) for n in [x for x in range(len(OD_task))]]
    SP_task = [sum(SP_task[:n]) for n in [x for x in range(len(SP_task))]]
    reject = [0 for x in range(48)]
    plt.plot(x, OD_task, color='r', marker='o', mec='r', mfc='r', label='on demand instance')
    plt.plot(x, SP_task, color='blue', marker='o', mec='blue', mfc='blue', label='spot instance')
    plt.plot(x, pn, color='green', marker='o', mec='green', mfc='green', label='private cloud')
    plt.plot(x, reject, color='y', marker='o', mec='y', mfc='y', label='rejected')
    plt.xlabel('time(mins)', fontsize=15)
    plt.ylabel('number of cumulative scheduled tasks', fontsize=15)
    plt.legend()
    plt.savefig('FIG2')
    plt.show()
    plt.close()


def pic5(_a_, _b_):
    pkl_file = open('data_middle.pkl', 'rb')

    LIST = pickle.load(pkl_file)

    pn, prn = private_cloud(LIST)
    # _a_ = [668.6937549860297, 939.9092129163337, 848.526420934258, 629.6561072513375, 668.692955356629,
    #        927.7781983613288]
    # _b_ = [5462.519910837557, 12792.009686189911, 4786.366765714456, 5452.009824866729, 6127.0120683630175,
    #        4187.488011342355]
    OD_task = []
    SP_task = []
    profit = []
    for num in range(6):
        if num == 0:
            ln = 0
        profit, task_OD, task_SP = ICOAO(LIST, num, pn, prn, _a_[num], _b_[num], ln)
        OD_task += task_OD
        SP_task += task_SP
        ln = max(_b_[num])

    TASK_num = [len(x) for x in LIST]
    sum_task_1 = [sum(TASK_num[:x]) for x in range(48)]
    sum_task_2 = [sum(TASK_num[:x]) for x in range(48)]
    sum_task_1.insert(len(sum_task_1), sum_task_1[-1])
    sum_task_2.insert(0, 0)
    x = [x * 7.5 for x in range(49)]
    plt.plot(x, sum_task_1, color='r', marker='o', mec='r', mfc='r', label='arriving tasks')
    plt.plot(x, sum_task_2, color='b', marker='o', mec='b', mfc='b', label='scheduled tasks')
    plt.plot(x, [0 for x in range(49)], color='y', marker='o', mec='y', mfc='y', label='rejected')
    plt.xlabel('time(min)', fontsize=15)
    plt.ylabel('number of tasks', fontsize=15)
    plt.legend()
    plt.savefig('fig3')
    plt.show()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2. - 0.2, 1.03 * height, '%s' % float(height))


def pic6(_a_, _b_):
    index = np.arange(6)
    a = plt.bar(index, [int(x) for x in _a_], width=0.4, color='b', label='on demand instance')
    plt.xlabel('time slot', fontsize=15)
    plt.ylabel('number of on demand instance', fontsize=15)
    axs = plt.gca()
    axs.set_ylim(0, 1000)
    plt.legend()
    autolabel(a)
    plt.savefig('fig7')
    plt.show()


def pic7(_a_, _b_):
    index = np.arange(48)
    b_tot = []
    for i in _b_:
        b_tot += i
    plt.plot(index, [int(x) for x in b_tot], color='b', marker='o', label='spot instance')

    plt.xlabel('hour number', fontsize=15)
    plt.ylabel('number of spot instance biding in each turn', fontsize=15)
    axs = plt.gca()
    axs.set_ylim(0, 1200)
    plt.legend()
    # autolabel(a)
    plt.savefig('fig8')
    plt.show()


def pic8():
    a = [0, 0, 50.9792987361633, 221.971079667734, 49.5889917771793, 181.329011859511, 48.2118423394682,
         543.900362507463, 49.1185472504562, 239.420593236236, 50.0067892191240, 191.138121856955, 48.3927130951098,
         211.265965843565, 49.9530362879272, 124.988068932895, 49.4251581725841, 191.505466870498, 47.7852559180127,
         150.395118988945, 49.4138107020665, 253.693302146548, 51.0863229492494, 241.120389420474, 50.0047721071384,
         229.269064875220, 51.2371332258966, 240.779045681494, 49.9504934097396, 261.168227183026, 50.3574702159500,
         333.200855555871, 48.6235125694881, 588.408541760999, 48.9475381708161, 548.838914786215, 49.0816168930673,
         277.854396060477, 49.5005490592370, 184.166014758671, 47.0465852306245, 669.945511742099, 49.9582705626379,
         237.449491071758, 48.1546772016640, 321.271002766264, 48.2039766186494, 444.702554283236, 48.4515041338136,
         99.4377155145447]
    plt.plot([x * 7.5 for x in range(len(a))], a, color='r', marker='o', mec='r', mfc='r', label='scheduled tasks')

    plt.ylabel('number of the scheduled tasks in 7.5 mins', fontsize=15)
    plt.xlabel('time(min)', fontsize=15)
    plt.legend()
    plt.savefig('PIC10')
    plt.show()


def pic9():
    a = [0, 47, 221, 47, 172, 47, 521, 47, 219, 47, 176, 47, 211, 47, 116, 47, 189, 47, 141, 47, 241, 47, 220, 47, 212,
         47, 223, 47, 257, 47, 315, 47, 566, 47, 526, 47, 254, 47, 172, 47, 611, 47, 223, 47, 307, 47, 417, 47, 99, 0]
    b = [0, 0, 0, 0, 2155.66666666667, 0, 1848.66666666667, 0, 0, 0, 2116.66666666667, 2544, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 2075, 0, 0, 2376, 0, 0, 2383, 0, 0, 0, 0, 2321.33333333333, 1973.33333333333, 2356, 0, 0, 2297.33333333333,
         0, 1918.33333333333, 0, 0, 0, 0, 0, 0, 2264, 0, 0]
    c = [0, 900.666666666667, 1440, 2341.33333333333, 0, 0, 0, 0, 0, 0, 0, 0, 2332.33333333333, 0, 0, 0, 0, 0,
         2141.33333333333, 2305.33333333333, 2139.33333333333, 2540.33333333333, 0, 2239.33333333333, 0, 0, 2131, 0, 0,
         0, 0, 2038, 1659, 0, 0, 0, 2317, 2664, 0, 2335.33333333333, 0, 2281, 0, 2232, 1981, 0, 1996, 0, 1994, 1560]
    d = [0, 0, 0, 0, 0, 2520, 0, 2034.33333333333, 1604.66666666667, 2275.66666666667, 0, 0, 0,
         2494.33333333333, 2329.66666666667, 2543, 2376.66666666667, 2543.33333333333, 0, 0, 0, 0, 0,
         0, 1910, 0, 0, 2470.33333333333, 0, 2627.66666666667, 1952.66666666667, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 1802, 0, 0, 2444, 0, 0, 0, 0]
    plt.plot([x * 7.5 for x in range(50)], a, color='y', marker='o', mec='y', mfc='y', label='private_cloud')
    plt.plot([x * 7.5 for x in range(50)], b, color='r', marker='o', mec='r', mfc='r', label='public cloud1')
    plt.plot([x * 7.5 for x in range(50)], c, color='b', marker='o', mec='b', mfc='b', label='public cloud2')
    plt.plot([x * 7.5 for x in range(50)], d, color='g', marker='o', mec='g', mfc='g', label='public cloud3')
    plt.legend()
    plt.gca().set_ylim(0, 3500)
    plt.xlabel('time(min)', fontsize=15)
    plt.ylabel('number of tasks per 7.5 mins', fontsize=15)
    plt.savefig('fig11')
    plt.show()


def pic10():
    a = [32.36805680608091, 31.668012366503355, 27.660739512719815, 30.332533694546015, 25.78478685849148,
         32.90896716814242, 29.665789795227067, 31.725327867869005]
    b = [31.415044028882615, 28.123525163230212, 36.06161682176523, 36.963447290001206, 36.0371394681517,
         32.404893590149854, 32.751748091361605, 32.46831605654569]
    c = [34.27823928879112, 33.167543228472695, 31.377612963305502, 31.66292612555571, 31.79350182239795,
         31.628883094006, 30.189156234142533, 31.585461884233766]
    d = [33.54430960321714, 33.23000889871145, 33.703867332359316, 32.437405853168215, 31.20920620530675,
         30.00672522515751, 31.56609598841047, 28.941595027169278]
    e = [39.62095303873246, 38.904450717327386, 36.12335596547612, 37.32046293052659, 35.445553430576915,
         33.7582653394234, 31.947393497955304, 30.383206967320092]
    f = [31.447486470425464, 34.02343906634506, 32.758733828914636, 27.68941575381748, 26.187925364169452,
         30.95802519130408, 28.83438060554736, 30.845457326762205]
    totel = [41.63926949112579,
             43.86610763518307,
             44.976735284323375,
             37.9688375797187,
             36.75487873628334,
             36.62502244932585,
             41.13172492067104,
             47.34129589593069,
             31.863959099877256,
             32.63123942888317,
             40.711242276371436,
             42.803251980070414,
             33.95111384383915,
             40.69350593792706,
             40.27122543268291,
             42.55139191202333,
             32.251365218829136,
             36.78450062426867,
             39.27733528672735,
             39.779142174896066,
             42.45240936006759,
             40.86692169647643,
             43.7784430246267,
             41.60128398892991,
             43.11110725755751,
             39.79328061636398,
             49.53047242800757,
             39.7434411266188,
             31.214583329581984,
             38.848706109797845,
             47.17569676701212,
             48.96866096753311,
             34.420640053427796,
             35.12786278288561,
             44.670437651639176,
             44.39396979663961,
             35.13885537492592,
             44.59938393230804,
             35.484285419223525,
             46.23997685490744,
             30.19509169678073,
             33.50902651875014,
             39.87960826512584,
             46.02042487599728,
             45.83668081179812,
             40.54153201964628,
             47.44829926232944,
             43.24721382243442,
             ]
    SO = [0, 15.8592937283263, 27.4042106714967, 38.2368203547701, 39.0069909565212, 39.7416657750804, 43.0044059328487,
          33.0799305771868, 32.6094280977872, 38.0893788604006, 38.4614116050198, 41.2848921955181, 42.5440708580312,
          42.3167041750478, 38.7112599539154, 43.3576825140082, 42.4690289822818, 37.3396053656691, 35.1708838647112,
          36.9137570238846, 40.3398145900454, 39.3162022639493, 37.6117760051419, 36.1529309317347, 35.1116905281608,
          38.6828953786524, 39.2118484063592, 40.5191362796086, 43.5293312532859, 41.9955978578223, 39.9280121768334,
          31.8293862091560, 42.1922433715303, 38.1925113349834, 44.9661869798978, 33.9468714475165, 40.2746592323965,
          44.9202775769255, 42.4997721569049, 36.9856295648996, 47.7955447769739, 38.7560624237677, 32.7383952956685,
          36.6923305776220, 39.2422390636865, 41.3842922112264, 42.8941917279342, 35.5273252523630, 33.4963614771916]
    PR = [1.38317333169185, 7.21904530810730, 1.59641281031323, 5.02497363090206, 1.43721345176978,
          17.3001180767526, 1.66201038672766, 7.15377773167253, 1.53553316569043, 5.39825554874246,
          1.88417868570099, 6.27670973381273, 1.46771963399682, 3.91038683741099, 1.94159401075564,
          6.69371161625943, 1.55780241264537, 4.42079033542087, 1.45524602788020, 8.14430886411479,
          1.72152960586062, 7.07649209441094, 1.61227849468977, 6.26806271992741, 1.54758248065237,
          7.04667812694705, 1.39293291516471, 7.90412403525012, 1.38963331067421, 10.3194002500081,
          1.62470582799982, 18.4373797889160, 1.75304958058766, 17.8089912320432, 1.78004669144428,
          7.69854372952714, 1.62722195790198, 5.67351318046083, 1.38527296610583, 20.1098767292699,
          1.11195968347538, 6.31932174709030, 1.62386393571807, 10.5582935093550, 1.56016793095361,
          12.1315935352219, 1.61070632387029, 2.93889063354264, ]
    totel.insert(0, 0)
    PR.insert(0, 0)
    SO = [x for x in SO]
    SO[0] = 0
    x = [x * 7.5 for x in range(len(totel))]
    plt.plot(x, totel, color='r', marker='o', mec='r', mfc='r', label='POA')
    plt.plot(x, PR, color='b', marker='o', mec='b', mfc='b', label='eco-IDC')
    plt.plot(x, SO, color='g', marker='o', mec='g', mfc='g', label='SAPSO')
    plt.legend()
    plt.xlabel('time(min)', fontsize=15)
    plt.ylabel('profit per 7.5 min($)', fontsize=15)
    plt.savefig('final')
    plt.show()

    print(sum(totel) / sum(SO) - 1)
    print((sum(totel) - sum(SO)) / 48)


def pic11():
    x = np.linspace(0.02, 0.05, 1000)
    plt.plot(x, [(1 / 0.000204) * exp((-1 / 0.000204) * 0.02 * (0.3 / (0.1 - 2 * x) - 1)) for x in x])
    # plt.ylim(0,1)
    plt.show()


if __name__ == '__main__':
    od = [449.51366338628213, 407.70122886297503, 459.8790478104646, 496.84199724564337, 432.2189598321702,
          481.0823914849194]
    sp = [[552.1522933617837, 473.74504645294957, 535.9958582985887, 434.5156557677739, 357.8391833884067,
           347.25674826701436, 423.76170629326333, 592.3254275554032], [459.6263124497453, 329.47361104141294,
                                                                        556.8444162094547, 521.1230546640435,
                                                                        312.92963988101883, 496.20696233781246,
                                                                        485.7107419268031,
                                                                        609.4061425573851],
          [411.2553886897025, 426.745828878658, 377.3599538844495, 377.5048039917648,
           448.612021801166, 418.0997559945549, 482.876995774533, 432.6973053339971], [485.70607230663603,
                                                                                       348.6311011117998,
                                                                                       594.5965813022142,
                                                                                       401.0692856340689,
                                                                                       318.4154990194509,
                                                                                       314.4565458595571,
                                                                                       548.1182301707058,
                                                                                       588.8076203745053],
          [593.297879314668, 560.0270213712563, 555.072581627174,
           551.0923464062035, 315.0872796630786, 566.4455937223175, 323.7606944544113, 658.1334765759012],
          [237.58829415116844, 457.4071687117012, 389.8140635301537, 528.4532537875398, 485.03716053637277,
           350.549904688571, 522.3815045387271, 515.0931771040804]]
    # pic3()
    x = 3399
    print(0.1 * 0.0284 * exp(0.000272 * x) / (0.1 + 0.0284 * (exp(0.000272 * x) - 1)))
