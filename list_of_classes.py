"""Part 2: List of classes

Write a program that asks for the names of all of the classes you are taking this semester
Save these class names in a list.
Print all the items in the list, one per line."""


class_list = [] # making a list to be populated
class_input = 'Start'
while class_input:
    class_input = input('What classes are you taking? Press enter with no input to finish: ') #getting the classes the user is taking
    class_list.append(class_input) #adding their input to the list
class_list.pop()

for item_num,item in enumerate(class_list): #showing the classes the user entered in a nice format from the list
    print(f"Item {item_num+1:>5}: {item:>20}") #counting each class and giving it a number in the list

print('Goodbye!') #saying goodbye to the user and making sure the application exits corectly