
import random

# in python we write in upper case constant (not changed during run)
CAPITAL_CITIES = [
    "TOKYO", "PARIS", "LONDON", "BERLIN", "MADRID",
    "ROME", "VIENNA", "PRAGUE", "WARSAW", "ATHENS",
    "CAIRO", "ANKARA", "BEIJING", "SEOUL", "HANOI",
    "BANGKOK", "CANBERRA", "OTTAWA", "BRASILIA", "BUENOS AIRES"
]

random.seed(1)

city = random.choice(CAPITAL_CITIES)
print(city)
print('_ ' * len(city))
    # 'A'
    # _ _ _ _ _ _
    # _ A _ _ A _
    # 'T'
    # _ A _ _ A _
    # 'R'
    # _ A R _ A _

hangman = 5

print(f"You have {hangman} guesses left")
guss = input("Guss a word: ")

while str(len(guss)) != 1:
    hangman -= 1
    if hangman == 0:
        print("you out of gusses")
        break
    print(f"You have {hangman} guesses left")
    guss = input("Guss a word: ")

city.split(" ")
