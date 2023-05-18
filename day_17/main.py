class User:
    def __init__(self,id_num,user_name):
        self.id=id_num
        self.username = user_name
        self.followers=0
        self.following=0

    def follow(self,user):
#beeing user the one we folow and self our own user.
        user.followers+=1
        self.following+=1


user_1 = User('001','Mauricio')
user_2 = User('002','Daniela')

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_1.following)
