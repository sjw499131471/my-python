class FirstClass:
    def setdata(self,value):
        self.data=value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print("override display:"+self.data)

class ThridClass(SecondClass):
    def __init__(self,value):
        self.data=value
    def __add__(self,other):
        return SecondClass(self.data+other)
    def __str__(self):
        return '[ThridClass]:%s'%self.data

if __name__=='__main__':
    #self-test code
    x=FirstClass()
    x.setdata('test FirstClass')
    y=SecondClass()
    y.setdata('test SecondClass')
    z=ThridClass('test ThridClass')
    x.display()
    y.display()
    z.display()
    print(z)
