#This is a lottery game created by Derrick Hobbs under Creative Common Attribution Non Commercial (CC BY -NC) License#
import random
a = int(input("What is your lottery number"))
random_number = random.randint(1,10)
if a == random_number:
    print(random_number)
    print("     **  ")
    print("    *****")
    print("  **     ")
    print("  **     ")
    print("    *****")
    print("         **")
    print("         **") 
    print("    *****")
    print("     ** ")
    print("You have won the lottery!!!")
else:
    print("Wrong number")
