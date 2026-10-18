def show_menu():
    print("======= STUDENT GRADE CALCULATOER =======")
    print("1. Calculate Student Grade.")
    print("2. Exit.")

def get_student_name():
    while True:
        name = input("Enter student name:").strip()

        if name:
            return name

        else:
            print("Name cannot be empty. Please enter a name.")    

def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (1 to 100): "))
            if 0 <= marks <= 100:
                return marks
            
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")        

def get_subject_marks():
    hindi = get_valid_marks("hindi")
    english = get_valid_marks("hindi")
    math = get_valid_marks("hindi")
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

def check_result(percentage):
    if percentage >= 33:
        return "PASS"

    else:
        return "FAIL"

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

result = check_result(percentage)
print("Result:", result)