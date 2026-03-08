def feedback():
               import re
               hashtag=str(input(("We're trying to promote our facility, we could use your help! Reccomend a hashtag we could use on social media! Make sure to include a hashtag. Either end the hashtag in SmileFF, hockeySmileFF, tennisSmileFF, or basketballSmileFF depending on what facility you want your hashtag to apply to. Please do not include any numbers:   ")))
               if re.search(r"^#\D.+$", hashtag):
                 print("Thank you for your idea! We'll review it.")
               else:
                 print("Wrong format for hashtag. You have one more attempt before we proceed to the next section")
               
if __name__=="__main__":
      feedback()