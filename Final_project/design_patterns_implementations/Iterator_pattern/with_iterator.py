from abc import ABC,abstractmethod

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
    
class Iterator(ABC):

    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Employee:
        pass

class EmployeeIterator(Iterator) :

    position = -1
    
    def __init__(self,list):
        self.list = list

    def has_next(self) -> bool:
        if EmployeeIterator.position < len(self.list)-1:
            return True
        else :
            return False
        
    def next(self) -> Employee:
        EmployeeIterator.position +=1
        return self.list[EmployeeIterator.position]
    

class Collection(ABC):

    @abstractmethod
    def create_employees_iterator(self):
        pass

class EmployeeCollection (Collection):

    def __init__(self) -> None:
        self.EmployeesList = []
    
    def add_employee(self, employee):
        self.EmployeesList.append(employee)

    def create_employees_iterator(self):
        return EmployeeIterator (self.EmployeesList)
    

employee1 = Employee('employee1')
employee2 = Employee('employee2')
employee3 = Employee('employee3')
employee4 = Employee('employee4')
employee5 = Employee('employee5')

EmployeesList = EmployeeCollection()

EmployeesList.add_employee(employee1) 
EmployeesList.add_employee(employee2)
EmployeesList.add_employee(employee3)
EmployeesList.add_employee(employee4)
EmployeesList.add_employee(employee5)

iterator = EmployeesList.create_employees_iterator()

while iterator.has_next():
    employee = iterator.next()
    print(employee.get_name(),employee.id)
