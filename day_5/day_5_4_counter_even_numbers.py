

# sum the even numbers in range 

counter =0

for number in range(1,101):
    if number %2 ==0:
        counter+=number
print(counter)


# Or

counter2 =0

for number2 in range(1,101,2):
    counter2+=number2
print(counter2)