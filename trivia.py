from inputimeout import inputimeout
from random import *
from time import sleep
x = 0
def diff_(x):
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

answer = 0
quest_list_1 = [
["what is the name of the first star in the solar system?: ", "the sun"],
["what is the name of the corrent usa president?: ","jo biden"],
["what is the last name of barak obama?: ","obama"],
["what country blow up hiroshima and nagasaki?: ","usa"]]
while answer != "stop" or x > 20:
    i = randrange(0,len(quest_list_1))
    j = quest_list_1[i]
    try:
        answer = inputimeout(j[0], timeout=8)
        sleep(1)
    except:
        print("your time is over")
        print(f"the answer is {j[1]}")
    if answer == {j[1]}:
        print("correct")
    else:
        print("wrong")
        print(f"the correct answer is: {j[1]}")