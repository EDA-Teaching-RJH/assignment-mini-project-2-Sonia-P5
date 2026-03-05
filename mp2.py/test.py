def main():
    usernames=[]
    Hockey=[]
    Tennis=[]
    Basketball=[]
    Football=[]
    def options():
        print("---WELCOME TO THE PORTAL---")
        print("Clubs available at the Smile Factory Facility")
        print("Hockey, Tennis, Basketball, and Football")
        print("MENU")
        print("1. Create an Account")
        print("2. Overview of each club")
        print("3. Select a club(s) (Maximum 2)")
        print("4. Pay subscription for club")
        print("5. Exit")
    
        a=input("Select option: ")

        def create_new_user():
           import re
           if a=="1":
              name=input("What is your first name: ").capitalize()
              while name=="":
                        print("This is a mandatory field")
                        name=input("What is your first name: ").capitalize()

              last_name=input("What is your last name: ").capitalize()
              while last_name=="":
                        print("This is a mandatory field")
                        last_name=input("What is your last name: ").capitalize()

              nationality=input("What is your nationality: ")
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

              print("You must create a username. The username must begin with a number and end with the .SmileFF domain. It must be minimum 8 characters. ")
              while True:
                    username=str(input("Enter username: "))
                    if re.search(r"^\d.+\.+SmileFF$", username) and len(username)>=8:
                        print("Valid Username")
                        break
                    else:
                        print("Username not valid.")
                        continue

           usernames.append(username)
           print("Account Succesfully Created. Information stored")

        if __name__=="__main__":       
         create_new_user()

    if __name__=="__main__":
     options()

if __name__=="__main__":
    main()