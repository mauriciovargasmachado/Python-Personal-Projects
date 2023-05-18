
name = input("What is your name?: ")
last_name = input("What is your last name?: ")


def formated_names(f_name,l_name):
    formated_name =f_name.title()
    formated_last_name=l_name.title()
    return f"{formated_name} {formated_last_name}"

print(formated_names(name,last_name))