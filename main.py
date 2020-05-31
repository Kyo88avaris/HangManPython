import random
import string


hangman_pic = ["""
+___+
    |
    |
    |
===== """ , """
+___+
  O |
    |
    |
===== """ , """
+___+
  O |
  | |
    |
===== """ , """
+___+
  O |
 /| |
    |
===== """ , """
+___+
  O |
 /|\|
    |
===== """ , """
+___+
  O |
 /|\|
 /  |
===== """ , """
+___+
  O |
 /|\|
 / \|
===== """]

words = { "animal": ['alligator', 'ant', 'bear', 'bee', 'bird', 'camel', 'cat', 'cheetah', 'chicken', 'chimpanzee', 'cow', 'crocodile', 'deer', 'dog', 'dolphin', 'duck', 'eagle', 'elephant',\
                     'fish', 'fly', 'fox', 'frog', 'giraffe', 'goat', 'goldfish', 'hamster', 'hippopotamus', 'horse', 'kangaroo', 'kitten', 'lion', 'lobster', 'monkey', 'octopus', 'owl', 'panda',\
                     'pig', 'puppy', 'rabbit', 'rat', 'scorpion', 'eal', 'shark', 'sheep', 'snail', 'snake', 'spider', 'squirrel', 'tiger', 'turtle', 'wolf', 'zebra'],\
          "fruit": ['apple', 'apricot', 'banana', 'blackberry', 'blueberry', 'cherry', 'cranberry', 'currant', 'fig', 'grape', 'grapefruit', 'grapes', 'kiwi', 'kumquat', 'lemon', 'lime', 'melon', 'nectarine',\
                    'orange', 'peach', 'pear', 'persimmon', 'pineapple', 'plum', 'pomegranate', 'prune', 'raspberry', 'strawberry', 'tangerine', 'watermelon'],\
          "vegetable": ['asparagus', 'beans', 'beet', 'broccoli', 'brussels sprouts', 'cabbage', 'carrot', 'cauliflower', 'celery', 'corn', 'cucumber', 'eggplant',\
                        'green pepper', 'kale', 'lettuce', 'okra', 'onion', 'peas', 'potato', 'pumpkin', 'radish', 'spinach', 'tomato'] }

alpha = list(string.ascii_lowercase)

def select_category():
    category = []
    for x in words:
        category.append(x)

    topic = random.choice(category)

    return topic


def select_word(c):

    word_list = words[c]

    word_len = len(word_list)
    choice = random.randint(0 , word_len-1)

    secret_word = word_list[choice]

    return secret_word


def dsp_word(secret_word, correct_letters):
    dsp_word = []

    for char in secret_word:
        if char in alpha:
            dsp_word.append("_")
        else:
            dsp_word.append(" ")

    for ind, letr in enumerate(dsp_word):
        if secret_word[ind] in correct_letters:
            dsp_word[ind] = secret_word[ind]

    return("".join(dsp_word))

def play_again():
    answer = input("Do you want to play again? y/n")
    val = False

    while not val:
        answer = answer[0]

        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            answer = input("You have inputted an invalid response.  Please use Y / N")


def main():
    print("H A N G M A N:  G A M E")
    print("Starting Game")
    missed_letters = []
    correct_letters = []
    unique_char = set()
    num_of_wrong = 0
    end_game = False
    num_of_guess = 0
    game_done = False

    hint = select_category()
    sw = select_word(hint)

    for char in sw:
        unique_char.add(char)

    unique_char = list(unique_char)

    ##print(sw)

    while not end_game:
        print(hangman_pic[num_of_wrong])
        print("Topic is: {}".format(hint))
        if num_of_guess != 0:
            print("Missed Letters: ", end= " ")
            for char in missed_letters:
                print(char, end = " ")
            print("\nCorrect Letters: ", end=" ")
            for char in correct_letters:
                print(char, end = " ")
        word = dsp_word(sw, correct_letters)
        print()

        for char in word:
            print(char + " ", end = "")

        if len(unique_char) == len(correct_letters):
            print("\nCongrats~! You have found the secret word.")
            game_done = True


        if num_of_wrong == 6:
            print("\nGAME OVER")
            print("Secret World was {}".format(sw))
            game_done = True

        if not game_done:
            input_val = False
            while not input_val:
                guess = input("\n\nPlease enter your guess letter: ")
                guess = guess.lower()
                if len(guess) != 1:
                    print("Please Only type in 1 letter.")
                elif guess not in alpha:
                    print("You have inputted invalid character.")
                elif guess in correct_letters:
                    print("You have already guessed this letter.")
                elif guess in missed_letters:
                    print("You have already guessed this letter.")
                else:
                    input_val = True

            found = False
            for i, char in enumerate(sw):
                if sw[i] in guess:
                    found = True
                    break

            if found:
                correct_letters.append(guess)
                print("{} is in the secret word.".format(guess))
                num_of_guess += 1
            else:
                missed_letters.append(guess)
                num_of_wrong += 1
                num_of_guess += 1
                print("{} is not in the secret word.".format(guess))
        else:
            if play_again():
                missed_letters = []
                correct_letters = []
                num_of_wrong = 0
                end_game = False
                num_of_guess = 0
                unique_char = set()
                game_done = False

                hint = select_category()
                sw = select_word(hint)

                for char in sw:
                    unique_char.add(char)

                unique_char = list(unique_char)

                print("\nN E W  H A N G M A N    G A M E")
            else:
                break






















if __name__ == "__main__":
    main()
