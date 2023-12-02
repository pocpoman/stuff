import random
import json
import time    

quest_data = {
    "time":0 ,
    "diff":0 , 
    "word":""

}
def difficulty_():
    _difficulty_ = int(input("choose a difficulty 1-3: "))
    if _difficulty_ == 1:
        difficulty = 10
    elif _difficulty_ == 2:
        difficulty = 7
    elif _difficulty_ == 3:
        difficulty = 4
    return difficulty,_difficulty_
def game_data(data,filename):
    try:
        
        with open(filename, "a") as game:
            game.write(json.dumps(data, indent = 3))
            game.close()
    except:
        return

mistake = 0 
from inputimeout import inputimeout

input_ = 0
long_words = ["comfortable",
    "a very long word",
    "jujutsu kaisen",
    "replicate", 
    "hamburger",
    "people",
    "luminosity",
    "serendipity",
    "eccentricity",
    "versatility",
    "camaraderie",
    "tranquility",
    "diligence",
    "authenticity",
    "resilience",
    "equilibrium",
    "excuse me"]
input_2 = input("would you like to play a game: ")
filename = "fast_writing_" + input("what is your name: ") + ".json"
f = open(filename, "w")
f.write("")
f.close
difficulty, quest_data["diff"] = difficulty_()

while input_2 == "yes":
    x = random.randrange(0,len(long_words))
    binchiling = long_words[x]
    quest_data["word"] = binchiling
    while input_ != binchiling:
        print("get ready")
        time.sleep(1)
        print("go")
        try:
            start_time = int(time.time())
            input_ = inputimeout(f"write {binchiling}: ",timeout = difficulty)
            
        except:
            input_ = "Your time is over!"
            print(input_)
        if input_ == "":
            print("ok")
            q_1 = input("would you like choose a new difficulty:")
            if q_1 == "yes":
                difficulty_()
                break
            else:
                exit()
        time.sleep(1)
        print("...")
        time.sleep(1)
        if input_ == binchiling:
            print(f"correct")
            over_time = int(time.time()) - start_time
            quest_data["time"] = over_time
            game_data(quest_data, filename)
            print(f"took you {over_time} seconds")
        else:
            print(f"you did not write {binchiling}")
            mistake += 1
        if mistake == 10:
            print("game over")
            q_1 = input("would you like choose a new difficulty:")
            if q_1 == "yes":
                difficulty_()
            else:
                exit()
        time.sleep(1)


