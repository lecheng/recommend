import os
import json

filenames = []
filenames = os.listdir('data')

def read_data_from_file():
	for filename in filenames:
		path = 'data/' + filename
		print path
		if '.txt' not in path:
			continue
		else:
			f = open(path,'r')
			lines = f.readlines()
			for line in lines:
				video = json.loads(line)
				yield video['tag']

read_data_from_file()