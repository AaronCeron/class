type_of_user = ["student", "teacher", "homeroomteacher"]
commands = ["create", "manage", "end"]


class Student:
    def __init__(user):

        user.name = input("Enter your first name: ")
        user.surname = input("Enter your surname: ")
        user.classname = input ("Enter your classname: ")
        
class Teacher:
    def __init__(user):

        user.name = input("Enter your first name: ")
        user.surname = input("Enter your surname: ")
        user.subject = input("Enter your Subject: ")
        user.classes = input("Enter your classes : ")
        
class Homeroomteacher:
    def __init__(user):

        user.name = input("Enter your first name: ")
        user.surname = input("Enter your surname: ")
        user.classname = input ("Enter your classname: ") 
        

class Menu:
    def __init__(user):
        user.students = []
        user.teachers = []
        user.homeroomteachers = []

    def student_creation(user):
        student = Student()
        user.students.append(student)
        print("Student created correctly")

    def teacher_creation(user):
        teacher = Teacher()
        user.teachers.append(teacher)
        print("Teacher created correctly")

    def homeroomteacher_creation(user):
        homeroomteacher = Homeroomteacher()
        user.homeroomteachers.append(homeroomteacher)
        print("Homeroomteacher created correctly")


    def user_creation(user):
        user = input("Enter type of user: student, teacher, homeroomteacher: ")
        if user == "student":
            user.student_creation()
        if user == "teacher":
            user.teacher_creation()
        if user == "Homeroomteacher":
            user.homeroomteacher_creation()
        if user == "end":
            return
        else:
            print("error")


    def manage(user):
        manage = input("Select the field to edit: student, teacher, homeroomteacher, classname: ")
        if manage == "student":
            user.manage_student()
        if manage == "teacher":
            user.manage_teacher()
        if manage == "homeroomteacher":
            user.manage_homeroomteacher()
        if manage == "classname":
            user.manage_classname()

    def manage_student(user):



menu = Menu()
while True:
    command = input ("Enter the command you want to chose: create, manage, end: \n"
                     "create, to start the profile creation\n"
                     "manage, to dispaly the information required\n"
                     "end, to terminate the program")
    if command not in commands:
        print("Please enter a valid command: ")
        continue
    if command == "create":
        menu.user_creation()
    if command == "manage":
        menu.manage()
    if command == "end":
        break