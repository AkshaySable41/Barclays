class Emp:
    def prdetails(self):
        self.name='Test'
        self.address='Jalna'
    def show(self):
        print('name:',self.name)
        print('address:',self.address)
class AddingProfessionaldetails(Emp):
    def deptdetails(self):
        self.dept_id=777
        self.dept_name='Mechanical'
    def show1(self):
        print('dept:',self.dept_id)
        print('deptName:',self.dept_name)
class ClientDetails(AddingProfessionaldetails):
    def t1(self):
        print('In t1')
obj=ClientDetails()
obj.t1()#Here all methods are accessable
#obj=AddingProfessionaldetails()
obj.prdetails()
obj.deptdetails()
obj.show()
obj.show1()

