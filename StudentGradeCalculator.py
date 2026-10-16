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

def calculate_total(hindi, english, math):
    total = hindi + english + math
    return total

def calculate_percentage(total):
    percentage = (total / 300) * 100
    return percentage

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    
    elif percentage >= 75:
        return "B"
    
    elif percentage >= 60:
        return "C"
    
    elif percentage >= 33:
        return "D"
    
    else:
        return "F"    

show_menu()

student_name = get_student_name()
print("Student Name:", student_name)

hindi, english, math = get_subject_marks()
print("Hindi Marks:", hindi)
print("English Marks:", english)
print("Math Marks:", math)

total_marks = calculate_total(hindi, english, math)
print("Total Marks:", total_marks)

percentage = calculate_percentage(total_marks)
print("Percentage:",  round(percentage, 2), "%")

grade = calculate_grade(percentage)
print("Grade:", grade)