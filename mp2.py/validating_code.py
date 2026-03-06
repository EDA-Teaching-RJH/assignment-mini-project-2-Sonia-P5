import re

def form_username(username):    
   print("You must create a username. The username must begin with a number and end with the .SmileFF domain. It must be minimum 8 characters. ")
   while True:
      username=str(input("Enter username: "))
      if re.search(r"^\d.+\.+SmileFF$", username) and len(username)>=8:
         return True
      return False

def main():
    email=input("What's your email? ").strip()
    if form_username(username):
        print("Valid")
    else:
        print("Invalid")
      
if __name__=="__main__":
      form_username()
