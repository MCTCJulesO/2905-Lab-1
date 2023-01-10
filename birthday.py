"""Part 1: Hello, birthday month

Write a program that asks for your name and the month you were born in.

Then, your program should print
A greeting to you, using your name
A message with the number of letters in your name
A 'Happy birthday month!' message if you were born in the current month
Easier - compare the user's input to "January" or "August" or whatever the current month is
Harder - use Python to figure out the current month and use that in the comparison.
 Check out the datetime library."""


name = input('Hello, please enter your name ') #asking the users name

birth_month_from_user = input('Please enter the name of the month you were born in ') #asking the users birth month
birth_month = birth_month_from_user.strip().lower() #converting is to a lowercase string to it can be compared regardless of upper or lower case

letters_in_name = len(name) #getting the length of the users name

print('Hello ' + name + '!') #saying hello to the user using the name they entered

print('There are ' + str(letters_in_name) + ' letters in your name') #showing how many letters are in the name the user entered

if birth_month == 'january': #comparing the month the user entered to the current month
    print('Happy birthday month!') # if it is their birthday month a nice message is printed

print('Goodbye!') #saying goodbye to the user and also making sure the application is exiting correctly