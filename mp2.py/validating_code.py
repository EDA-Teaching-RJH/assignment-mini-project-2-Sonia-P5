import re

def form_username(username):
    if re.search(r"^\d.+\.+SmileFF$", username):
        return True
    return False

def main():
    username=str(input("Enter username: "))
    if form_username(username):
        print("Valid")
    else:
        print("Invalid")

if __name__=="__main__":
    main()