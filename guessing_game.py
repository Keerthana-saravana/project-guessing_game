import random   #to generate a random number
def guessing_game():
    #getting the user name
    name=input("enter your name:")
    print(f"Hello {name},Welcome to the guessing game!!")
    print("I will think a number between 1 to 100 and you have to  guess it!!")
    print("Maximum attempts is 15!!")
    #to generate a random number by the machine
    machine_number=random.randint(0,100)
    attempts=0 
    while True:
        try:
            #getting input from the user
            user_guess=int(input("enter your guess:"))
            attempts+=1  #increasing the attempts by 1
                
            if attempts==15 and machine_number!=user_guess:
                print(f"your attempts are over.the correct number is {machine_number}")
            if user_guess<machine_number:
                print("number is too low!!,try again")
            elif user_guess>machine_number:
                print("number is too high!!,try again")
            else:
                print(f"congrats {name}!, you guessed the correct number!!")
                print(f"you guessed the number in {attempts} attempts!")
                break     #exit the loop
        except ValueError:
            print("Invalid input !!.please enter a valid input")   #to handle the invalid input 
#function calling
guessing_game()            

        