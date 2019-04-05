# Import libraries
import requests
import random
import json

user_input = input("Enter a word for the dictionary to define: ")

words_file = open("words.txt", "r")
all_words = words_file.read()
words_file.close()

app_id = "2f5596aa"
app_key = "cb0e7fe2e343054d8bd14743f44f5b6c"
language = "en"
region = "us"
word_id = str(user_input)

base_url = "https://od-api.oxforddictionaries.com:443/api/v1" 
appended_url = "/entries/" + language + "/" + word_id.lower() + "/regions=" + region
requested_url = base_url + appended_url

r = requests.get(requested_url, headers = {"app_id": app_id, "app_key" : app_key})

if r.status_code == 200:
    print("\nHTTP Status Code: 200 \nSuccess!\n")
else:
    print("Error")

parsed_text = json.loads(r.text)
# json.dumps(json.loads(r.text), sort_keys=True, indent=2)
print(parsed_text)
print(parsed_text["metadata"]["provider"])