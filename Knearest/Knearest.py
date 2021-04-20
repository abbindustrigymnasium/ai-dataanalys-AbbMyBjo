import warnings
from collections import Counter
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use("fivethirtyeight")


# def eucdist(goalPlot, plot):
#     euc = sqrt((plot[0]-goalPlot[0])**2+(plot[1]-goalPlot[1])**2)
#     print(euc)
#     plt.scatter(plot[0], plot[1], s=150)

# plot = [1, 3]
# plot2 = [4, 7]
# goalPlot = [2, 5]
# plt.scatter(goalPlot[0], goalPlot[1], s=100)
# eucdist(goalPlot, plot)
# eucdist(goalPlot, plot2)

# eucdist(goalPlot, goalPlot)
# plt.show()

dataset = {
    "Lägenhet": [[22, 25], [54, 41], [36, 15], [60, 22]],
    "Villa": [[23, 42], [36, 33], [34, 55], [83, 30]],
    "Radhus": [[25, 45], [87, 67], [50, 36], [41, 39]]
}

colours = {
    "Lägenhet": "r",
    "Villa": "g",
    "Radhus": "b"
}
newFeature = [18, 50]

def kNearest(data, predict, k=3):
    if len(data) >= k:
        warnings.warn("K is set to a value less than total groups!")
    distance = []
    for group in data:
        for feature in data[group]:
            euclidianDistance = np.linalg.norm(np.array(feature)-np.array(predict))
            distance.append([euclidianDistance, group])
    votes = [i[1]for i in sorted(distance)[:k]]
    # print(Counter(votes).most_common(1))
    votesResult = Counter(votes).most_common(1)[0][0]
    return votesResult

result = kNearest(dataset, newFeature, k=4) #Hur många datavärden ska man jämföra med? K=4 => jämför mina värden med 4 pluppar
print("Du bor i "+result)
[[plt.scatter(ii[0], ii[1], color=colours[i]) for ii in dataset[i]] for i in dataset ]
plt.scatter(newFeature[0], newFeature[1], s=100)
plt.show()
