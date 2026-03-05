while True:
        try:
            age=int(input("What is your age: "))
            break
        except ValueError:
            print("Use numbers to type your age")
            continue

