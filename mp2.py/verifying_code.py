def showing_info():
    if b=="H":
        with open("members_of_hockey.txt", "r") as f:
         f_contents=f.read()
         print(f_contents, end="")

    elif b=="T":
        with open("members_of_tennis.txt", "r") as f:
         f_contents=f.read()
         print(f_contents, end="")

    elif b=="B":
        with open("members_of_basketball.txt", "r") as f:
         f_contents=f.read()
         print(f_contents, end="")
              
    else:
        print("Invalid input")
        b=input("Which club would you like to view? Click H for Hockey, T for tennis, and B for basketball: ")

if __name__=="__main__":
    showing_info()