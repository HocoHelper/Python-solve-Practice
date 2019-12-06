import math
import csv
from statistics import mean
import operator
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name, newline='') as f:
        reader = csv.reader(f)
        f = open(output_file_name, "w")
        for row in reader:
            name=row[0]
            numbers=list()
            for number in row[1:]:
                numbers.append(int(number))
            average=float(mean(numbers))
            f.write(name+',' )
            f.write(str(average)+'\n')
        f.close()
            


def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name, newline='') as f:
        reader = csv.reader(f)
        f = open(output_file_name, "w")
        num=[]
        names=[]
        for row in reader:
            name=row[0]
            numbers=list()
            for number in row[1:]:
                numbers.append(int(number))
            names.append(name)
            num.append(float(mean(numbers)))
            dictionary = OrderedDict(zip(names, num))
        sorted_d = sorted(dictionary.items(),key=lambda t: t[::-1])
        for x,y in sorted_d:
            f.write(str(x)+',' )
            f.write(str(y)+'\n' )
        f.close()

def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name,newline='') as f:
        reader=csv.reader(f)
        f = open(output_file_name,"w")
        num=[]
        names=[]
        for row in reader:
            name=row[0]
            numbers=list()
            for number in row[1:]:
                numbers.append(int(number))
            names.append(name)
            num.append(float(mean(numbers)))
            dictionary = OrderedDict(zip(names, num))
        sorted_d = sorted(dictionary.items(),key=lambda t: t[::-1])
        rev=list(reversed(sorted_d))
        for x,y in rev[:3]:
            f.write(str(x)+',' )
            f.write(str(y)+'\n' )
        f.close()


def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name,newline='') as f:
        reader=csv.reader(f)
        f = open(output_file_name,"w")
        num=[]
        names=[]
        for row in reader:
            name=row[0]
            numbers=list()
            for number in row[1:]:
                numbers.append(int(number))
            names.append(name)
            num.append(float(mean(numbers)))
            dictionary = OrderedDict(zip(names, num))
        sorted_d = sorted(dictionary.items(),key=lambda t: t[::-1])
        for x,y in sorted_d[:3]:
            f.write(str(y)+'\n' )
        f.close()


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name,newline='') as f:
        reader=csv.reader(f)
        f = open(output_file_name,"w")
        num=[]
        names=[]
        for row in reader:
            name=row[0]
            numbers=list()
            for number in row[1:]:
                numbers.append(int(number))
            names.append(name)
            num.append(float(mean(numbers)))
        all_ave=float(mean(num))
        f.write(str(all_ave))
        f.close()
        
