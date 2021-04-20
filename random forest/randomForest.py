import pandas as pd
import random

def CreateValues():
    values=[]
    template=[
        {"label":"Kylrum", "mintemp":6.4, "maxtemp":14.34, "minhum": 20, "maxhum": 56.6},
        {"label": "Klassrum", "mintemp": 18.4, "maxtemp": 24.34, "minhum": 70, "maxhum": 96.6},
        {"label": "Kylrum", "mintemp": 17.4, "maxtemp": 23.65, "minhum": 65, "maxhum": 93}
    ]
    for room in template:
        times = random.randint(1, 101)
        for i in range(0, times):
            newTemp = random.uniform(room["mintemp"], room["maxtemp"])
            newHum = random.uniform(room["minhum"], room["maxhum"])
            value = [newHum, newTemp, room["label"]]
            values.append(value)
    print(values[0])
    print(values[2])
    return values

newData = CreateValues()
newValues = pd.DataFrame(newData)
#26:55 google collab