

import cheater

import random

def fetch_word():
    # will fetch a random word from valid-wordle-words.txt
    dict = cheater.make_dict()
    word = random.choice(dict)
    #print(word)
    return word


def check_win(secret_word, guess_word):
    if secret_word == guess_word:
        return True
    else:
        return False
    
zip('hello', 'hello')




def play_game(word):
    count = 0


    while count < 7:
        guess_word = input(f"Guess # {count + 1} : ")


        # turn guess word into a list of chars
        guess_word_list = []
        for char in guess_word:
            guess_word_list.append(char)

        secret_word_list = []
        for char in word:
            secret_word_list.append(char)

        res_to_print = guess_word_list.copy()
        
        for i in range(len(secret_word_list)):
            if guess_word_list[i] == secret_word_list[i]:
                res_to_print[i] = f"**{guess_word_list[i]}**"
            if guess_word_list[i] in secret_word_list and guess_word_list[i] != secret_word_list[i]:
                res_to_print[i] = f"*{guess_word_list[i]}*"
        
        print(res_to_print)

        if check_win(word, guess_word):
            print("WIN")
            exit()





        count += 1

#word = fetch_word()
#play_game(word)