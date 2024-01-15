class Emp:
    def __int__(self,id,name,city,sal):
        self.id=id
        self.name=name
        self.city=city
        self.sal=sal
    def show(self):
        print('Id:',self.id)
        print('NAME:',self.name)
        print('CITY:',self.city)
        print('SAL:',self.sal)
class DeptAdded(Emp):
    def __init__(self,deptId,deptname):
        super().show()
        self.deptId=deptId
        self.deptName=deptname
    def show1(self):
        super().show()
        print('DEPTID:',self.deptId)
        print('DEPTNAME:',self.deptId)
obj=DeptAdded(101,'Akshay')
obj2=obj.show()







