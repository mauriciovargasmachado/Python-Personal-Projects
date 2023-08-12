print("********************************************")
print("********* Vacation calculator system ********")
print("********************************************")
print("")
print("")

employee_name = input("please insert the name of the employee: ")
department_code =input("please insert the department code: ")
employee_age = float(input("Please insert how many years the employee has been working in the company: "))

if department_code ==1:
    if employee_age >= 1 and employee_age<2:
        print("The employee "+employee_name+" Have right to 6 days of vacations.")
    elif employee_age >=2 and employee_age<=6:
        print("The employee " + employee_name + " Have right to 14 days of vacations.")
    elif employee_age >=7:
        print("The employee " + employee_name + " Have right to 20 days of vacations.")
    else:
        print("The employee " + employee_name + " Dont have vacation periods to take yet.")

elif department_code == 2:
    if employee_age >= 1 and employee_age < 2:
        print("The employee " + employee_name + " Have right to 7 days of vacations.")
    elif employee_age >= 2 and employee_age <= 6:
        print("The employee " + employee_name + " Have right to 15 days of vacations.")
    elif employee_age >= 7:
        print("The employee " + employee_name + " Have right to 22 days of vacations.")
    else:
        print("The employee " + employee_name + " Dont have vacation periods to take yet.")

elif department_code == 3:
    if employee_age >= 1 and employee_age <2:
        print("The employee " + employee_name + " Have right to 10 days of vacations.")
    elif employee_age >= 2 and employee_age <= 6:
        print("The employee " + employee_name + " Have right to 20 days of vacations.")
    elif employee_age >= 7:
        print("The employee " + employee_name + " Have right to 30 days of vacations.")
    else:
        print("The employee " + employee_name + " Dont have vacation periods to take yet.")

else:
    print("The department code do not exist, please try again")