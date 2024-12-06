import pandas as pd
name=input("Enter your name: ").title()
course_code_list=[]
course_grade_list=[]
course_unit_list=[]
total_unit_load=0
total_points=0
while True:
    course=input("\nEnter the course code(Type 'Done' if you are done entering the courses): ").upper()
    if course == "DONE":
        if not course_code_list:
            print("Thanks")
        break
    course_code_list.append(course)

    while True:
        course_grade = input("Enter the grade: ").upper()
        if course_grade in ['A', 'B', 'C', 'D', 'E', 'F']:
            course_grade_list.append(course_grade)
            break
        else:
            print("Please enter a valid grade (A, B, C, D, E, F).")

    course_unit=int(input("Enter the unit load: "))
    total_unit_load+=course_unit
    course_unit_list.append(course_unit)
    
    if course_grade=='A':
        point=course_unit*5
        total_points+=point
    if course_grade=='B':
        point=course_unit*4
        total_points+=point
    if course_grade=='C':
        point=course_unit*3
        total_points+=point
    if course_grade=='D':
        point=course_unit*2
        total_points+=point
    if course_grade=='E':
        point=course_unit*1
        total_points+=point
    if course_grade=='F':
        point=course_unit*0
        total_points+=point
cgp=total_points/total_unit_load

course_data = {
    "Courses": course_code_list,
    "Grade":course_grade_list,
    "Unit":course_unit_list
}

transcript_table = pd.DataFrame(data=course_data)
print (transcript_table)
print()

print(f"Dear {name}, your CGPA is {cgp:.2f}")
if cgp >= 4.5:
    print("You made first class. BRAVO!!!")
elif cgp >= 3.5:
    print("You made second class upper. You did good.")
elif cgp >= 2.5:
    print("You made second class lower. That's okay.")
elif cgp >= 1.5:
    print("You made third class class.")
elif cgp >= 1.0:
    print("You made a pass.")
else:
    print("Not even up to a pass. That's very very poor.")