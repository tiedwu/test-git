from random import randint
import math

unit_military_abilities = {
    'guard': [5,  10,  10, 0], 
    'lancer': [5,  13,  10, 3600],
    'shieldman': [9,  7,  15, 3700], 
    'archer': [3,  18,  8,  3800],
    'cavalryman': [7,  15,  11,  3900]
}

enemies = {
    "guard": 100, 
    "lancer": 1805, 
    "shieldman": 1152, 
    "archer": 1279, 
    "cavalryman": 1725
}

me = {
    "lancer": 0, 
    "shieldman": 0, 
    "archer": 1000, 
    "cavalryman": 20000
}

position = ['guard',  'shieldman',  'lancer', 'cavalryman',  'archer']

def get_formation(army):
    matrix = []
    for p in position:
        if p in army.keys() and army[p] != 0:
            matrix.append([p,  army[p]])
    return matrix

def get_military_abilities(military_info):
    military,  amount = military_info[0],  military_info[1]
    hp = unit_military_abilities[military][0] * amount
    attack = unit_military_abilities[military][1] * amount
    armor = unit_military_abilities[military][2] * amount
    return hp,  attack,  armor

def is_alive(army):
	c = sum([army[x][1] for x in range(len(army))])
	return False if c == 0 else True

def get_fortune():
	return True if randint(1,  100)  <  25 else False

def has_archer(matrix):
    c = [matrix[n][0] for n in range(len(matrix))]
    return True if "archer" in c else False

def get_attack(military, group):
	for n in range(len(group)):
		if group[n][0] == military:
			return group[n][1] * unit_military_abilities[military][1]

def defend_cavalryman(attack,  group):
    defends = group
    last_military = group[-1][0]
    defend_hp,  defend_attack,  defend_armor = get_military_abilities(group[-1])
    remain_hp = defend_hp + defend_armor - attack
    if remain_hp > 0:
        remain_amount = get_amount(remain_hp,  last_military)
        defends[-1][1] = remain_amount
    else:
        defends.pop(-1)
    return defends

def defend(attack,  group):
    defends = group
    first_military = group[0][0]
    defend_hp,  defend_attack,  defend_armor = get_military_abilities(group[0])
    remain_hp = defend_hp + defend_armor - attack
    if remain_hp > 0:
        remain_amount = get_amount(remain_hp, first_military)
        defends[0][1] = remain_amount
    else:
        defends.pop(0)
    return defends

def get_amount(hp, military):
	unit  = unit_military_abilities[military][0] + unit_military_abilities[military][2]
	return int(math.ceil(hp / unit))

def defend_archer(attack,  group):
    defends = []
    for n in range(len(group)):
        military = group[n][0]
        group_hp,  group_attack,  group_armor = get_military_abilities(group[n])
        hp_remain = group_hp + group_armor - attack
        if hp_remain > 0:
            remain_amount = get_amount(hp_remain,  military)
            defends.append([military,  remain_amount])
    return defends

def fight(g1,  g2):
	result = {'resources': 0, 
				"soldiers": {"lancer": 0, "shieldman": 0, 
								"archer": 0, "cavalryman": 0}}
	MAXLOOP = 5
	nLoop = 0
	WIN = False
	while nLoop < MAXLOOP:
		print("Loop [%d]" % nLoop)
		g1_military = g1[0][0]
		g2_military = g2[0][0]

		if g1_military != "archer" and has_archer(g1) and get_fortune() and g2_military != "guard":
			print("attacks: archer get fortune to attack all",  g2)
			g1_archer_attack = get_attack("archer", g1)
			g2 = defend_archer(g1_archer_attack, g2)
			print("g2: ", g2)
			if not is_alive(g2):
				WIN = True
				break
		if g2_military != "archer" and has_archer(g2) and get_fortune():
			print("defends: archer get fortune to attack all",  g1)
			g2_archer_attack = get_attack("archer", g2)
			g1 = defend_archer(g2_archer_attack, g1)
			print("g1", g1)
			if not is_alive(g1):
				WIN = False
				break

		if g1_military == "cavalryman" and g2[-1][0] != "guard" and get_fortune():
			print("attacks: cavalryman get fortune to acctack %s" % g2[-1][0])
			g1_cavalryman_attack = get_attack("cavalryman", g1)
			g2 = defend_cavalryman(g1_cavalryman_attack,  g2)
			print("g2: ", g2)
			if not is_alive(g2):
				WIN = True
				break
		if g2_military == "cavalryman" and g1[-1][0] != "guard" and get_fortune():
			print("defends: cavalryman get fortune to acctack %s" % g1[-1][0])
			g2_cavalryman_attack = get_attack("cavalryman", g2)
			g1 = defend_cavalryman(g2_cavalryman_attack,  g1)
			print("g1: ", g1)
			if not is_alive(g1):
				WIN = False
				break

		g1_military = g1[0][0]
		g2_military = g2[0][0]
		g1_hp,  g1_attack,  g1_armor = get_military_abilities(g1[0])
		g2_hp,  g2_attack,  g2_armor = get_military_abilities(g2[0])

		if g1_military == "lancer" and get_fortune():
			g1_attack = g1_attack * 2
		if g2_military == "lancer" and get_fortune():
			g2_attack = g2_attack * 2

		if g2_military == "shieldman":
			g1_attack = math.ceil(g1_attack / 2)

        # calc damage
		print("attacks: %s attack %s" % (g1_military,  g2_military))
		g2 = defend(g1_attack,  g2)
		print("g2: ", g2)
		print("defends: %s attack %s" % (g2_military,  g1_military))
		g1 = defend(g2_attack,  g1)
		print("g1: ", g1)

		if not is_alive(g1):
			WIN = False
			break
		if not is_alive(g2):
			WIN = True
			break
		nLoop += 1

	if WIN:
		for n in range(len(g1)):
			military, amount = g1[n][0], g1[n][1]
			result['resources'] += unit_military_abilities[military][3] * amount
			result['soldiers'][military] = amount

	return result

attacks = get_formation(me)
defends = get_formation(enemies)
#print(attacks)
#print(defends)
result = fight(attacks,  defends)
print("War of Result: ",  result)
