import sys
import random

# local edit nov 24

def make_dict():
    # Open the text file for reading
    with open("wordle.txt", "r") as file:
        # Read the lines from the file and store them in a list
        word_list = file.read().splitlines()

    return word_list


def build_confirmed(confirmed_word):
    # making GREEN section
    confirmed = []
    for letter in confirmed_word:
        if letter == "_":
            confirmed.append(None)
        else:
            confirmed.append(letter)
    return confirmed


def build_letter_lists_and_contains_and_exlude(confirmed):
    contains = {}
    exclude = []
    letter_lists = [[] for _ in range(5)]

    for i in range(len(sys.argv) - 2):
        word = sys.argv[i + 2]
        if len(word) != 5:
            print(f"Invalid input. {word} is a SHIT word. Gotta be five letters.")
            sys.exit()

        word_list = list(word)
        for j in range(len(word_list)):
            if word[j] != '_':
                #add to exclude
                if word[j].islower():
                    if word[j] not in confirmed:
                        exclude.append(word[j])
                # ADD YELLOWS
                if word[j].isupper():
                    lowercase = word_list[j].lower()
                    if lowercase not in contains:
                        contains[lowercase] = []
                    contains[lowercase].append(j)
                    word_list[j] = lowercase

            letter_lists[j].append(word_list[j])

    return letter_lists, contains, exclude


def eliminate_words(word_list, contains, confirmed, letter_lists, exclude):
    possible_words = []

    for word in word_list:
        flag = True

        # contains logic
        contains_keys = contains.keys()
        contains_list = list(contains_keys)

        # contains = list(contains_keys)
        for i in range(len(contains_list)):
            if contains_list[i] not in word:
                flag = False

        for i in range(5):
            # eliminate if letter is excluded
            if word[i] in exclude:
                flag = False
            # eliminate b/c known letter is not matched
            if confirmed[i] and confirmed[i] != word[i]:
                flag = False
            if word[i] in letter_lists[i] and word[i] != confirmed[i]:
                flag = False
            # contains dict logic
            if word[i] in contains and i in contains[word[i]]:
                flag = False

        if flag:
            possible_words.append(word)
    return possible_words


def print_res(possible_words):
    if len(possible_words) > 30:
        print(f"{len(possible_words)} possibilities remain!")
    if len(possible_words) < 30:
        print(f"{len(possible_words)} possible words:\n")
        print(possible_words)


def stochastic_guess(possible_words, contains, confirmed, letter_lists, exclude):
    min_possibles = 999999

    if len(possible_words) > 500:
        n = random.randint(450, 499)
    else:
        n = len(possible_words)

    word_to_return = None

    for i in range(n):
        word = random.choice(possible_words) 
        #word = possible_words[i]

        # add word to contains & letter_lists
        for letter in word:
            if letter not in contains:
                contains[letter] = []
            contains[letter].append(word.index(letter))
            letter_lists[word.index(letter)].append(letter)

        possibles = eliminate_words(possible_words, contains, confirmed, letter_lists, exclude)

        if len(possibles) < min_possibles:
            word_to_return = word

        min_possibles = min(min_possibles, len(possibles))

    return word_to_return, min_possibles


def main():
    print("Cheating is wrong.")
    confirmed = build_confirmed(sys.argv[1])
    letter_lists, contains, exclude = build_letter_lists_and_contains_and_exlude(confirmed)

    word_list = make_dict()
    possible_words = eliminate_words(word_list, contains, confirmed, letter_lists, exclude)

    suggested_guess, num = stochastic_guess(
        possible_words, contains, confirmed, letter_lists, exclude
    )

    print_res(possible_words)
    print(f"Stochastic guess: {suggested_guess}")


# if __name__ == "__main__":
#     main()
