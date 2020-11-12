# Write a Python program to display a user entered name followed by Good Afternoon using input()func
name = input("Enter a name: ")
print("Good Afternoon " , name)

# Write a program to fill in a template given below with name and date.
letter = '''Dear <|Name|>,
You are selected!
Date: <|Date|>
'''
name = input("Enter your name: ")
date = input("Enter date: ")
letter = letter.replace("<|Name|>" , name)
letter = letter.replace("<|Date|>" , date)
print(letter)

# Write a program to detect double spaces in a string.
a = "Spandan is a very good boy. He is learning python.  He will soon make India proud."
print(a.find("  "))

# Replace the double spaces from problem 3 with single spaces.
a = "Spandan is a very good boy. He is learning python.  He will soon make India proud."
print(a.replace("  " , " "))

# Write a program to format the following letter using escape sequence characters.
'''
letter = "Dear Spandan, This Python course is nice. Thanks!
'''
letter = "Dear Spandan,\n\tThis Python course is nice.\nThanks"
print(letter)