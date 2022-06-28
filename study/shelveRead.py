import shelve
db=shelve.open('classdb')
for key in db:
	print(key,'=>',db[key])