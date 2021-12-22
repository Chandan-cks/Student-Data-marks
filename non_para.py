class Employee:
    id = ''
    name=''
    desg=''
    sal=''
    def __init__(self,name,id,desg,sal):
        self.id = id;
        self.name = name;
        self.desg = desg;
        self.sal = sal;
    def display (self):
        print("ID: %d \nName: %s \nDesg: %s\nSal: %d"%(self.id,self.name,self.desg,self.sal))
emp1 = Employee("John",101,"SA",25000)
emp2 = Employee("David",102,"SD",15000)
#accessing display() method to print employee 1 information
emp1.display();
#accessing display() method to print employee 2 information
emp2.display();

#wap in python to create a class to store details information about an object student rollno, name,branch,marks in 5 subject.then find out total mark,average mark and gread of a student.
