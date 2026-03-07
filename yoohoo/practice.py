def campaign():
                  import re
                  
                  class Socials:
                     def __init__(self, trend):
                        self.trend=trend

                        def message(self):
                           print("We are thinking of making a social media campaign to promote the Hockey club! Please input a social media hashtag you think could help. We may choose yours! Make sure it starts with a hastag." )
                           yo=input("Enter proposed hashtag: ")
                           if re.search(r"^#.+$", yo):
                              print("Valid Username")
                           else:
                              print()
                     
                  class Hockey(Socials):
                     def start(self):
                        print("We hope you enjoy Hockey! Make sure to pay the fee.")
                  
                  class Tennis(Socials):
                     def start(self):
                        print("We hope you enjoy Tennis! Make sure to pay the fee.")
                  
                  class Basketball(Socials):
                     def start(self):
                        print("We hope you enjoy Tennis! Make sure to pay the fee.")
                  
                  hockey=Hockey("Hockey")
                  tennis=Tennis("Tennis")
                  basketball=Basketball("Basketball")

                        

               
               if __name__=="__main__":
                  campaign()