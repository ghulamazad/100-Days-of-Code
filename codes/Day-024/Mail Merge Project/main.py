NAME_PLACEHOLDER = "[name]"

with open('./Input/Names/invited_names.txt') as invited_name_file:
    names = invited_name_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        name = name.strip()
        new_letter = letter_contents.replace(NAME_PLACEHOLDER, name)
        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as completed_letter:
            completed_letter.write(new_letter)
