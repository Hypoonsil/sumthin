#importing
import keyboard

#Functions
def welcome():
    print("Hello Master,\nWhat do you want to store today?")

#variables
file = open("C:\Users\Hypensil\Documents\Projects\BoWL\BOWL.txt", "w")
#starting main program
welcome()
FirstInput = input()
print("Okay Master,what should i store it as?")
SecondInput = input()
file.write(f"{FirstInput} - {SecondInput}")
print("Program Has Finished\nPress f to continue")
while True:
    if keyboard.is_pressed("f" or "F"):
        break
