class Person:   #부모 클래스
    def __init__(self, name, phoneNumber):
        self.Name = name
        self.PhoneNumber = phoneNumber
    def PrintInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))
    def PrintPersonData(self):
        print("Person(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

class Student(Person): #자식클래스 (Person에서 상속받음)
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self,name,phoneNumber) #부모 클래스 생성자 호출
        self.Subject = subject
        self.StudentID = studentID

    def PrintStudentData(self): #새로운 메서드 추가
        print("Student(Subject: {0},Student ID: {1})".format(self.Subject,self.StudentID))

    def PrintInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))
        print("Info(Subject:{0}, Student: {1})".format(self.Subject, self.StudentID))
