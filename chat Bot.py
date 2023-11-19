mport nltk
nltk.download('wordnet')

# Importing modules
import re
from nltk.corpus import wordnet

# Building a list of Keywords
list_words=['hello','timings','diet','food','equipments','machines','packages','fees','shop','activities']
list_syn={}
for word in list_words:
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            # Remove any special characters from synonym strings
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            synonyms.append(lem_name)
    list_syn[word]=set(synonyms)
print (list_syn)

# Building dictionary of Intents & Keywords
keywords = {}
keywords_dict = {}

for word in list_words:
    keywords[word] = []
    for synonym in list(list_syn[word]):
        keywords[word].append('.*\\b' + synonym + '\\b.*')

for intent, keys in keywords.items():
    keywords_dict[intent] = re.compile('|'.join(keys))

print(keywords_dict)

# Building a dictionary of responses
responses={
    'hello':'Hello! How can I help you?',
    'timings':'We are open from 6AM to 10PM, Monday to Saturday and 10AM to 5PM on Sundays',
    'fallback':'I dont quite understand. Could you repeat that?',
    'equipments' : 'We have a variety of equipments, including treadmills, weights, and more.',
    'machines' : 'We have a variety of equipments, including treadmills, weights, and more.',
    'diet' : 'Meal 1 (Breakfast): \n Whole eggs (3-4) Oatmeal (1 cup) Whole milk (1 cup) Banana (1) \n Meal 2 (Snack): \n Greek yogurt (1 cup) Almonds (handful) Meal 3 (Lunch): Brown rice or quinoa (1 cup).\n Our trainers can help you better to create a personalized diet chart based on your fitness goals.',
    'food' : 'Our trainers can help you create a personalized diet chart based on your fitness goals.',
    'activities': 'We offer a range of activities, including yoga, cardio, and strength training classes.',
    'packages' : 'We have different membership packages. You can check them on our website (www.fitverse.com) or visit us for details.',
    'shop' : 'In our shop, we offer supplements , shoes and jackets to support your fitness journey. Visit out website www.fiterseshop.com'
}

print("Welcome to Fitverse Gym. How may I help you?")
# While loop to run the chatbot indefinitely
while True:
    # Takes the user input and converts all characters to lowercase
    user_input = input().lower()
    # Defining the Chatbot's exit condition
    if user_input == 'quit':
        print("Thank you for visiting.")
        break

    matched_intent = None
    for intent, pattern in keywords_dict.items():
        # Using the regular expression search function to look for keywords in user input
        if re.search(pattern, user_input):
            # if a keyword matches, select the corresponding intent from the keywords_dict dictionary
            matched_intent = intent

    # Print the matched intent for debugging
   # print("Matched Intent:", matched_intent)

    # The fallback intent is selected by default
    key = 'fallback'
    if matched_intent in responses:
        # If a keyword matches, the fallback intent is replaced by the matched intent as the key for the responses dictionary
        key = matched_intent

    # The chatbot prints the response that matches the selected intent
    print(responses[key])

