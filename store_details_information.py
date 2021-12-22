#wap in python to create a class to store details information about an object student rollno, name,branch,marks in 5 subject.then find out total mark,average mark and gread of a student.

class Student:
    marks = []
    def getData(self, rn, name,branch, m1, m2, m3,m4,m5):
        Student.rn = rn
        Student.name = name
        Student.branch = branch
        Student.marks.append(m1)
        Student.marks.append(m2)
        Student.marks.append(m3)
        Student.marks.append(m4)
        Student.marks.append(m5)
        
    def displayData(self):
        print ("Roll Number is: ", Student.rn)
        print ("Name is: ", Student.name)
        print ("Branch is: ",Student.branch)
        print ("Marks are: ", Student.marks)
        print ("Total Marks are: ", self.total())
        print ("Average Marks are: ", self.average())
        
    def total(self):
        return (Student.marks[0] + Student.marks[1] +Student.marks[2]+Student.marks[3]+Student.marks[4])
    
    def average(self):
        return ((Student.marks[0] + Student.marks[1] +Student.marks[2]+Student.marks[3]+Student.marks[4])/5)

#main program
rn = int (input("Enter the roll number: "))
name = input("Enter the name: ")
branch= input("Enter the Branch: ")
m1 = int (input("Enter the marks in the first subject: "))
m2 = int (input("Enter the marks in the second subject: "))
m3 = int (input("Enter the marks in the third subject: "))
m4 = int (input("Enter the marks in the fourth subject: "))
m5 = int (input("Enter the marks in the fiveth subject: "))

s1 = Student()
s1.getData(rn, name,branch, m1, m2, m3,m4,m5)
s1.displayData()
