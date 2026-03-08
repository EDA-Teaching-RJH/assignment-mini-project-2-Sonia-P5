import re

def feedback(hashtag):
    if re.search(r"^#\D.+(SmileFF|hockeySmileFF|tennisSmileFF|basketballSmileFF)$", hashtag):
        return True
    return False

def main():
    hashtag=str(input(("We're trying to promote our facility, we could use your help! Reccomend a hashtag we could use on social media! Make sure to include a hashtag. Either end the hashtag in SmileFF, hockeySmileFF, tennisSmileFF, or basketballSmileFF depending on what facility you want your hashtag to apply to. Please do not include any numbers:   ")))
    if feedback(hashtag):
        print("Valid")
    else:
        print("Invalid")
if __name__=="__main__":
    main()