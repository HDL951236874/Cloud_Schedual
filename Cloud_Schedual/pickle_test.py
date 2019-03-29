import pickle
import csv

totle_list = []
for num in range(1,49):
    num_list = []
    csv_reader = csv.reader(open("data_base/data_set_"+str(num)+".txt","r"))
    for index in csv_reader:
        num_list.append([float(index[0].split(' ')[0]),
                         float(index[0].split(' ')[1]),
                         float(index[0].split(' ')[2])])
    totle_list.append(num_list)

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data_middle.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(totle_list, output)

# Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)

output.close()