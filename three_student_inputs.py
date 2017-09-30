lloyd = {
    "name":"Lloyd",
    "homework": [90,97,75,92],
    "quizzes": [ 88,40,94],
    "tests": [ 75,90]
    }
alice = {
    "name":"Alice",
    "homework": [100,92,98,100],
    "quizzes": [82,83,91],
    "tests": [89,97]
    }
tyler = {
    "name":"Tyler",
    "homework": [0,87,75,22],
    "quizzes": [0,75,78],
    "tests": [100,100]
    }
student = ["lloyd","alice","tyler"]
## get the average of scores for each list within the dictionary##
def average(lst):
    return sum(lst)/len(lst)


##get the average of each individual score given it's overall effect on final grade##    
def get_average(student):
    hw = average(student["homework"]) * .10
    quiz = average(student["quizzes"]) * .30
    test = average(student["tests"]) * .60
    weighted_average = hw + quiz + test
    return weighted_average


##convert each weighted_average value to a letter grade##
def get_letter_grade(score):
    if score >= 90:
        return "A"
    if 80 <= score < 90:
        return "B"
    if 70 <= score < 80:
        return "C"
    if 60 <= score < 70:
        return "D"
    if score < 60:
        return "F"

##little test for correct output##
print get_letter_grade(get_average(lloyd))

##get average of the entire class##
def get_class_average(student):
    L = get_average(student[0])
    A = get_average(student[1])
    T = get_average(student[2])
    return (L+T+A) / 3.0  
    
students = [lloyd, alice, tyler]

print get_class_average(students) 
print get_letter_grade(students)
