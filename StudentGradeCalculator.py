def show_menu():
    print("======= STUDENT GRADE CALCULATOER =======")
    print("1. Calculate Student Grade.")
    print("2. Exit.")

def get_student_name():
    name = input ("Enter student name:")
    return name    

def get_subject_marks():
    hindi = float(input("Enter Your hindi mark:"))
    english =float( input("Enter Your english mark:"))
    math = float(input("Enter Your math mark:"))
    return hindi, english, math 

show_menu()

student_name = get_student_name()
print("Student Name:", student_name)

hindi, english, math = get_subject_marks()
print("Hindi Marks:", hindi)
print("English Marks:", english)
print("Math Marks:", math)