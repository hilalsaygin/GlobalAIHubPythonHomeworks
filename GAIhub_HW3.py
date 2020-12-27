import random
def Hangman_Visual(turn):           #prints the visual state of the hangman. at index 6 initial state
    stages=["""
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \   """,   #both legs
            """                      
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /      """,  #leg
            """                      
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |           """,  # both arms
            """                    
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |          """,  #arm
            """                     
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |         """,   #body2
            """                     
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |         """,    #body1
            """                     
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |         """ ,  #head
           """                        
                    --------
                   |      |
                   |
                   |
                   |
                   |            """   #initial
            ]
    return stages[turn]

file_lines= open('hangman_words.txt','r').readlines()
num_lines = sum(1 for line in file_lines)

choice,score=1,0
user = input(" >>>>  Hello, Enter your name to play :)  <<<< ")

while choice==1 :
    if user.isalpha():
        print(" WELCOME {} , Let's play Hangman :)) ".format(user))
        turns = 7                                                   #num of lives that player
        rand_index=random.randint(0,num_lines)
        game_word=file_lines[rand_index].strip('\n').upper()
        gameword_list=list('*'*len(game_word))
        guessedLett_list = []
        print('\n', '-'*18,"GAME STARTING",'-'*18 )
        print(Hangman_Visual(turns))

        while turns >0:
            print('\n',"*"*50)
            guess_lett = input("Guess a letter : ").upper()
            if len(guess_lett) == 1 and guess_lett not in guessedLett_list and guess_lett.isalpha() :
                guessedLett_list.append(guess_lett)
                if guess_lett in game_word :
                    for lett in range(len(game_word)):
                        if guess_lett == game_word[lett]:
                            gameword_list[lett] = guess_lett
                    print("Nice Guess :D \n")

                else:
                    turns-=1
                    print("Opps :O Your guess not in the word !!         Reamining  <<< {} >>> ".format(turns))
                    print(Hangman_Visual(turns))

                print("Your Progress : "," ".join(gameword_list))
                print("The letters you guessed so far {}".format(guessedLett_list))


            elif guess_lett == game_word:   #if user enter the game word, the game has won.
                print("Congratulations !! You saved a man's life :D  *** ^-^ ***")
                gameword_list = list(guess_lett)
                score+=1
                print("Your word:  {} \nYour total score {}".format("".join(gameword_list),score))
                break

            else:
                if len(guess_lett) != 1:
                    print("Please enter only 1 character at each time !! ")
                elif not guess_lett.isalpha():  # if user didn't enter one letter at each time ask again to guess letter
                    print("You must enter a character not a number. It's a word guessing game :D ")

                elif guess_lett in guessedLett_list:
                    turns -= 1
                    print("You already tried letter {} !!!           Reamining  <<< {} >>>".format(guess_lett,turns))
                    print(Hangman_Visual(turns))

        if turns !=0:
            choice = int(input("Do you want to play again ? If yes hit 1 otherwise 0 "))
            if choice == 1:
                turns = 7
                continue
            else:
                break

        score-=1
        print("OPPS !! You just hanged a man :((      Word was >>> {} \n".format(game_word))
        print("Your total score >>>>>>>",score)
        choice=int(input("Do you want to plat again ? If yes hit 1 otherwise 0 "))

    else:
        print("You must enter a valid name to play Sorry :(( Name should include letters not numbers!!")
        break









