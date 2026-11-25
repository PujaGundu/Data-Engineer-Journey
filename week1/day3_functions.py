def calc_average(score1, score2):
    return (score1 + score2) / 2
average = calc_average(60,80)
print(average)


def grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
result = grade(90)
print(result)
result1 = grade(70)
print(result1)
result2 = grade(45)
print(result2)

def get_score(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That was not a number - try again.")
score = get_score("Enter your score:")
print(score)

score1 = get_score("First test score: ")
score2 = get_score("Second test score: ")
average = calc_average(score1, score2)
print(f"Average score: {average}")
print(f"Grade: {grade(average)}")

if average >= 60:
    print("Pass!")
else:
    print("Keep practising - you'll get there.")