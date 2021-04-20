import numpy as np
from sklearn import preprocessing, neighbors, model_selection
import pandas as pd

df = pd.read_csv("votering-201718.csv")
print(list(df))
df.drop(['punkt'],1, inplace=True)

df = df[["rost", "parti", "fodd", "kon", "intressent_id"]]

print(df.head(3))
inputLabels = ["kvinna", "man"] #kvinna: 0, man: 1
encoder = preprocessing.LabelEncoder()
encoder.fit(inputLabels)
df["kon"] = encoder.transform(df["kon"])

for i, item in enumerate(encoder.classes_):
    print(item,"--->",i)
    #16:06 in i videon