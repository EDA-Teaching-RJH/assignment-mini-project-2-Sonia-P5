def main():
    print("---WELCOME TO THE PORTAL---")
    print("Clubs available at the Smile Factory Facility")
    print("Hockey, Tennis, Basketball, Football, and Dance")
    print("1. Create an Account")
    print("2. Overview of each club")
    print("3. Select a club(s) (Maximum 2)")
    print("4. Pay subscription for club")

    a=input("Select and Option: ")

    Hockey=["Jessica", "Ryan"]
    Tennis=["Kelly"]
    Basketball=["Bryan", "Shelly", "Linda"]
    Football=[]
    Dance=["Kai", "Zayn", "Cole", "Lloyd"]

    import re 
    if a=="1": 
        print("OPTION SELECTED: Create an account")
        print("You must create a username. The username must begin with a number and end with .SmileFF. It must be minimum 8 characters. ")
        username=str(input("Enter username:  "))
        while username=="":
            print("This is a mandatory field")
            username=str(input("Enter username:  "))
        if re.search(r"^\d.+\.+SmileFF$", username) and len(username)>=8: 
            print("Valid Username")
        else:
                print("Username not valid. Opting out of Option 1")
        print("Extra informatio Needed before making your account")
                

        
        
if __name__=="__main__":
    main()



 
