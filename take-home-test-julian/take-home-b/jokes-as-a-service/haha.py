# 1
# We have a group of dads in our congregation that are in dire need of some fresh dad and Chuck Norris jokes. Write a function that returns a random dad joke and a random Chuck Norris joke via these free APIs:
# https://publicapis.io/chucknorris-io-api
# https://icanhazdadjoke.com/api
import requests

def get_random_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    joke_data = response.json()
    return joke_data['joke']

def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    joke_data = response.json()
    return joke_data['value']

def get_random_jokes():
    dad_joke = get_random_dad_joke()
    chuck_joke = get_random_chuck_norris_joke()
    return dad_joke, chuck_joke

# Example usage
dad_joke, chuck_joke = get_random_jokes()
print("Random Dad Joke:", dad_joke)
print("Random Chuck Norris Joke:", chuck_joke)
