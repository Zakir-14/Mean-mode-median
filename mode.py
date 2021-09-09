import csv
from collections import Counter
#from statistics import mode
with open("data.csv",newline="") as f :
    reader = csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)) :
    n_num=file_data[i][2]
    new_data.append(float(n_num))

data=Counter(new_data)

newList= data.items()
value=data.values()  
#print(max(value))   
mode = [] 
for weight,occurance in data.items():
    if occurance == max(value) :
        mode.append(weight)

#Mode  = mode(newList)
print(mode)