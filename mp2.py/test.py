class Participant:
    def __init__(self, name, last_name, occupation, age):
        self.name=name
        self.last_name=last_name
        self.occupation=occupation
        self.age=age
participant1=Participant(Sonia, Piroso, )

print(f"User's first name: {Participant.name}")
print(f"User's last name: {Participant.last_name}")
print(f"User's occupation: {Participant.occupation}")
print(f"User's occupation: {Participant.age}")