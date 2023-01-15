
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


list_length = 0
for height in student_heights:
    list_length += 1

list_sum = 0
for height in student_heights:
    list_sum += height

average = round(list_sum/list_length)

print(f"The average height in {student_heights} is {average}.")
