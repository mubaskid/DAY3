students = {}


def Average(lst):
    return sum(lst) / len(lst)


while True:
    name = input("enter student name: ")
    score = int(input("enter student score: "))

    students[name] = score

    repeat = input("would you like to add another student?" "(yes/no)")
    
    if repeat == 'no':
        break

print("-------RESULT-------")
for name, score in students.items():
    print(name, "your score is: ", score)


avg = Average(students.values())

highest = max(students, key=students.get)

lowest = min(students, key=students.get)

print('avg :', avg)
print('highest :', highest)
print('lowest :', lowest)


# Assuming there are 10 student in a class offering 10 courses each, write a program that;
# a) Collect the score of each student for all score.
    # b) Sum the score scored in all courses by a particular student and gives the maximum, average, and minimum of score of each student.
    # c) Calculate the average, maximum, and minimum of scores for each courses.