#Average sentiment score
import json

data = []
with open('z_saved_data.json') as data_file: 
data = json.load(data_file)

sum1=0
for i in range(0,len(data)):
sum1 = sum1 + data[i][1]


print sum1/len(data)

