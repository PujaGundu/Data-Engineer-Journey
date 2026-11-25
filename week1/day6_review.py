scores =[50,70,90]
total = 0
for score in scores:
    total = total + score
average = total/len(scores)
if average >= 90 :
    grade = 'A'
elif average >= 80 :
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Average : {average}")
print(f"Grade : {grade}")

count = 5
while count >= 1:
    print(count)
    count = count -1 
print("Done")