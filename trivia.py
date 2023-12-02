from inputimeout import inputimeout
from random import *
from time import sleep
import json
name = input("what is your name: ")
time = 15
x = 0
boom = 0
y = 0
z = 0
answer = 0
scores_dict = {}
filename = "scores.json"


def store_scores(scores_dict):
    try:
        with open(filename, "a") as scores:
            scores.write(json.dumps(scores_dict, indent = 4))
            scores.close()
    except:
        return
    
def load_scores(filename):
    try:
        with open(filename, "r") as scores:
            json_str = scores.read()
            scores_dict = json.loads(json_str)
            scores.close()
            return scores_dict
    except:
        return {}

quest_list_1 = [
    ["What is the capital of france? ", "paris"],
    ["Which planet is known as the 'red planet'? ", "mars"],
    ["how many continents are there on earth? ", "7"],
    ["What is the largest mammal in the world? ", "blue whale"],
    ["Who wrote the play 'Romeo and juliet'? ", "william shakespeare"],
    ["What is the chemical symbol for water? ", "h2o"],
    ["What is the smallest prime number? ", "2"],
    ["What is the tallest mountain in the world? ", "mount everest"],
    ["What is the national flower of japan? ", "cherry blossom"],
    ["Who painted the mona lisa? ", "leonardo da Vinci"],
    ["What is the largest organ in the human body? ", "skin"],
    ["Which famous scientist is known for his theory of relativity? ", "albert einstein"],
    ["What is the capital of japan? ", "tokyo"],
    ["What is the largest ocean in the world? ", "pacific ocean"],
    ["how many sides does a hexagon have? ", "6"],
    ["Who was the first president of the United States? ", "george washington"],
    ["What is the largest planet in our solar system? ", "jupiter"],
    ["Which animal is known as the 'king of the jungle? ", "lion"],
    ["What is the smallest prime number greater than 10? ", "11"],
    ["What is the freezing point of water in degrees celsius? ", "0"],
    ["What is the largest species of shark? ", "whale shark"],
    ["What is the largest desert in the world? ", "sahara desert"],
    ["Which gas do plants give off during photosynthesis? ", "oxygen"],
    ["What is the smallest planet in our solar system? ", "mercury"],
    ["Which planet is known as the 'morning Star' or 'evening Star'? ", "venus"],
    ["What is the national flower of the United States? ", "rose"],
    ["What is the most abundant gas in earth's atmosphere? ", "nitrogen"],
    ["What is the national flower of canada? ", "maple leaf"],
    ["What is the largest species of bear? ", "polar bear"],
    ["Who is the author of 'harry potter' book series? ", "j.k. rowling"],
]
quest_list_2 = [
    ["in which year did World War ii end? ", "1945"],
    ["Which country is known as the land of the Rising Sun? ", "japan"],
    ["Who is the famous scientist known for his theory of evolution by natural selection? ", "charles darwin"],
    ["Who painted 'Starry night'? ", "van gogh"],
    ["What is the capital of brazil? ", "brasilia"],
    ["Which gas do plants absorb and use for photosynthesis? ", "co2"],
    ["Who wrote the play 'hamlet'? ", "william shakespeare"],
    ["Which element is the most abundant in the earth's crust? ","oxygen"],
    ["Who is known for discovering the laws of motion and universal gravitation? ", "isaac newton"],
    ["Which gas do humans primarily inhale when they breathe in? ", "nitrogen"],
    ["What is the capital of South korea? ", "seoul"],
    ["What is the largest species of penguin? ", "emperor penguin"],
    ["in which country was the game of chess believed to have originated? ", "india"],
    ["What is the chemical symbol for silver? ", "ag"],
    ["What is the capital of china? ", "beijing"],
    ["Which gas is known as 'laughing gas'? ", "n2o"],
    ["What is the chemical symbol for iron? ", "fe"],
    ["What is the tallest tree species in the world? ", "coast redwood"],
    ["Who was the first woman to win a nobel prize? ", "marie curie"],
    ["Which planet is known for its beautiful rings? ", "saturn"],
    ["Who was the first person to set foot on the moon? ", "neil armstrong"],
    ["in which country is the great barrier Reef located? ", "australia"],
    ["What is the smallest continent by land area? ", "australia"],
    ["in which year did christopher columbus first reach the americas? ", "1492"],
    ["What is the capital of canada? ", "ottawa"],
    ["What is the main component of the earth's core? ", "iron"],
    ["Who is the famous scientist known for his theory of gravity? ", "isaac newton"]
]

if name == "tus":
    quest_list = quest_list_2
else:
    quest_list = quest_list_1
while x < 5:
    try:
        i = randrange(0,len(quest_list))
        j = quest_list[i]
    except:
        print(f"you answered {y} question correctly out of {z}")
        exit()
    try:
        sleep(1)
        answer = inputimeout(j[0], timeout=time)
        z += 1
        sleep(1)
        quest_list.remove(j)
    except :
        print("your time is over")
        print(f"the answer is {j[1]}")
        x += 1
        z += 1
        continue
        
    if answer == "stop":
        print(f"{name}. you answered {y} question correctly out of {z}")
        exit()   
    if answer == j[1]:
        print("correct")
        y += 1
    
    else:
        print("wrong")
        print(f"the correct answer is: {j[1]}")
        x += 1
    if y >= 10:
        quest_list = quest_list_2
        if boom == 0:
            print("level 2")
            sleep(0.5)
            print()
            sleep(1)
            boom += 1

    else:
        if name == "tus":
            quest_list == quest_list_2
        else:
            quest_list = quest_list_1


scores_dict = load_scores(filename)
user = {}
user["correct_cnt"] = y
user["quest_cnt"] = z
if quest_list == quest_list_1:
    user["level"] = 1
else:
    user["level"] = 2
if scores_dict.get(name):
    if user["quest_cnt"] > scores_dict[name]["quest_cnt"]:
        scores_dict[name] = user
        store_scores(scores_dict)

else:
    scores_dict[name] = user
    store_scores(scores_dict)

print(f"{name}. you answered {y} question correctly out of {z}")
