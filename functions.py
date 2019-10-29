students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)


vraag = True
while vraag:
    antwoord = input("Do you want to add another student")
    if antwoord == "Yes":
        vraag = True
        student_name = input("Enter student name: ")
        student_id = input("Enter a student id: ")
        add_student(student_name, student_id)
    else:
        vraag = False


print_students_titlecase()