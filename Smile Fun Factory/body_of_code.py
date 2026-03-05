def main():
    usernames=[]
    Hockey=[]
    Tennis=[]
    Basketball=[]

    def options():
        print("---WELCOME TO THE PORTAL---")
        print("Clubs available at the Smile Factory Facility")
        print("Hockey, Tennis, and Basketball")
        print("Menu")
        print("1. Create an Account")
        print("2. Overview of each club")
        print("3. Select a club(2) (Maximum 2)")
        print("4. Pay Subscription for club")
        print("5. Exit")

        a=input("Select option: ")

        def create_new_user():
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
                    name=input("Name: ").capitalize()

                last_name=input("Last Name: ").capitalize()
                while last_name=="":
                    print("This is a mandatory field")
                    last_name=input("What is your last name: ").capitalize

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

                
                            
    