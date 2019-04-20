# Import libraries
import requests
import random
import json

#Opens GRE word list and reads lines into a list
file = open("gre_wordlist.txt")
word_list = file.read().split()
file.close()

# Organizes the list and generates a random word from within the list
new_word_list = [x[:-1] for x in word_list]
del new_word_list[:10]
list_length = len(new_word_list)
word_id = random.randint(0, list_length)
word = new_word_list[word_id]

# API Variables
app_id = "2f5596aa"
app_key = "cb0e7fe2e343054d8bd14743f44f5b6c"
language = "en"
region = "us"

# Create a URL with API keys to access the Oxford Dictionary API
base_url = "https://od-api.oxforddictionaries.com:443/api/v1" 
appended_url = "/entries/" + language + "/" + word + "/regions=" + region
requested_url = base_url + appended_url

# Create the GET request for the API
r = requests.get(requested_url, headers={"app_id": app_id, "app_key": app_key})

# Status code handling
if r.status_code == 200:
    print("\nHTTP Status Code: 200 \nSuccess!\n\n")
else:
    print("Error! Something went wrong.")

# # Handle/parse the JSON that returns
parsed_text = json.loads(r.text)
# # print(json.dumps(parsed_text, indent=2, sort_keys=True))

results_id = parsed_text["results"][0]["id"].capitalize()
results_definition = parsed_text["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0].capitalize()
results_example = parsed_text["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["examples"][0]["text"]

print("#############################\n")
print(f"The word of the day is:\n\n{results_id}\n")
print(f"Definition: {results_definition}\n")
print(f"Example: {results_example}\n")
print("#############################")