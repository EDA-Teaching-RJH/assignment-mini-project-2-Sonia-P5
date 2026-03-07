log_in=str(input(" "))
if log_in in open("Database.csv").read():
    print("Yay")
else:
    print("nay")