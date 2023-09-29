import statistics
import random
import json
import time    

filename = "math_data.json"

def resort(excercises, e):
    asked = e["good_cnt"] + e["bad_cnt"]
    e["prob"] = 5000 * (e["bad_cnt"] / asked) + 2500 * (statistics.median(e["times"]) / 30)  

    return sorted(excercises, key=lambda d: d['prob'], reverse=True) 

def store_excercise_data(obj):
    try:
        with open(filename, "w") as fmath:
            fmath.write(json.dumps(obj))
            fmath.close()
    except:
        return

def get_excercise_data():

    try:
        with open(filename, "r") as fmath:
            return json.loads(fmath.read())
    except:
        pass

    excercises = list()
    for i in range(2,10):
        for j in range(i,10):
            e = dict()
            e["x"] = i
            e["y"] = j
            e["prob"] = 10000
            e["good_cnt"] = 0
            e["bad_cnt"] = 0
            e["times"] = []
            
            excercises.append(e)

    return excercises

answer = 100000000000000000000000
y = 0


random_list = [1] * 1300
random_list += [2] * 1200
random_list += [3] * 1000
random_list += [4] * 985
random_list += [5] * 980
random_list += [6] * 970
random_list += [7] * 960
random_list += [8] * 950
random_list += [9] * 930
random_list += [10] * 910
random_list += [11] * 870
random_list += [12] * 830
random_list += [13] * 770
random_list += [14] * 720
random_list += [15] * 660
random_list += [16] * 600
random_list += [17] * 530
random_list += [18] * 460
random_list += [19] * 380
random_list += [20] * 300
random_list += [21] * 210
random_list += [22] * 120
random_list += [23] * 90
random_list += [24] * 70
random_list += [25] * 60
random_list += [26] * 55
random_list += [27] * 50
random_list += [28] * 45
random_list += [29] * 44
random_list += [30] * 43
random_list += [31] * 42
random_list += [32] * 41
random_list += [33] * 40
random_list += [34] * 39
random_list += [35] * 38


correct_list = ["awesome","great","amazing","spectacular","correct","good job","indeed"]

excercises = get_excercise_data()


    
while answer != 0:
    yum = random.randrange(0,len(random_list))
    index = random_list[yum]
    question = excercises[index]
       
    num_1 = question["x"]
    num_2 = question["y"]
    word = random.randrange(0,len(correct_list))
    word = correct_list[word]
    
    answer = None
    while answer == None:
        try:
            start_time = int(time.time())
            answer = int(input(f"{num_1}x{num_2} = " ))
        except:
            print("oops")

    diff = int(time.time()) - start_time
    
    if not "answers" in question:
        question["answers"] = []

    question["times"].append(diff)
    question["answers"].append(answer)

    if answer == 0:
        print("ok")
        store_excercise_data(excercises)
        exit()
    elif answer == num_1 * num_2:
        print(word, "\n\n")
        question["prob"] -= 5000
        question["good_cnt"] += 1
    else:
        print("wrong. it is ", num_1 * num_2, "\n\n")
        question["prob"] += 4000
        question["bad_cnt"] += 1

    if diff > 30:
        question["prob"] += 4000

    excercises = resort(excercises, question)