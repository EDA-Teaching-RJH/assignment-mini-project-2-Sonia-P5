def pay():
    import re

    pay_up=input("Please transfer: ")
    if re.search("^#\D.+$", pay_up):
        print("Payment accepted. Thank you")
    else:
        print("Invalid Input")
if __name__=="__main__":
 pay()

#if re.search("^#.+$", pay_up):