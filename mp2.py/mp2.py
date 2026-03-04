print("---WELCOME TO THE PORTAL---")
print("Clubs available at the Smile Factory Facility")
print("Chess, Tennis, Pottery, Archery, and Dance")
print("1. Create an Account")
print("2. Overview of each club")
print("3. Select a club(s) (Maximum 2)")

a=input("Select and Option: ")

chess=()
tennis=()
pottery=()
archery=()
dance=()

import re 
if a=="1":
    print("OPTION SELECTED: Create an account")
    b=input("Type in your first name: ").capitalize()
    c=input("Type in your last name: ").capitalize()
    print("You must create a username. The username must begin with a number, and end with .SFF. Special character's are not allowed. It must be miniimum 8 characters. ")
    username=input("Enter username:  ")
    if re.search(".", username):
        print(f"Username accepted. Welcome {username} ")