Grade_Categories = ("Excellent", "Good", "Pass", "Fail")

students = [
    {"name": "Mg Mg", "age": 20, "study_hour": 2, "score": 30},
    {"name": "Aung Aung", "age": 22, "study_hour": 3, "score": 60},
    {"name": "Hla Hla", "age": 21, "study_hour": 4, "score": 70},
    {"name": "Su Su", "age": 23, "study_hour": 5, "score": 70}
]

def average_score(scores):
    if len(scores) == 0:
        return 0    
    total = sum(scores ) / len(scores)
    return total
    

def classify_grade(score):
    if score > 100 or score < 0:
        return "Invalid Score"
    elif score >= 80:
        return Grade_Categories[0]
    elif score >= 60:
        return Grade_Categories[1]
    elif score >= 40:
        return Grade_Categories[2]
    else:
        return Grade_Categories[3]

def passed_count(students):
    count = 0
    for student in students:
        if student["score"] >= 40:
            count += 1
    return count

def performance_report(studentreport):
    print("===Student Performance Report===")
    for student in studentreport:
        grade = classify_grade(student["score"])
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Study Hours: {student['study_hour']}")
        print(f"Score: {student['score']}")
        print(f"Grade: {grade}")

        scores = [student["score"] for student in students]
        total_students = len(studentreport)
        average = average_score(scores)
        highest_score = max(scores)
        lowest_score = min(scores)
        passed_students = passed_count(students)
        failed_students = total_students - passed_students
        top_students = [s["name"]for s in students if s["score"] == highest_score]
        top_student_str = ", ".join(top_students)

        print("===Summary===")
        print(f"Total Students: {total_students}")
        print(f"Average Score: {average}")
        print(f"Highest Score: {highest_score}")
        print(f"Lowest Score: {lowest_score}")
        print(f"Total Passed Students: {passed_students}")
        print(f"Total Failed Students: {failed_students}")
        print(f"Top Student: {top_student_str}")

performance_report(students)     



