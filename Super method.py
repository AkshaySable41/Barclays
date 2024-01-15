class A:
    def test(self):
        print('from a')
class B(A):
    def test(self):
        #super(C,self).test()   # this will not execute
        print('from b')
class C(B):
    def test(self):
        print('from c')
class D(C):
    def test(self):
        super(B,self).test()   #call directly from a
        print('from d')

obj=D()
obj.test()