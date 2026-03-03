
import random

names = ["alice", "bob", "charlie", "david", "eve"]

# Traditional way to capitalize names
capitalized_names = []
for name in names:
    capitalized_names.append(name.capitalize())

print(capitalized_names)

# Using list comprehension to capitalize names
capitalized_names = [name.capitalize() for name in names]
print(capitalized_names)

# Using list comprehension to filter names that start with 'a' and capitalize them
capitalized_a_names = [name.capitalize() for name in names if name.startswith('a')]
print(capitalized_a_names)

# Using list comprehension to create a list of name lengths
name_lengths = [len(name) for name in names]
print(name_lengths)

# Using list comprehension to create the combination of names with their lengths
name_length_pairs = [(name, len(name)) for name in names]
print(name_length_pairs)

name_lenght_pairs_list = [f"{name} {len(name)}" for name in names for length in [len(name)]]
print(name_lenght_pairs_list)

# Create a list of all 52 playable cards in a standard deck
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

cards = [f"{value} of {suit}" for suit in suits for value in values]
print(cards)
print(len(cards))

#Shuffle the cards using the random module
random.shuffle(cards)
print(cards)

# Deal 4 bridge hands of 13 cards each
hands = [cards[i:i+13] for i in range(0, 52, 13)]
for i, hand in enumerate(hands):
    print(f"Hand {i+1}: {hand}")    

