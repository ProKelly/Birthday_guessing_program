import os
name = input("Enter your name: ")
print(name + " answer the questions bellow for the program to gues your bithday\n ")
day = 0
question1 = '''is your birthday in set 1
 1 3 5 7\n9 11 13 15\n17 19 21 23\n25 27 29 31\n\nEnter 0 for No and 1 for Yes:'''
answer = eval(input(question1))
if answer == 1:
    day += 1
    
    
question2 = '''is your birthday in set 2
 2 3 6 7\n10 11 14 15\n18 19 22 23\n26 27 30 31\n\nEnter 0 for No and 1 for Yes:'''
answer = eval(input(question2))
if answer == 1:
    day += 2
    
    
question3 = '''is your birthday in set 3
 4 5 6 7\n12 13 14 15\n20 21 22 23\n28 29 30 31\n\nEnter 0 for No and 1 for Yes:'''
answer = eval(input(question3))
if answer == 1:
    day += 4
    
    
question4 = '''is your birthday in set 4
 8 9 10 11\n12 13 14 15\n24 25 26 27\n28 29 30 31\n\nEnter 0 for No and 1 for Yes:'''
answer = eval(input(question4))
if answer == 1:
    day += 8
    
    
question5 = '''is your birthday in set 5
 16 17 18 19\n20 21 22 23\n24 25 26 27\n28 29 30 31\n\nEnter 0 for No and 1 for Yes:'''
answer = eval(input(question5))
if answer == 1:
    day += 16
    
print("\n"+ name + " Your birthday is on the "+ str(day) + "!")

os.system("pause")
