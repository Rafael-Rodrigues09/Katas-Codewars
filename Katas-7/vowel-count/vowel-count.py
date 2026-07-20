def get_count(sentence):
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for letter in sentence:
            if letter in vowels:
                vowels[letter] += 1
        return sum(vowels.values())

# Take a try!
sentence = input('Type a sentence: ')
print(f'Vowels in sentence {sentence}: {get_count(sentence)}')