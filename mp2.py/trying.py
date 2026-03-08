import re

def feedback(hashtag):
    if re.search(r"^#\D.+$", hashtag):
        return True
    return False

def main():
    hashtag=str(input(("We're trying to promote our facility, we could use your help! Could you reccomend a slogan with a hashtag we can use on social media? Please type here, don't forget to include the hashtag! Please don't include numbers:  ")))
    if feedback(hashtag):
        print("Valid")
    else:
        print("Invalid")
if __name__=="__main__":
    main()