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
    