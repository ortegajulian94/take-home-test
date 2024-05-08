# Take-Home Test Challenge

## Introduction
-This repository contains my solution to a take home test with challenges to solve. 

### Usage
- Challenges are listed in order to ideally allow them to be built on each other as you progress.


## Technologies Used
- Python, Regular Expressions (regex), File I/O, Collections module, Command-line interface (CLI), API's, Version Control, Containerization, AWS, Libraries and Modules,


## Testing
- Include some tests, so we can see how you approach testing. With respect to programming languages, use either golang, python and/or javascript with a preference for python. Some of the samples have been setup with python.

## Challenges
bible-challenge

1)
Write a function that prints out the top 20 words used (frequency) in the Bible and the number of times they are used.

2)
Write a function that takes a word (or phrase) as input and prints out the verses where that word is used in the Bible.

3)
Write a function that prints the top 5 longest words in the KJV Bible

3)
Write a function that takes a word or phrase as input and prints out the number of times it's used in the Bible.

4)
Sign up for Google Translate (free to sign up no cc required) via rapidapi and create a function that will take a random verse from the Bible and translate it to Chinese and print it.
https://rapidapi.com/googlecloud/api/google-translate1

5)
Sign up for PK AI (free to sign up no cc required) via rapid AI and create a function that will take one of the top longest words in the Bible (using function #3) and print out the definition and synonyms
https://rapidapi.com/pk-ai-pk-ai-default/api/words-definitions-dictionary-and-data-api

6)
Sign up for Cohere (free no cc required).  Create a function that will take an entire chapter from a book in the Bible and summarize it with Cohere's summarize API endpoint.
https://docs.cohere.com/reference/summarize-2

7) 
Sign up for VoiceRSS (free no cc required).  Create a function that will take a random verse from the Bible and convert it to speech and download the mp3 file locally for the user.
https://www.voicerss.org/
https://rapidapi.com/voicerss/api/text-to-speech-1/

jokes-as-a-service

1)
We have a group of dads in our congregation that are in dire need of some fresh dad and Chuck Norris jokes. Write a function that returns a random dad joke and a random Chuck Norris joke via these free APIs:
https://publicapis.io/chucknorris-io-api
https://icanhazdadjoke.com/api

scrabble-challeenge

1)
Write a function that takes a word and returns all of its anagrams in the given dictionary.  For example input of eat would return tea, ate, etc.

2)
Write a function that returns a list of 7 random letters from a collection of Scrabble letters from a bag of 98 tiles (lets skip the blanks for now)
and reduces the bag of letters by those 7 letters.  Use the standard Scrabble tile distribution.

3)
Write a function that returns the Scrabble score for a word.

4)
Write a function that takes a list of 7 random letters and returns all the valid words in the dictionary that can be made from those letters as well as their Scrabble scores.  Ensure the returned set of words are sorted from highest to lowest score.  Of course, it may not be possible to use all 7 letters for a word, it may only be a subset when printing out candidates.

5)
Assume we're playing Scrabble but without the board.  Create a function that has 2 players draw 7 tiles each initially (follow standard Scrabble drawing rules).
Have each player find the optimal (highest) scoring word and these players take turns playing by putting the word down (print it such as: Player: 1, word: soda, word score: 5 points, cumulative score: X points, etc.  When they draw a new tile, they can only draw up to a maximum of 7 to replace the tiles they played.  The game ends when the bag is empty and/or there are no more words to play.

