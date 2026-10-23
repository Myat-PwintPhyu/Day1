def greet(name):
    print(f"Hello , {name}!")

greet('Ma Ma ')
greet('Mg Mg ')   

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores)/len(scores)



def calculate_total(scores):
    return sum(scores)

def classify_grade(score):
    if score < 0 or score > 100:
       return "invalid"
    elif score >=80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"

def count_passed (score):
    passed_count = 0
    for score in scores:
        if score >= 40:
            passed_count+=1
    return passed_count

scores =[45,70,85,60,80]
average = calculate_average(scores)
print(f"average ={average}")
total = calculate_total(scores)
print(f"total={total}")
passcount = count_passed(scores)
print(f"passcount={passcount}")
grade  = classify_grade(90)
print(f"grade={grade}")













    