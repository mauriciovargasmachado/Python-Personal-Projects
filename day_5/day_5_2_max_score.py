
# used with the numbers: 156 178 165 171 187 copy and paste the numbers structure


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0

for score in student_scores:
    if score>high_score:
        high_score=score

#the high_score takes the value of the biggest score and then you equal the high_score to score

print(f'The highest score in the class is: {high_score}')



