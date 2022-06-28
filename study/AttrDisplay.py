class AttrDisplay:
    def __getAttrsStr(self):#子类无需使用的方法用__（双下划线）开头
        attrs=[]
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key,getattr(self,key)))
        return ','.join(attrs)
    def __repr__(self):
        return '[%s:%s]' % (self.__class__.__name__,self.getAttrsStr())

if __name__=='__main__':
    class TopTest(AttrDisplay):
        count=0
        def __init__(self):
            self.attr1=TopTest.count
            self.attr2=TopTest.count+1
            TopTest.count+=2
    class SubTest(TopTest):
        pass

    X,Y=TopTest(),SubTest()
    print(X)
    print(Y)
