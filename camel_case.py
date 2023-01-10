"""Part 3: camelCase

Write a program that turns a sentence into camel case. The first word is lowercase, 
the rest of the words have their initial letter capitalized, and all of the words are joined together. 
For example, with the input "fOnt proCESSOR and ParsER", your program will output "fontProcessorAndParser".

Optional extra question: print a warning message if the input will not produce a valid variable name. 
You don't need to be exhaustive in checking, but test for a few common issues, 
such as starting with a number, or containing invalid characters such as # or + or ".
Or, would it be easier to check that the name only contains valid characters?

Test your program with different example inputs, and comment your code. """


words = input("Write a sentence to be converted to camel case: ") #getting the sentence to be converted from the user

word_list = words.split() #splitting the sentence up into individual strings
camelized_sentence = word_list[0].lower() #making the first word in the sentence lower case
for i in range(1,len(word_list)): #counting each next word in the sentence
    camelized_sentence+=word_list[i].title() #making each next word in the sentence have an uppercase first letter

print("This is your sentence camelized: \n" +  camelized_sentence + '\n') #showing the user their sentence camelized
print('Goodbye!') #saying goodbye to the user and making sure the application closes correctly