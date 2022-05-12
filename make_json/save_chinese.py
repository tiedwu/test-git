import json

names = {'0001': {"name": u"幸运"}, 
            '0002': {"name": u"星河"}}

print(names)

with open('test.json', "w", encoding='utf-8') as f:
    json.dump(names, f, indent=4, ensure_ascii=False)


