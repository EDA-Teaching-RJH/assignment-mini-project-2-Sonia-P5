try:
    age=int(input("What is your age:  "))
except ValueError:
    print("Use numbers to type your age")
    age=int(input("What is your age:  "))