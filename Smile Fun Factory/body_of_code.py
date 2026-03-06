import csv
def main():
    name=input("What is your name?")
    email=input("What is your email")

    def is_valid_email(email):
        import re
        if re.search(r"^\w+@\w.+\.(ac.uk|gov.uk)", email):
    if is_valid_email(email):
        print("Valid email. Saving to contacts...")

        with open("contacts.csv", "a") as file:
            write=csv.DictWriter(file, fieldnames=["names", "email"])
            write.writerow({"name": name, "email": email})

    else:
        print("Invalid email. Not saved")