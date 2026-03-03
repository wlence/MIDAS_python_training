# Code that counts the frequency of each letter in a given string
def letter_frequency(text):
    frequency = {}
    for letter in text:
        if letter.isalpha():  # Check if the character is a letter
            letter = letter.lower()  # Convert to lowercase for case-insensitivity
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
    return frequency

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

frequency = letter_frequency(text)
for letter, count in frequency.items():
    print(f"{letter}: {count}")

