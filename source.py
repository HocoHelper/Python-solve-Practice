import csv
import itertools
from collections import OrderedDict
import hashlib

def hash_password_hack(input_file_name, output_file_name):
    with open (input_file_name, 'r') as f:
        reader = csv.reader(f)
        f = open(output_file_name,"w")
        key=[]
        val1=[]
        for row in reader:
            name = row[0]
            val=[str(num) for num in row[1:]]
            key.append(name)
            val1.append(val)
            value = list(itertools.chain.from_iterable(val1)) 
            value=[str(i) for i in value]
        dict_csv = OrderedDict(zip(key, value))  
    listval=[]
    for item in dict_csv.values():
        listval.append(item)
    rainbow_dict = OrderedDict()
    for i in range(1000, 10000): 
        my_hash = hashlib.sha256(str(i).encode()).hexdigest()
        rainbow_dict[my_hash] = i

    list1=[k for k,v in dict_csv.items() if v in listval]
    list2=[v for k,v in rainbow_dict.items() if k in listval]
    list3 = [ item for pair in zip(list1, list2 + [0]) for item in pair]
    data=[]
    for item in list3:
        l3=[]
        l3.append(item)
        data.append(str(item))
    esm=data[::2]
    pas=data[1::2]
    XY = [i for i in zip(esm, pas)]
    for x,y in XY:
        f.write(str(x)+',')
        f.write(str(y)+'\n')

