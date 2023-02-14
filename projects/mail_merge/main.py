with open("Input/Letters/starting_letter.txt", "r") as template:
    template_text = template.read()

with open("Input/Names/invited_names.txt", "r") as names:
    invited_names = names.read().split()
    for name in invited_names:
        with open(f"Output/ReadyToSend/letter_for_{name}", "w") as output:
            new_letter = template_text.replace("[name]", name)
            output.write(new_letter)
