from playernames import names
import json
import random

#print(names)

file = "user_data.json"

def create_user(data, userid, name, degree):
    user_data = {\
            "nickname": name,\
            "buildings": {"castle": 0, "house": 0, "guard": 0, "camp": 0}, \
            "resources": 0, "resources_increase": 0, \
            "residents": 0, "residents_increase": 0, \
            "soldiers": {"lancer": 0, "shieldman": 0, "archer": 0, "cavalryman": 0}, \
            "mines": 0, "crystal": 0}
    
    # define degree
    # H: High resource(500M-1000M), High army(5K-10K), Middle guard (500 ~ 1000) - 0.01%
    # M: High resource(200M-500M), Some army(1K - 2K), Little guard (200 - 500) - 10%
    # L: Middle resource(100M-200M), Zero army, Bit guard (0 - 100) - 90%
    if degree == 'H':
        user_data["resources"] = random.randint(500000000, 1000000000)
        for k in user_data["soldiers"]:
            user_data["soldiers"][k] = random.randint(5000, 10000)
        user_data["buildings"]["guard"] = random.randint(500, 1000)
    elif degree == 'M':
        user_data["resources"] = random.randint(200000000, 500000000)
        for k in user_data["soldiers"]:
            user_data["soldiers"][k] = random.randint(1000, 2000)
        user_data["buildings"]["guard"] = random.randint(200, 500)
    elif degree == 'L':
        user_data["resources"] = random.randint(100000000, 200000000)
        for k in user_data["soldiers"]:
            user_data["soldiers"][k] = 0
        user_data["buildings"]["guard"] = random.randint(0, 100)        
        
    data[userid] = user_data
    
    # save chinese in json    
    with open(file, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("create user: %s %s resources: %s soldiers: %s" % (userid, name, str(format(user_data["resources"], ",")), user_data["soldiers"]))    
    
def delete_user(user):

    with open(file, "r") as f:
        data = json.load(f)
    data.pop(user)
    
    with open(file, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("delete user: %s" % user)        

def check_user(user, name, degree):
    with open(file, "r") as f:
        data = json.load(f)
        if not user in data.keys():
            create_user(data, user, name, degree)

#check_user('000001', 'EmpireKing', 'H')

#delete_user('000001')

def create_id():
    degree_L = 0
    degree_M = 0
    degree_H = 0
    for i in range(len(names)):
        user = "%06d" % (i+1)
        #print(user, names[i])
        n = random.randint(1, 1000)
        if n < 10:
            check_user(user, names[i], 'H')
            degree_H += 1
        elif n >= 900 and n < 1000:
            check_user(user, names[i], 'M')
            degree_M += 1
        else:
            check_user(user, names[i], 'L')
            degree_L += 1
    print("H:%s M:%s L:%s" % (degree_H, degree_M, degree_L))

create_id()

    
