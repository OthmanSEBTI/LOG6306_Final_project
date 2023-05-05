class Employee :
    
    count=0
    
    def __init__(self,name) -> None:
        self.__name = name
        self.id = Employee.count
        Employee.count += 1 
        

    def get_name (self):
        return self.__name

    def get_id (self):
        return self.id



    

employee1 = Employee('employee1')
employee2 = Employee('employee2')
employee3 = Employee('employee3')
employee4 = Employee('employee4')
employee5 = Employee('employee5')

EmployeesList = [employee1,employee2,employee3,employee4,employee5]


for employee in EmployeesList :
    print(employee.get_name(),employee.id)
