import re
def pay(pay_up):
   if re.search("^\$.+$", pay_up):
        return True
   return False

def main():
     pay_up=input("Please transfer: ")
     if input(pay_up):
          print("Valid")
     else:
          print("Invalid")
if __name__=="__main__":
    pay()