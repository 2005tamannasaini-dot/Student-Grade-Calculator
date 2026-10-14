def show_menu():
    print("======= STUDENT GRADE CALCULATOER =======")
    print("1. Calculate Student Grade.")
    print("2. Exit.")

def get_student_name():
    name = input ("Enter student name:")
    return name    

show_menu()

student_name = get_student_name()
print("Student Name:", student_name)
