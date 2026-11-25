with open("student.txt","w")as file:
    file.write("Puja scored 82.5")
with open("student.txt","r") as file:
    content = file.read()
print(content)

import math
print(math.sqrt(81))
print(math.ceil(82.5))

user = input("Enter your name :")
raw_name = user
print(raw_name)
name = raw_name.strip()
print(f"Hello {name} , Welcome to day 5")   

def get_score(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That was not a number - try again.")

score = get_score("Enter one score: ")
print(score)

score1 = get_score("Enter score 1: ")
score2 = get_score("Enter score 2: ")
score3 = get_score("Enter score 3: ")

scores = [score1, score2, score3]
total = 0
for score in scores:
    total = total + score
average = total /len(scores)
print(f"Average : {average}")

score1 = get_score("Enter score 1: ")
score2 = get_score("Enter score 2: ")
score3 = get_score("Enter score 3: ")
average = total/len(scores)
if average >= 90 :
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70 :
    grade = "C"
elif average >= 60 :
    grade = "D"
else :
    grade = "F"
print(f"Grade: {grade}")
subjects = ["Python","SQL","Python","Git","SQL"]
unique_subjects = set(subjects)
student = {"name": name, "scores": scores, "average": average, "grade": grade, "passed": average > 60, "unique_subjects": len(unique_subjects)}
print(student)

with open("report.txt","w")as file:
    file.write(f"student name : {student['name']}\n")
    file.write(f"student scores :{student['scores']}\n")
    file.write(f"student avergae :{math.ceil(student['average'])}\n")
    file.write(f"student grade : {student['grade']}\n")
    file.write(f"student passed :{student['passed']}\n")
    file.write(f"student unique subjects :{student['unique_subjects']}\n")
with open("report.txt","r") as file:
    content = file.read()
print(content)

