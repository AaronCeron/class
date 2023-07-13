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
        user = user.lower()
        if user == "student":
            self.student_creation()
        if user == "teacher":
            self.teacher_creation()
        if user == "homeroomteacher":
            self.homeroom_teacher_creation()
        if user == "end":
            return


    def manage(self):
        manage = input("Select the field to edit: student, teacher, homeroomteacher: ")
        if manage == "student":
            student_name = input("Enter your name: ")
            for student in self.students:
                if student_name == student.name:
                    print(f"user card:\n Name:{student.name}\n Surname:{student.surname}\n Classname:{student.classname}.")            
        if manage == "teacher":
            teacher_name = input("Enter your name: ")
            for teacher in self.teachers:
                if teacher_name == teacher.name:
                    print(f"user card:\n Name:{teacher.name}\n Surname:{teacher.surname}\n Subject:{teacher.subject}\n. Classes:{teacher.classes}.")
        if manage == "homeroomteacher":
            homeroomteacher_name = input("Enter your name: ")
            for homeroomteacher in self.homeroomteachers:
                if homeroomteacher_name == homeroomteacher.name:
                    print(f"user card:\n Name:{homeroomteacher.name}\n Surname:{homeroomteacher.surname}\n Classname:{homeroomteacher.classname}.")


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