# Je fabrique le moule ( classe)
class User:
    # Je vais créer un attribut password
    user_created= 0
    password = ''

    # création d'une méthode
    def __init__(self, password):
        self.password = password
        User.user_created += 1


admin = User('password')
print(User.user_created)
