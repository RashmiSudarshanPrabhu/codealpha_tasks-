import random
wordslist=[
    "apple",
    "bat",
    "cat",
    "dog",
    "elephant",
    "fig",
    "ginger",
    "hangman",
    "inova",
    "jackfruit",
    "kitkat",
    "laddu",
    "monkey",
    "newzeland",
    "oman",
    "peacock",
    "queen",
    "rashmi",
    "shriansh",
    "twinkle",
    "ukraine",
    "van",
    "window",
    "xtream",
    "yak",
    "Zoom"

]



def  get_word():
    word=random.choice(wordslist)
    return word.upper()

def start(word):
    completion="_" * len(word)
    guessed=False
    choosen_letters=[]
    choosen_words=[]
    life=6
    print("Start the game")
    print(display(life))
    print(completion)

    while not guessed and life>0:
        guess=input("\n Guess the letter: ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in choosen_letters:
                print("\n already choosen choose another letter",guess)
            elif guess not in word:
                life-=1
                choosen_letters.append(guess)
            else:
                print("Congrats",guess,"is present in word")
                choosen_letters.append(guess)
                lists=list(completion)
                positions=[i for i,letter in enumerate(word) if letter==guess]
                for position in positions:
                    lists[position]=guess
                completion="".join(lists)
                if "_" not in completion:
                    guessed=True
        elif len(guess)==len(word) and guess.isalpha():
            if guess in choosen_words:
                print("Already guessed")
            elif guess!=word:
                print("not in word")
                life-=1
                choosen_words.append(guess)
            else:
                guessed=True
                completion=word
        else:
            print("Inncorrect guess try again")
        print(display(life))
        print(completion)
    if guessed:
        print("win")
    else:
        print("Sorry try again")
def main():
    word=get_word()
    start(word)
    while input("Play again?(Y/N)").upper()=="Y":
        word=get_word()
        start(word)
def display(life):
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
    return stages[life]

if __name__ =="__main__":
    main()

            
