class User:
    def __init__(self, name, last_name, nationality, age):
        self.name=name
        self.last_name=last_name
        self.nationality=nationality
        self.age=age
    
def collecting():
    user=get_user()
    print(f"Information Collected: {user.name} {user.last_name}, {user.nationality}, {user.age} years old")

def get_user():
    name=input("Name: ").capitalize()
    while name=="":
        print("This is a mandatory field")
        name=input("What is your first name: ").capitalize()

    last_name=input("Last Name: ").capitalize()
    while last_name=="":
        print("This is a mandatory field")
        last_name=input("What is your last name: ").capitalize()

    nationality=input("Nationality: ").capitalize()
    while nationality=="":
        print("This is a mandatory field")
        nationality=input("What is your nationality: ")
    while True:
                try:
                    age=int(input("What is your age: "))
                    break
                except ValueError:
                    print("Use numbers to type your age")
                    continue
    user=User(name, last_name, nationality, age)
    return user

if __name__=="__main__":
    collecting()