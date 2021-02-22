#Ylva & My 190S

import csv
import math
import numpy as np
import matplotlib.pyplot as plt

newData = []

with open('Ylva & jag Dataanalys\Marklyft My.csv', newline='') as firstData:
    spamreader = csv.reader(firstData, delimiter=' ', quotechar='|')
    for row in spamreader:
        row=row[0].split(";")
        for index,value in enumerate(row):
            row[index] = float(value)
        newData.append(row)

oldDataX = []
oldDataY = []
oldDataZ = []
oldTime = []

for row in newData:
    oldTime.append(row[0])
    oldDataX.append(row[1])
    oldDataY.append(row[2])
    oldDataZ.append(row[3])

counter = 0
tidstämplar = []
filterX = []
filterY = []
filterZ = []

for item in newData[0:len(newData)-9]:
    XnyLista = []
    YnyLista = []
    ZnyLista = []
    x = counter
    y = counter+9
    for number in newData[x:y]:
        XnyLista.append(number[1])
        YnyLista.append(number[2])
        ZnyLista.append(number[3])

    xmedel = round(sum(XnyLista)/len(XnyLista),4)
    ymedel = round(sum(YnyLista)/len(YnyLista),4)
    zmedel = round(sum(ZnyLista)/len(ZnyLista),4)

    timeAdd = item[0]
    Xadd = xmedel
    Yadd = ymedel
    Zadd = zmedel

    tidstämplar.append(timeAdd)
    filterX.append(Xadd)
    filterY.append(Yadd)
    filterZ.append(Zadd)
    counter += 1



fig, axs = plt.subplots(3,2)
axs[0,0].plot(oldTime, oldDataX)
axs[0,0].set_title('gammal tid, X')
axs[0,1].plot(tidstämplar, filterX)
axs[0,1].set_title('ny tid, X')
axs[1,0].plot(oldTime, oldDataY)
axs[1,0].set_title('gammal tid, Y')
axs[1,1].plot(tidstämplar, filterY)
axs[1,1].set_title('ny tid, Y')
axs[2,0].plot(oldTime, oldDataZ)
axs[2,0].set_title('gammal tid, Z')
axs[2,1].plot(tidstämplar, filterZ)
axs[2,1].set_title('ny tid, Z')

for ax in axs.flat:
    ax.label_outer()

plt.show()