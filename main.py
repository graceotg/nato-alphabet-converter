import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in data.iterrows()}


user_input = input("Type in your word: ").upper()

is_it_alphabet = False

while not is_it_alphabet:
    try:
        user_input_list = [dict[letter] for letter in user_input]
        is_it_alphabet = True


    except KeyError:
        print("Sorry, only letters in the alphabet please")
        user_input = input("Type in your word: ").upper()

    else:
        print(user_input_list)




