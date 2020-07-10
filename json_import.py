import json

with open('sample.json') as json_file:
	data = json.load(json_file)

for k in data.keys():
	print(k + ':' , data[k])
