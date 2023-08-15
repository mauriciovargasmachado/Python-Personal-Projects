
string = input("please insert a frase: ")
letter = input("Please insert a final letter you choose!.")

for i in string:
    if i.lower()==letter.lower():
        break
    if i.lower()=="a":
        continue
    if i.lower()=="e":
        continue
    if i.lower()=="i":
        continue
    if i.lower()=="o":
        continue
    if i.lower()=="u":
        continue
    print(i,end="")
