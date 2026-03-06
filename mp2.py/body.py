import csv
def main():
    usernames=[]
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
        
        if a=="1":
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

           def form_username():    
            import re
            print("You must create a username. The username must begin with a number and end with the .SmileFF domain. It must be minimum 8 characters. ")
            while True:
               username=str(input("Enter username: "))
               if re.search(r"^\d.+\.+SmileFF$", username) and len(username)>=8:
                  print("Valid Username")
                  with open("Database.csv", "a") as file:
                     writer=csv.DictWriter(file, fieldnames=["User"])
                     writer.writerow({"User": username})
                  break
               else:
                  print("Username not valid.")
                  continue
            usernames.append(username)
            print("Account succesfully created. Data Stored")

           if __name__=="__main__":
              form_username()

          if __name__=="__main__":       
           create_new_user()
         
        if a=="2":
           def view_clubs():
              def displaying_info():
               class Clubs:
                 def __init__(self, name):
                    self.name=name
                  
                 def location(self):
                    print(f"This club is located at the Smile Factory Facility")
              
               class Hockey(Clubs):
                 def price(self):
                    print("$70")
               
               class Tennis(Clubs):
                 def price(self):
                    print("$30")
            
               class Basketball(Clubs):
                 def price(self):
                    print("$20")
            
               hockey=Hockey("Hockey")
               tennis=Tennis("Tennis")
               basketball=Basketball("Basketball")

               print(hockey.name)
               hockey.price()
               hockey.location()

               print("-----")

               print(tennis.name)
               tennis.price()
               tennis.location()

               print("-----")

               print(basketball.name)
               basketball.price()
               basketball.location()

              displaying_info()
              
              def showing_info():
               b=input("Which club would you like to view their members? Click H for Hockey, T for tennis, and B for basketball: ")
              
               if b=="H":
                 with open("members_of_hockey.txt", "r") as f:
                    f_contents=f.read()
                    print(f_contents, end="")

               elif b=="T":
                 with open("members_of_tennis.txt", "r") as f:
                    f_contents=f.read()
                    print(f_contents, end="")

               elif b=="B":
                with open("members_of_basketball.txt", "r") as f:
                  f_contents=f.read()
                  print(f_contents, end="")
              
               else:
                 print("Invalid input")
                 b=input("Which club would you like to view? Click H for Hockey, T for tennis, and B for basketball: ")

              if __name__=="__main__":
                 showing_info()
           

           if __name__=="__main__":  
              view_clubs()

        if a=="3":
           def sign_up_to_club():
            print("Signed Up Usernames")
            with open("Database.csv", "r") as f:
                    f_contents=f.read()
                    print(f_contents, end="")
            log_in=input("Please enter your username: ")


           sign_up_to_club()
           
           

    if __name__=="__main__":
     options()

if __name__=="__main__":
    main()