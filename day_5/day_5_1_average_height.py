
# used with the numbers: 156 178 165 171 187 copy and paste the numbers structure

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0

for student in student_heights:
    total_height += student
print(f'the sum of the height is: {total_height}')

total_students = 0

for student in student_heights:
    total_students +=1
print (f'The amoung of students is: {total_students}') 

average =round(total_height/total_students)

print (average)