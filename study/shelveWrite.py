from ClassTest1 import FirstClass
x=FirstClass()
x.setdata('1')
import shelve
db=shelve.open('classdb')
db['x']=x
db.close()