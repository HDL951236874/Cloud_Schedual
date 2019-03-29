import csv
import numpy as np
"""
this programme is to process the data in the data_release
which is to delete the useless lines in the data set
"""
list_of_arrive_tasks = np.random.randint(2000,3000,48)

tmp = []
totel_list = []
for num in range(1,49):
    csv_reader = csv.reader(open('data/data_'+str(num)+'.txt','r'))
    for index in csv_reader:
       tmp.append(index)
    totel_list.append(tmp)
    tmp = []

new = []
new_totel = []
for num in range(len(totel_list)):
    l = np.random.randint(0,len(totel_list[num])-1,list_of_arrive_tasks[num])
    for index in l:
        new.append([float(totel_list[num][index][0].split(" ")[0]),float(totel_list[num][index][0].split(" ")[1])])
    new_totel.append(new)
    new =[]

for index in new_totel:
    l = np.random.rand(len(index))*5
    for num in range(len(index)):
        index[num].append(l[num])

for num in range(1,49):
    a = new_totel[num-1]
    np.savetxt('data_base/data_set_'+str(num)+'.txt',a)

