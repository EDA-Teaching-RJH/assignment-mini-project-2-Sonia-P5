import csv
def main():
    def options():
        print("---WELCOME TO THE PORTAL---")
        print("Clubs available at the Smile Factory Facility")
        print("Hockey, Tennis, and Basketball")
        print("MENU")
        print("1. Create an Account")
        print("2. Overview of each club")
        print("3. Select a club ")
        print("4. Pay subscription for club")
        print("5. Customer Feedback")
        print("6. Exit")
    
        a=input("Select option: ")


        if a=="3":
           def sign_up_to_club():
            print("Signed Up Usernames")
            with open("Database.csv", "rt") as f:
                    f_contents=f.read()
                    print(f_contents, end="")
            
            log_in=str(input("Please enter your username: "))
            if log_in in csv:
               print("There are some steps to complete before sign up is succesfull")
            else:
               print("Username not registered. You must create an account or type a valid username to sign up to a club. Exiting programe...")


           sign_up_to_club()
           
           

    if __name__=="__main__":
     options()

if __name__=="__main__":
    main()