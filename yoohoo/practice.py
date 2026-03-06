class Clubs:
    def __init__(self, name):
        self.name=name
        
    def location(self):
        print(f"This club is located at the Smile Fun Factory")

class Hockey(Clubs):
    def price(self):
        print("$70")

class Tennis(Clubs):
    def price(self):
        print("$30")

class Basketball(Clubs):
    def price(self):
        print("$20")

hockey=Hockey("Hockey")
tennis=Tennis("Tennis")
basketball=Basketball("Basketball")

print(hockey.name)
hockey.price()
hockey.location()

print("------")

print(tennis.name)
tennis.price()
tennis.location()

print("------")

print(basketball.name)
basketball.price()
basketball.location()
