
def add_word_phrase():
    user_input = "yes"

    while user_input == "yes":
        user_new_element = input("New phrase or word: ").lower()

        data_base = open("data_base.txt", "a")
        data_base.write(user_new_element + "\n")
        data_base.close()

        user_input = input("Do you want to add another word/phrase (yes/no): ")


def see_all_words_phrases():
    data_base = open("data_base.txt", "r")
    for line in data_base:
        print(line.strip())


def menu_add_words_phrases():
    print("""
ADD WORDS AND PHRASES
1. Add phrase or word
2. See all phrases and words
""")

    user_input = input("Number: ")
    if user_input == "1":
        add_word_phrase()
    elif user_input == "2":
        see_all_words_phrases()
    else:
        print("Wrong input")


def main():
    print("""
MENU
1. Play Game
2. Add words and phrases
    """)

    user_input = input("Number: ")
    if user_input == "1":
        print("WIP")
    elif user_input == "2":
        menu_add_words_phrases()
    else:
        print("Incorrect input")

main()