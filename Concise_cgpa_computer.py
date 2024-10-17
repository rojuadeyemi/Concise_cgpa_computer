import re
def get_input(prompt, input_type=int, validation_fn=None, error_msg="Invalid input, try again"):
    while True:
        try:
            value = input_type(input(prompt).strip())
            if validation_fn and not validation_fn(value):
                raise ValueError()
            return value
        except:
            print(error_msg)

def is_valid_course_code(code):
    # Check if the code is exactly 6 characters long, starts with letters, and ends with numbers
    return bool(re.match(r'^[A-Za-z]{3}\d{3}$', code))

def get_course_code(prompt):
    return get_input(prompt, str, is_valid_course_code, "Invalid course code, try again").upper()

def get_grade(prompt):
    return get_input(prompt, str, lambda g: g in 'ABCDEFabcdef', "Invalid grade, please enter A, B, C, D, E, or F").upper()

# Map of grades to points
grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}

# Get number of courses
num_courses = get_input("\nEnter the number of courses you wish to compute CGPA for: ", int, lambda x: x > 0, "Please enter a valid number of courses.")

courses = []

# Collect course data
for i in range(num_courses):
    course_code = get_course_code(f"\nEnter the {'first' if i == 0 else 'next'} course code: ")
    course_unit = get_input("Enter the unit of the course entered above: ", int, lambda x: x > 0, "Please enter a valid unit.")
    course_grade = get_grade("Enter the grade of the course entered: ")

    courses.append({
        'code': course_code,
        'unit': course_unit,
        'grade': course_grade
    })

    print(f"\nCourse \"{course_code}\" saved!".center(44))

# Calculate CGPA
total_points = sum(grade_points[course['grade']] * course['unit'] for course in courses)
total_units = sum(course['unit'] for course in courses)
cgpa = total_points / total_units

# Display results
print('\n\nSummary Table')
print("".rjust(38, '='))
print("S/N", "Course-code".rjust(10), "Unit".rjust(8), "Grade".rjust(13))
print(''.rjust(38, '-'))

for i, course in enumerate(courses, start=1):
    print(i, course['code'].rjust(10), str(course['unit']).rjust(10), course['grade'].rjust(12))
    print(''.rjust(38, '-'))

print(''.rjust(61, '='))
print("Courses\t", "Cumulative-Total\t", "Total Units\t\t", "CGPA", '\n')
print(str(num_courses).rjust(4), str(total_points).rjust(13), str(total_units).rjust(19), str(f"{cgpa:.2f}".rjust(22)))
print(''.rjust(61, '='))

