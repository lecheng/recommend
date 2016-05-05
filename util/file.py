import os
import json

filenames = []
filenames = os.listdir('../data')

def read_data_from_file():
	for filename in filenames:
		path = '../data/' + filename
		f = open(path,'r')
		lines = f.readlines()
		for line in lines:
			video = json.loads(line)
			print video['tag']
		break
	pass

read_data_from_file()