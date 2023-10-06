from inputimeout import inputimeout
from random import *
from time import sleep
import json
name = input("what is your name: ")
x = 0
y = 0
z = 0
answer = 0
scores_dict = {}


def diff_(m):
    diff = 1
    if x > 4 and x < 8:
        diff = 2
    if x > 8 and x < 12:
        diff = 3
    if x > 12 and x < 16:
        diff = 4
    if x > 16 and x < 20:
        diff = 5
    if x > 20 and x < 24:
        diff = 6
def store_scores(scores_dict):
    try:
        with open("scores.json", "a") as scores:
            scores.write(json.dumps(scores_dict, indent = 4))
            scores.close()
    except:
        return

quest_list_1 = [
    ["What is the capital of France? ", "paris"],
    ["Which planet is known as the 'red planet'? ", "mars"],
    ["How many continents are there on Earth? ", "7"],
    ["What is the largest mammal in the world? ", "blue whale"],
    ["Who wrote the play 'Romeo and Juliet'? ", "william shakespeare"],
    ["What is the chemical symbol for water? ", "h2o"],
    ["What is the smallest prime number? ", "2"],
    ["What is the tallest mountain in the world? ", "mount everest"],
    ["What is the national flower of Japan? ", "cherry blossom"],
    ["Who painted the mona Lisa? ", "leonardo da Vinci"],
    ["What is the largest organ in the human body? ", "skin"],
    ["Which famous scientist is known for his theory of relativity? ", "albert einstein"],
    ["What is the capital of Japan? ", "tokyo"],
    ["What is the largest ocean in the world? ", "pacific ocean"],
    ["How many sides does a hexagon have? ", "6"],
    ["Who was the first President of the United States? ", "george washington"],
    ["What is the largest planet in our solar system? ", "jupiter"],
    ["Which animal is known as the 'King of the Jungle? ", "lion"],
    ["What is the smallest prime number greater than 10? ", "11"],
    ["What is the freezing point of water in degrees celsius? ", "0"],
    ["What is the largest species of shark? ", "whale shark"],
    ["What is the largest desert in the world? ", "sahara desert"],
    ["Which gas do plants give off during photosynthesis? ", "oxygen"],
    ["What is the smallest planet in our solar system? ", "mercury"],
    ["Which planet is known as the 'morning Star' or 'Evening Star'? ", "venus"],
    ["What is the national flower of the United States? ", "rose"],
    ["What is the largest species of penguin? ", "emperor penguin"],
    ["What is the most abundant gas in Earth's atmosphere? ", "nitrogen"],
    ["What is the national flower of canada? ", "maple leaf"],
    ["What is the largest species of bear? ", "polar bear"],
    ["Who is the author of 'Harry Potter' book series? ", "j.k. rowling"],
]

while x < 5:
    try:
        i = randrange(0,len(quest_list_1))
        j = quest_list_1[i]
    except:
        print(f"you answered {y} question correctly out of {z}")
        exit()
    try:
        sleep(1)
        answer = inputimeout(j[0], timeout=15)
        z += 1
        sleep(1)
        quest_list_1.remove(j)
    except:
        print("your time is over")
        print(f"the answer is {j[1]}")
        break
    if answer == "stop":
        print(f"you got {y} points")
        exit()   
    if answer == j[1]:
        print("correct")
        y += 1

    else:
        print("wrong")
        print(f"the correct answer is: {j[1]}")
        x += 1

user = {}
user["correct_cnt"] = y
user["quest_cnt"] = z
if scores_dict.get(name):
    if user["quest_cnt"] > scores_dict[name]["quest_cnt"]:
        print()
    else:
        scores_dict[name] = user
else:
    scores_dict[name] = user

print("the highest score is {?} out of {?}")
print(f"{name}. you answered {y} question correctly out of {z}")
store_scores(scores_dict)