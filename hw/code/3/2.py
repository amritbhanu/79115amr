from __future__ import division, print_function
class Employee:
    """Employee class"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __lt__(self,other):
        return self.age < other.age
        
    def __repr__(self):
        return 'Employee Name:'+repr(self.name) + 'Age:'+repr(self.age)+'\n'
        

if __name__ == "__main__":
    e1=Employee("Amrit", 22)
    e2=Employee("Mno", 23)
    e3=Employee("Ijk", 21)
    e4=Employee("Abc", 26)
    e5=Employee("Xyz", 17)
    employees=[e1,e2,e3,e4,e5]
    print (sorted(employees))
