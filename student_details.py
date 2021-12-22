class student:
    def __init__(self,rn,name,branch,m1,m2,m3,m4,m5,total,average):
        self.rn=rn
        self.name=name
        self.branch=branch
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
        self.mark4=m4
        self.mark5=m5
        self.total=(self.mark1+self.mark2+self.mark3+self.mark4+self.mark5)
        self.average=(self.total/5)
    def display(self):
        print("Enter student roll number: ",self.rn)
        print("Enter student name: ",self.name)
        print("Enter student branch: ",self.branch)
        print("The total 5 marks: ",self.mark1,self.mark2,self.mark3,self.mark4,self.mark5)
        print("total marks: ",self.total)
        print("The average marks of student = ",self.average)
        print("the grade of student: ",self.point())
        
    def point(self):
        if self.average>=90:
           grade = 'A'
        elif self.average>=80 and self.average<90:
            grade='B'
        elif self.average>=70 and self.average<80:
            grade='C'
        elif self.average>=60 and self.average<70:
            grade='D'
        else:
            grade='E'
        return grade
#main function
rn=int(input("Enter student rollno: "))
name=input("enter name: ")
branch=input("enter branch")
m1= float(input("Enter the mark of subject 1: "))
m2= float(input("Enter the mark of subject 2: "))
m3= float(input("Enter the mark of subject 3: "))
m4= float(input("Enter the mark of subject 4: "))
m5= float(input("Enter the mark of subject 5: "))
t = m1+m2+m3+m4+m5
a = t/5
x = student(rn,name,branch,m1,m2,m3,m4,m5,t,a)
x.display()
