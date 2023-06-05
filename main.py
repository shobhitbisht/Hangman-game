import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Genarate a random word and assign it to a variable "chosen_word"
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Defining an empty list called display and a varible called life with value 7
print(chosen_word)
display = []
life = 6

#Assigning display variable as many as blanks as there are letters in the chosen_word:
for word in chosen_word:
  display += "_"

print("################################\n")
print("Welcome to the world of hangman\n")
print("################################\n")
print(f"The random letter is {display} {len(display)} words long.")

while life > 0 and "_" in display:
  
  guess = input("Guess a letter: ").lower()
  
  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
      display[i] = guess
  
  if  guess not in chosen_word:
    life -= 1
    print(f"The letter you have chosed is not in the word. You losed a life. {life} life left.")
  print(f"{display}\n")
  print(stages[life])
if display == list(chosen_word):
  print("you won!!")

else: 
  print("You lose!!")



  