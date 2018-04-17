import random
Rounds = 0
Money_Left = 15
Left_Over_Money = 0
Most_Money = Money_Left
Highest_Round = 0

while Money_Left > 0 :
    D1 = (random.randint(1,6))
    D2 = (random.randint(1,6))
    roll = (D1 + D2)
    Rounds += 1
    print(D1 + D2)
    if roll == 7:
        print("You win 4 dollars")
        Money_Left += 4

        if Money_Left > Most_Money:
         Most_Money = Money_Left
         Highest_Round = Rounds

    else:
            print("You lose 1 dollar")
            Money_Left -= 1

    print("You have $%s" % Money_Left)



print("You lost all your money.")
print("You did %s rounds" % Rounds)
print("The most money you had was $%s." % Most_Money)
print("You should have stop at round %s." % Highest_Round)

