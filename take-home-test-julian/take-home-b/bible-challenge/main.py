import os
import requests
import re
import random
from collections import Counter

def text_to_speech(text, api_key, output_file):
    url = "https://api.voicerss.org/"
    params = {
        "key": api_key,
        "hl": "en-us",
        "src": text,
        "c": "MP3",
        "f": "48khz_16bit_stereo"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        with open(output_file, "wb") as file:
            file.write(response.content)
        print("Speech saved as:", output_file)
    else:
        print("Error:", response.text)

def random_verse_from_bible(filename):
    with open(filename, "r", encoding="utf-8") as file:
        verses = file.readlines()
    return random.choice(verses).strip()

# Function to print the top 20 words used in the Bible and their frequencies
def get_top_words(filename, top_n=20):
    word_counts = Counter()

    with open(filename, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())  # Extract words from the line
            word_counts.update(words)  # Update word counts

    # Print the top N words
    print("Top", top_n, "words used in the Bible and their frequencies:")
    for word, count in word_counts.most_common(top_n):
        print(word, ":", count)

# Function to find and print verses where a word is used in the Bible
def find_word_in_bible(filename, word):
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Check if line is not empty
                parts = line.strip().split('\t', 1)
                if len(parts) == 2:
                    verse, scripture = parts
                    print("Processing verse:", verse)  # Debugging statement
                    # Check if the word or phrase is in the verse (case insensitive)
                    if re.search(r'\b{}\b'.format(re.escape(word.lower())), verse.lower()):
                        print(verse)
                        print(scripture)

# Function to print the top 5 longest words in the KJV Bible
def top_longest_words(filename, top_n=5):
    word_lengths = Counter()

    with open(filename, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())  # Extract words from the line
            for word in words:
                word_lengths[word] = len(word)  # Update word lengths

    # Get the top N longest words
    top_longest = word_lengths.most_common(top_n)
    print("Top", top_n, "longest words used in the Bible:")
    for word, length in top_longest:
        print(word, ":", length, "characters")
    
    # Return the top longest words
    return [word for word, _ in top_longest]

# Function to count and print the number of times a word is used in the Bible
def count_word_occurrences(filename, word):
    word_count = 0
    with open(filename, 'r') as file:
        text = file.read().lower()
        # Count the occurrences of the word or phrase (case insensitive)
        word_count = len(re.findall(r'\b{}\b'.format(re.escape(word.lower())), text))
    
    print(f"The word or phrase '{word}' appears {word_count} times in the Bible.")

# Function to get the definition and synonyms of a word from PK AI API
def get_word_info(word, api_key):
    url = "https://words-definitions.p.rapidapi.com/words"
    params = {"word": word}
    headers = {
        "X-RapidAPI-Host": "words-definitions.p.rapidapi.com",
        "X-RapidAPI-Key": api_key
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["definitions"]:
            definition = data["definitions"][0]["definition"]
            synonyms = data["definitions"][0]["synonyms"]
            return definition, synonyms
        else:
            return "No definition found", []
    else:
        return "Error", []

# Function to translate a random verse to Chinese
def translate_random_verse_to_chinese(filename, api_key):
    # Load Bible verses from a file
    with open(filename, "r", encoding="utf-8") as file:
        verses = file.readlines()

    # Select a random verse
    random_verse = random.choice(verses).strip()

    # Translate the verse to Chinese
    translated_verse = translate_to_chinese(random_verse, api_key)
    
    if translated_verse:
        print("Original verse (English):", random_verse)
        print("Translated verse (Chinese):", translated_verse)

# Function to translate a text to Chinese using Google Translate API
def translate_to_chinese(text, api_key):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = {
        "q": text,
        "source": "en",
        "target": "zh-CN"
    }
    headers = {
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
        "X-RapidAPI-Key": api_key,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        translated_text = response.json()["data"]["translations"][0]["translatedText"]
        return translated_text
    else:
        print("Error:", response.text)
        return None

# Function to summarize a chapter using Cohere API
def summarize_chapter(chapter_text, api_key):
    # Make a request to Cohere API to summarize the text
    url = "https://api.cohere.ai/v1/summarize"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": chapter_text
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        summarized_text = response.json()["summary"]
        return summarized_text
    else:
        print("Error:", response.text)
        return None
    

if __name__ == "__main__":
    current_directory = os.path.dirname(__file__)
    filename = os.path.join(current_directory, 'kjv.txt')

    # Translate a random verse to Chinese
    api_key_translate = "fc6aeea711msh2243c0ef1dfd940p183587jsnbdb72816a723"#Enter your API key
    translate_random_verse_to_chinese(filename, api_key_translate)

    # Get top longest words in the Bible
    top_longest = top_longest_words(filename)
    
    # Select one of the top longest words
    word_to_query = random.choice(top_longest)

    # Get word information from PK AI API
    api_key_pk_ai = "fc6aeea711msh2243c0ef1dfd940p183587jsnbdb72816a723"#Enter your API KEY
    definition, synonyms = get_word_info(word_to_query, api_key_pk_ai)

    # Print the definition and synonyms
    print("Definition:", definition)
    print("Synonyms:", ", ".join(synonyms) if synonyms else "No synonyms found")

    # Define the text of the Bible chapter to summarize
    chapter_text = """
        In the beginning God created the heaven and the earth.
        And the earth was without form, and void; and darkness was upon the face of the deep. 
        And the Spirit of God moved upon the face of the waters.
        And God said, Let there be light: and there was light.
        And God saw the light, that it was good: and God divided the light from the darkness.
        And God called the light Day, and the darkness he called Night. 
        And the evening and the morning were the first day.
    """    
    # Define your ChatAPI key
    api_key_cohere = "utQekFKnRiGF072j19uIqBAVSCZS70jt09UbVuLz"

    # Summarize the chapter
    summarized_text = summarize_chapter(chapter_text, api_key_cohere)
    if summarized_text:
        print("Summarized text:")
        print(summarized_text)

    get_top_words(filename)
    top_longest_words(filename)

    word_to_find = input("Enter the word or phrase to search for: ")
    find_word_in_bible(filename, word_to_find)
    
    word_to_count = input("Enter the word or phrase to count occurrences for: ")
    count_word_occurrences(filename, word_to_count)

    # Convert a random verse to speech and save it as an MP3 file
    api_key_voicerss = "181c8a50bc34496da1169920b59be0fb"
    output_file = "random_verse.mp3"
    random_verse = random_verse_from_bible(filename)
    text_to_speech(random_verse, api_key_voicerss, output_file)

