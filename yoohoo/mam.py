import re

email=input((" "))
if re.search(r"^\w+@\w.+\.(ac.uk|gov.uk)$", email):
    print("good")
else:
    print("nay")