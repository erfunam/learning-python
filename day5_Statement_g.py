from random import randint

score = 0

while True :
    i = int(input("Adad bezan : "))
    numRandom = randint(1, 6)
    if i == numRandom :
        score += 1
        print(f"WoW U Win, your score {score}")
        continue
    elif score == 5 :
        break
    else :
        print(f"U Lost, your score {score}")