
#for i in range(1,5):
 #   x= input("please type a number: ")
  #  y=int(x)**i
   # print(y)

number = int(input("what multiplication table do you want to evaluate?: "))

print(f"The evaluated multiplication table is: {number}")

for i in range (number):

    result= number*i

    print(f"{number}*{i} = {result}")