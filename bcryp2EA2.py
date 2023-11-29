from colorama import Fore, Style, Back
import bcrypt
import random

userArr = []
streak = 0



def guessGame():
    global streak
    if userArr:
        arrSize = len(userArr)
        randomNum = random.randint(0, arrSize-1)
        randomUser = userArr[randomNum][0]
        randomUserPass = userArr[randomNum][1]
        result = False
        numTries = 0
        while not result and numTries < 5:
            guessPass = input("Can you try guessing the password for " + Fore.GREEN + "{}: ".format(randomUser) + Fore.WHITE)
            numTries = numTries + 1
            encodedGuess = guessPass.encode('utf-8')
            result = bcrypt.checkpw(encodedGuess, randomUserPass)
        if numTries > 4:
            print(Fore.RED + "Too many attempts.")
            print("You had a streak of ", streak)
            exit()
            regAgain()
        elif numTries == 1:
            print(Fore.GREEN + "You guessed the password correctly on the first try!")
            streak = streak + 1
            streakStr = "Your streak is: "
            if(streak == 1):{
                print(streakStr + Fore.RED + "1")
            }
            elif(streak < 3):{
                print(streakStr, Fore.RED, streak)
            }
            elif(streak < 6):{
                print(streakStr, Fore.YELLOW, streak)
            }
            else:{
                print(streakStr, Fore.GREEN, streak, Fore.WHITE + "! Keep going!")
            }
            
            regAgain()
        else:
            print("You guessed the password correctly in ", numTries, " tries!")
            streak = streak + 1
            streakStr = "Your streak is:"
            
            if(streak < 3):{
                print(streakStr, Fore.RED, streak)
            }
            elif(streak < 6):{
                print(streakStr, Fore.YELLOW, streak)
            }
            else:{
                print(streakStr, Fore.GREEN, streak, Fore.WHITE + "! Keep going!")
            }
            regAgain()

def register():
    

    
    user = input(Fore.GREEN + "Enter a username: " + Fore.WHITE)
    if user in [data[0] for data in userArr]:
        print(Fore.RED + "Username taken" + Fore.WHITE);
        user = input(Fore.GREEN + "Enter a username: " + Fore.WHITE)
        
    else:
        print("Thank you" + Fore.GREEN, user, Fore.WHITE)
    #print(userArr)

    password = input("Enter a password: ")
    
    encodedPw = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hashpass = bcrypt.hashpw(encodedPw, salt)

    userAndPass = [user, hashpass]
    userArr.append(userAndPass)
    guessGame()
    #print(userArr)


def regAgain():
    global streak
    choice = int(input(Fore.WHITE + "Enter 1 to register another user! Enter 0 to give up!"))
    if(choice == 1):
        register()
    else:
        print("You had a streak of ", streak)
        with open('userAndPass.txt', 'w') as file:
            for data in userArr:
                file.write(f"{data[0]}:{data[1]}\n")
        exit()
    



doReg = 45
while(doReg != 1 or 0 or 2):
    doReg = int(input(Style.BRIGHT + Fore.WHITE + Back.BLACK + "Do you want to register? " + Fore.GREEN + "1" + Fore.WHITE + " for yes " + Fore.RED +  "0" + Fore.WHITE + " for no. Type " + Fore.CYAN + "2" + Fore.WHITE + " to load userAndPass.txt: "))

    if(doReg == 1):
        register()
    elif(doReg == 0):
        print("Exiting")
        exit()
    elif(doReg == 2):
        
        with open('userAndPass.txt', 'r') as file:
            lines = file.readlines()
            userArr = [line.strip().split(':') for line in lines]
            userArr = [[data[0], data[1].encode('utf-8')] for data in userArr]
        guessGame()
    else:
        print("Enter " + Fore.GREEN + "1 or " + Fore.RED +  "0" + Fore.WHITE + ".")


    
        
        
    

