import random

def pick_winner(names):
    if not names:
        return "No participants to choose from!"
    
    winner = random.choice(names)
    return f"Congratulations, {winner}! You are the winner!"

names = []

while True:
    name = input("Enter a name (or -1 to finish): ")
    
    if name == "-1":
        break
    
    if name.strip():
        names.append(name.strip())

print(pick_winner(names))