with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_fileL:
    letter = letter_fileL.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace("[name]", stripped_name).replace("Angela", "Neeraj")
        with open(f'./Output/ReadyToSend/letter_for{stripped_name}.txt', "w") as new_file:
            new_file.write(new_letter)

        print('Done')
