import random 
looper = 1
while looper <= 5:
            number = random.randint(1,5)
            #cheat code
            #print(number)
            #ask question and get input from user
            a = input("Can you guess the number I'm thinking of between 1 and 5?\n")
            
            if int(a) == number:
                print("that's right!")
                looper = 88

            else:
                print("wrong!, Try again...")
                looper += 1

            if looper == 3:
                print("Game over...")
                break