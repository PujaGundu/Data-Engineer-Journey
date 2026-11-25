fruits = ["apple","banana","mango"]
print(fruits)
print(fruits[0])
print(len(fruits))
fruits.append("orange")
print(fruits)
for fruit in fruits:
    print(f"Fruit: {fruit}")


scores = [60,80,90,100]
total = 0
for score in scores:
    total = total + score
print(total)
print(total/len(scores))


scores = [60, 80, 90, 100]
total = 0

for score in scores:
    total = total + score

print(f"Total: {total}")
print(f"Average: {total / len(scores)}")

student = {"name": "Puja", "city": "Fremont", "score": 90}
print(student["name"])
print(student["score"])

student["passed"] = True
print(student)

for key, value in student.items():
    print(f"{key}: {value}")

numbers = [10, 20, 20, 30, 30, 30]
unique_numbers = set(numbers)

print(unique_numbers)
print(len(unique_numbers))
print(20 in unique_numbers)

full_name = "  Puja Gundu  "
clean_name = full_name.strip()

print(clean_name)
print(clean_name.lower())
print(clean_name.split())

raw_name = "  Puja Gundu  "
clean_name = raw_name.strip()
name_parts = clean_name.split()

print(clean_name)
print(name_parts[0])

scores = [60,80,90,100]
total = 0
for score in scores:
    total = total + score
    average = total/len(scores)
print(f" Average :{average}")

subjects = ["Python","SQL","Python","Git","SQL"]
unique_subjects = set(subjects)
print(f"{unique_subjects} = {len(unique_subjects)}")

student = {"name" : clean_name, "first_name" : name_parts[0],"city": "Fremont", "average" :average, "passed" :average >= 60}
print(student)
print(f" Student :{student['name']}, First name : {student['first_name']},City :{student['city']},Average : {student['average']},Passed :{student['passed']},Unique subjects count : {len(unique_subjects)}")