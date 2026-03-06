
import re
import csv
def form_username():    
        print("You must create a username. The username must begin with a number and end with the .SmileFF domain. It must be minimum 8 characters. ")
        while True:
            username=str(input("Enter username: "))
            if re.search(r"^\d.+\.+SmileFF$", username) and len(username)>=8:
                print("Valid Username")
                break
            else:
                print("Username not valid.")
                continue
        print("Account succesfully created. Data Stored")
        
def main():
    email=input("Insert username: ")
    if form_username(username):
        print("Username accepted")
    else:
        print("Username not accepted")
              

if form_username(username):
    print("Account Succesfully Created. Information stored")

    with open("Database.csv", "a") as file:
        writer=csv.DictWriter(file, fieldnames=["user"])
        writer.writerow{{"User": username}}
else:
    print("Account Creation Unsuccesfull. Exiting programme.")

if __name__=="__main__":
    main()
