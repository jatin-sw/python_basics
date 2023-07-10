import pandas

nato_phonetic_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dictionary = {row.letter:row.code for (index, row) in nato_phonetic_dataframe.iterrows()}

user_name = input("Enter your name: ")

nato_phonetic_namelist = [nato_phonetic_dictionary.get(character) for character in user_name.upper()]

print(nato_phonetic_namelist)