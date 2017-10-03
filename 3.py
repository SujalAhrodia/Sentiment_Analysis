#Calculate individual and average sentiment score
#Individual sentiment score 
from sentiment import sentiment_score
import json

data = []


for line in open('z_test_data.txt'):
b = line
a = sentiment_score(b)
data.append([b,a])




with open('z_saved_data.txt', 'w') as outfile:
json.dump(data, outfile)

