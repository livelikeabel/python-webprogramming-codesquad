class User:
    num_users = 0 # class variables

    #생성자
    def __init__(self, name):
        self.name = name # instance variables
        User.num_users += 1

u = User('honux')
print(User.num_users, u.name)
u2 = User('crong')
print(User.num_users, u2.name)
print(User.num_users, u.num_users, u2.num_users)
