import csv
import random
import os.path
from itertools import permutations

SCRABBLE_DISTRIBUTION = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
    'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6,
    'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}

# Function to load the dictionary
def load_dictionary(csv_file):
    print(f"Loading dictionary from file: {csv_file}")
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"The dictionary file '{csv_file}' does not exist.")

    dictionary = set()
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dictionary.add(row['Word'].lower())
    print("Dictionary loaded successfully.")
    return dictionary

# Function to find anagrams of a word in the dictionary
def find_anagrams(word, dictionary):
    word = word.lower()
    anagrams = ["".join(perm) for perm in permutations(word) if "".join(perm) in dictionary and "".join(perm) != word]
    return anagrams

# Function to get 7 random letters from the Scrabble bag
def get_random_letters():
    bag = []
    for letter, count in SCRABBLE_DISTRIBUTION.items():
        bag.extend([letter] * count)

    random_letters = random.sample(bag, 7)

    # Remove selected letters from the bag
    for letter in random_letters:
        bag.remove(letter)

    return random_letters

# Function to calculate Scrabble score for a word
def calculate_scrabble_score(word):
    SCRABBLE_LETTER_SCORES = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
        'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
        'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }

    word = word.upper()
    score = sum(SCRABBLE_LETTER_SCORES.get(letter, 0) for letter in word)
    return score

# Function to find valid words from 7 random letters and their scores
def find_valid_words(random_letters, dictionary):
    valid_words = []

    for r in range(1, len(random_letters) + 1):
        for combination in permutations(random_letters, r):
            word = ''.join(combination).upper()
            if word in dictionary:
                score = calculate_scrabble_score(word)
                valid_words.append((word, score))

    valid_words.sort(key=lambda x: x[1], reverse=True)
    return valid_words

# Function to draw tiles from the scrabble bag
def draw_tiles(scrabble_bag):
    if len(scrabble_bag) >= 7:
        tiles = random.sample(scrabble_bag, 7)
    else:
        tiles = scrabble_bag
    for tile in tiles:
        scrabble_bag.remove(tile)
    return tiles

# Function 5: Play Scrabble game
def play_scrabble_game():
    csv_file = 'OPTED-Dictionary.csv'

    try:
        dictionary = load_dictionary(csv_file)
    except FileNotFoundError as e:
        print(e)
        return

    # Initialize players' scores and the Scrabble bag
    player_scores = [0, 0]
    scrabble_bag = []

    # Draw initial tiles for each player
    for letter, count in SCRABBLE_DISTRIBUTION.items():
        scrabble_bag.extend([letter] * count)
    random.shuffle(scrabble_bag)

    player_tiles = [[], []]
    for player in range(2):
        player_tiles[player] = get_random_letters()

    # Start the game
    player_index = 0
    while scrabble_bag and (len(scrabble_bag) >= 7 or any(find_valid_words(player_tiles[i], dictionary) for i in range(2))):
        current_player = player_index % 2

        print(f"\nPlayer {current_player + 1}'s Turn:")

        # Display player's current tiles
        print("Player's tiles:", player_tiles[current_player])

        # Player inputs word
        word_input = input("Enter your word (or press Enter to skip): ")

        # Check if the player wants to quit
        if word_input.lower() == "quit":
            print("Exiting the game.")
            break

        # Check if the input word is valid
        if word_input and word_input.upper() in dictionary:
            word_score = calculate_scrabble_score(word_input)
            print(f"Player {current_player + 1}, played word: {word_input}, word score: {word_score}")
            player_scores[current_player] += word_score
            player_tiles[current_player] = [tile for tile in player_tiles[current_player] if tile not in word_input]
            print(f"Cumulative score for Player {current_player + 1}: {player_scores[current_player]}")
        else:
            print("Invalid word! Please enter a valid word or press Enter to skip.")

        # Draw new tiles for the player
        if len(scrabble_bag) >= 7:
            player_tiles[current_player] = get_random_letters()
        elif scrabble_bag:
            player_tiles[current_player] += random.sample(scrabble_bag, min(7 - len(player_tiles[current_player]), len(scrabble_bag)))
            scrabble_bag = [tile for tile in scrabble_bag if tile not in player_tiles[current_player]]

        # Switch to the next player
        player_index += 1

    # Game Over
    print("\nGame Over!")
    print("Final Scores:")
    for player in range(2):
        print(f"Player {player + 1}: {player_scores[player]}")



# Main function to start the game
def main():
    while True:
        print("\n1. Find Anagrams of a Word")
        print("2. Get Random Letters")
        print("3. Calculate Scrabble Score for a Word")
        print("4. Find Valid Words from Random Letters")
        print("5. Play Scrabble Game")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            word = input("Enter a word: ")
            dictionary = load_dictionary('OPTED-Dictionary.csv')
            print(f"Anagrams of {word}: {find_anagrams(word, dictionary)}")
        elif choice == '2':
            print(f"Random Letters: {get_random_letters()}")
        elif choice == '3':
            word = input("Enter a word: ")
            print(f"Scrabble score for {word}: {calculate_scrabble_score(word)}")
        elif choice == '4':
            dictionary = load_dictionary('OPTED-Dictionary.csv')
            random_letters = get_random_letters()
            print("Random Letters:", random_letters)
            valid_words = find_valid_words(random_letters, dictionary)
            print("Valid words from random letters:")
            for word, score in valid_words:
                print(f"{word}: {score}")
        elif choice == '5':
            play_scrabble_game()  # Remove the argument here
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
