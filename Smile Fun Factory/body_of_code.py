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
                  with open("Database.csv", "r") as f:
                     f_contents=f.read()
                     print(f_contents, end="")
            
                  log_in=str(input("Please enter your username: "))

                  if log_in in open("Database.csv").read():
                     print("Username recognized. There are some steps to complete before sign up is succesfull")
                  else:
                     print("Username not registered. You must create an account or type a valid username to sign up to a club. Exiting programe...")
                  
                  call=input("Enter name or nickname you would like to be referred to as: ")

                  joining=input("What club would you like to join? Click H for Hockey, T for tennis, and B for basketball: ")
                  if joining=="H":
                     file=open("members_of_hockey.txt", "w")
                     y=[call]
                     file.writelines(y)
                     file.close

                  elif joining=="T":
                        with open("members_of_tennis.txt", "a") as f:
                           f_contents=f.read()
                           print(f_contents, end="")

                  elif joining=="B":
                        with open("members_of_basketball.txt", "a") as f:
                           f_contents=f.read()
                           print(f_contents, end="")
              
                  else:
                     print("Invalid input")
                     joining=input("What club would you like to join? Click H for Hockey, T for tennis, and B for basketball: ")

               sign_up_to_club()


    if __name__=="__main__":
     options()

if __name__=="__main__":
    main()