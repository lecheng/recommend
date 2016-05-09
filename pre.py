from util.file import *
import json

def getdict():
	tagdict = {}
	for i in read_data_from_file():
		templist = []
		templist = get_co_list(i.split(','))
		for j in templist:
			if tagdict.has_key(j):
				tagdict[j] +=1
			else:
				tagdict[j] = 1
	print 'tagdict size:' + str(len(tagdict))
	return tagdict

def get_co_list(tags):
	co_list = []
	for i in range(0,len(tags)):
		for j in range(i,len(tags)):
			co_list += [frozenset([tags[i],tags[j]])]
	#print len(tags)
	#print len(co_list)
	return co_list
	pass

def get_table():
	tag_tables = read_table_from_file()
	tagdict = {}
	tagdict = getdict()
	for key,value in tagdict.items():
		templist = list(key)
		valuelist = []
		if len(templist)==1:
			tag = templist[0]
			if tag_tables.has_key(tag):
				d = {}
				d[tag] = value
				tag_tables[tag] += [d]
			else:
				d = {}
				d[tag] = value
				tag_tables[tag] = [d]
		elif len(templist)==2:
			tag1 = templist[0]
			tag2 = templist[1]
			if tag_tables.has_key(tag1):
				d = {}
				d[tag2] = value
				tag_tables[tag1] += [d]
			else:
				d = {}
				d[tag2] = value
				tag_tables[tag1] = [d]
			if tag_tables.has_key(tag2):
				d = {}
				d[tag1] = value
				tag_tables[tag2] += [d]
			else:
				d = {}
				d[tag1] = value
				tag_tables[tag2] = [d]
	print len(tag_tables)
	#print tag_tables
	return tag_tables

def sort_table(tag_tables):
	for key,value in tag_tables.items():
		#print value
		sorted_value = sorted(value,key = lambda a:a.values()[0],reverse=True)
		tag_tables[key] = sorted_value
	return tag_tables

def save_table_to_file(tag_tables):
	path = 'table.txt'
	f = open(path,'w')
	for key,value in tag_tables.items():
		d = {}
		d['seed_tag'] = key
		d['trigger_tags'] = value
		f.write(json.dumps(d) + '\n')
	f.close()

def read_table_from_file():
	tag_tables = {}
	try:
		path = 'table.txt'
		f = open(path,'r')
		lines = f.readlines()
		for line in lines:
			print line
			jsonobj = json.loads(line)
			tag_tables[jsonobj['seed_tag']] = jsonobj['trigger_tags']
		f.close()
	except Exception, e:
		print e
	return tag_tables

def train():
	table = sort_table(get_table())
	save_table_to_file(table)

def query(s):
	table = read_table_from_file() 
	print len(table)
	print table[s]

def run():
	s = '3D'
	query(s)

if __name__ == '__main__':
	run()