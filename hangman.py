import random


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


tries = 7
cow = ""
hangman = 0
result = []
wordsUsed = []
word = "cow"
count = 0
word1 = ""
for i in word:
    result.append("_")

while tries > 1:
    choice = str(input("Enter a Letter: "))
    choice.lower()
    wordsUsed.append(choice)
    if choice not in word:
        tries -= 1
        hangman += 1
        print(str(tries) + " tries remaining")
    else:
        for i in word:
            count += 1
            if i == choice:
                result[count-1] = choice
    print(HANGMANPICS[hangman-1])
    print(result)
    for i in result:
     word1 += i

    if word1 == word:
      break 
    
            
    count = 0
    word1 = ""

print(word)
   

        

