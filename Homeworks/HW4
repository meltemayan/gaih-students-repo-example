class Game():
    def __init__(self):      
      words = ['january', 'february', 'march', 'april', 
         'may', 'june', 'july', 'august', 
         'september', 'october', 'november', 'december']
      import random
      self.word = random.choice(words)

    #def showInfo(self):
        #print("{}".format(self.word))
    
    def lenghtofword(self):
        charnum = len(self.word)
        print("You word is {} characters.".format(charnum))
        #for i in range(charnum):
         # print("_"+ " ", end="")

    def guessthechar(self):
        guesslist = ''
        turns = 8
        while turns > 0:
          failed = 0
          for char in self.word: 
            if char in guesslist: 
              print(char + " ", end="")            
            else: 
              print("_"+ " ", end="")
              failed += 1
          print("\n")

          if failed == 0:
            print("You Won!") 
            print("The word is: ", self.word) 
            break
          guess = input("Guess a character:").lower()
          if len(guess) == 1 and guess != " ":
            guesslist += guess 

            if guess not in self.word:
              turns -= 1
              print("Wrong")
            print("You have", + turns, 'more guesses')
            if turns == 0:
              print("You Loose")
          else:
            print("You entered wrong input!")

print("Welcome to HANGMAN! Your word will be a month. Good Luck!")        
word=Game()
#word.showInfo()
word.lenghtofword()
print("Guess the characters")
word.guessthechar()
