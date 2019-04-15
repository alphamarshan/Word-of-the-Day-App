# Import libraries
import requests
import random
import json

# Initiate the input which will be used as the Word of the Day
user_input = input("Enter a word for the dictionary to define: ")

# Open and read the list of English words
words_file = open("words.txt", "r")
all_words = words_file.read()
words_file.close()

# Variables
app_id = "2f5596aa"
app_key = "cb0e7fe2e343054d8bd14743f44f5b6c"
language = "en"
region = "us"
word_id = str(user_input)

# Create a URL with API keys to access the Oxford Dictionary API
base_url = "https://od-api.oxforddictionaries.com:443/api/v1" 
appended_url = "/entries/" + language + "/" + word_id.lower() + "/regions=" + region
requested_url = base_url + appended_url

# Create the GET request for the API
r = requests.get(requested_url, headers = {"app_id": app_id, "app_key" : app_key})

# Status code handling
if r.status_code == 200:
    print("\nHTTP Status Code: 200 \nSuccess!\n")
else:
    print("Error! Something went wrong.")

# Handle/parse the JSON that returns
parsed_text = json.loads(r.text)
# print(json.dumps(parsed_text, indent=2, sort_keys=True))

results_id = parsed_text["results"][0]["id"].capitalize()
results_definition = parsed_text["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]

print(f"The word of the day is: {results_id}, which means: {results_definition}")