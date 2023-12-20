import sys
import time
import openai

openai.api_key = "YOUR API KEY"


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


name = typingInput("What's your Name?")
animal = typingInput("What's your favorite animal?")
food = typingInput("What's your favorite food?")
hobby = typingInput("Do you have a hobby/what do you like to do in your free time?")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Write a 5 sentence silly story about a " + animal + " named " + name + " who eats " + food + " and " + hobby + ".",
    temperature=0.7, # makes the answers less random as the number goes higher
    max_tokens=512,  # could add more if cutting off
    top_p=1,
    frequency_penalty=0,  # decreases the likelihood to say the same thing verbatim
    presence_penalty=0  # makes model talk about new topics
)

typingPrint(response["choices"][0]["text"] + "\n")
