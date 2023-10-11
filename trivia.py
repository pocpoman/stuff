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
    ["Who is the author of 'harry potter' book series? ", "j.k. rowling"],
]
quest_list_2 = [
    ["in which year did World War ii end?", "1945"],
    ["Who wrote the novel '1984'?", "george orwell"],
    ["Which country is known as the land of the Rising Sun?", "japan"],
    ["Who is the famous scientist known for his theory of evolution by natural selection?", "charles darwin"],
    ["Who painted 'Starry night'?", "van gogh"],
    ["What is the capital of brazil?", "brasília"],
    ["Which gas do plants absorb and use for photosynthesis?", "co2"],
    ["Who wrote the play 'hamlet'?", "William Shakespeare"],
    ["Which element is the most abundant in the earth's crust?","oxygen"],
    ["What is the main component of earth's outermost layer, the lithosphere?", "Silicon (Si)"],
    ["Who is known for discovering the laws of motion and universal gravitation?", "isaac newton"]
    ["Which gas do humans primarily inhale when they breathe in?", "nitrogen"],
    ["What is the capital of South korea?", "Seoul"],
    ["in which country was the game of chess believed to have originated?", "india"],
    ["What is the chemical symbol for silver?", "ag"],
    ["What is the process by which plants lose water vapor through small openings in their leaves?", "Transpiration"],
    ["Who wrote 'The catcher in the Rye'?", "j.d. Salinger"],
    ["What is the capital of china?", "beijing"],
    ["Which gas is known as 'laughing gas'?", "n2o"],
    ["What is the chemical symbol for iron?", "fe"],
    ["What is the tallest tree species in the world?", "coast Redwood"],
    ["Who was the first woman to win a nobel prize?", "marie curie"],
    ["Which planet is known for its beautiful rings?", "Saturn"],
    ["What is the chemical symbol for potassium?", "k"],
    ["Who was the first person to set foot on the moon?", "neil armstrong"],
    ["in which country is the great barrier Reef located?", "australia"],
    ["What is the smallest continent by land area?", "australia"],
    ["in which year did christopher columbus first reach the americas?", "1492"],
    ["What is the capital of canada?", "ottawa"],
    ["What is the main component of the earth's core?", "iron"],
    ["Who is the famous scientist known for his theory of gravity?", "isaac newton"]
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