type_of_user = ["student", "teacher", "homeroomteacher"]
commands = ["create", "manage", "end"]


class Student:
    def __init__(self):

        self.name = input("Enter your first name: ")
        self.surname = input("Enter your surname: ")
        self.classname = input ("Enter your classname: ")
      

class Teacher:
    def __init__(self):

        self.name = input("Enter your first name: ")
        self.surname = input("Enter your surname: ")
        self.subject = input("Enter your Subject: ")
        self.classes = input("Enter your classes: ") 

class Homeroomteacher:
    def __init__(self):

        self.name = input("Enter your first name: ")
        self.surname = input("Enter your surname: ")
        self.classname = input ("Enter your classname: ") 
    
        
print ("Hello, welcome in our classroom creator.\n ")
class Menu:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.homeroomteachers = []

    def student_creation(self):
        student = Student()
        self.students.append(student)
        print("Student created correctly")

    def teacher_creation(self):
        teacher = Teacher()
        self.teachers.append(teacher)
        print("Teacher created correctly")

    def homeroom_teacher_creation(self):
        homeroomteacher = Homeroomteacher()
        self.homeroomteachers.append(homeroomteacher)
        print("Homeroomteacher created correctly")


    def user_creation(self):
        user = input("Enter type of user: student, teacher, homeroomteacher: ")
        if user == "student":
            self.student_creation()
        if user == "teacher":
            self.teacher_creation()
        if user == "Homeroomteacher":
            self.homeroom_teacher_creation()
        if user == "end":
            return


    def manage(self):
        students = {}
        teachers = {}
        homeroomteachers = {}
        manage = input("Select the field to edit: student, teacher, homeroomteacher: ")
        if manage == "student":
            name = input("Enter your first name: ")
            surname = input("Enter your surname: ")
            if (name,surname) in students:
                students [name, surname].print()
        if manage == "teacher":
            name = input("Enter your first name: ")
            surname = input("Enter your surname: ")
            if (name,surname) in teachers:
                teachers [name, surname].print()
        if manage == "homeroomteacher":
            name = input("Enter your first name: ")
            surname = input("Enter your surname: ")
            if (name,surname) in homeroomteachers:
                homeroomteachers [name, surname].print()


menu = Menu()
while True:
    command = input ("Enter the command you want to choose: create, manage, end: \n"
                     "create, to start the profile creation.\n"
                     "manage, to dispaly the information required.\n"
                     "end, to terminate the program.\n")
    if command not in commands:
        print("Please enter a valid command: ")
        continue
    if command == "create":
        menu.user_creation()
    if command == "manage":
        menu.manage()
    if command == "end":
        break