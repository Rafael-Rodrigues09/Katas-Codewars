def alphabet_position(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    fixed_text = [letter.lower() for letter in text if letter.isalpha()]
    dict_alphabet = {letter: i for i, letter in enumerate(letters, start=1)}
    return ' '.join(([str(dict_alphabet[letter]) for letter in fixed_text]))

# Take a try!
text = input('Type a text: ')
print(alphabet_position(text))