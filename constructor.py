class student:
    company_name='Barclays'#class variable
    def __init__(self,r,n,a):
        self.roll=r
        self.name=n
        self.address=a
    def show(self):
        print('Roll:',self.roll)
        print('Name:',self.name)
        print('Address:',self.address)
        print('CompanyName:',student.company_name)#To access class variable use class name.variable name
s1=student(101,'Akshay','Jalna')
s1.show()
print(s1.name)