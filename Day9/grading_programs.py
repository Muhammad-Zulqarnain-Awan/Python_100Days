student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}

student_grades = {}

for student_name in student_scores:
    student_score = student_scores[student_name]
    if student_score > 90 and student_score <=100:
        student_grades[student_name] = "Outstanding"
        
    elif student_score > 80 and student_score <=90:
        student_grades[student_name] = "Exceeds Expectation"
        
    elif student_score > 70 and student_score <=80:
        student_grades[student_name] = "Acceptable"
        
    elif student_score <=70:
        student_grades[student_name] = "Fail"

print(student_grades)
