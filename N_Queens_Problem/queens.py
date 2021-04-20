from random import randint

Queens = "82417536" #28% = vinst

rows = "ABCDEFGH"
cols = "12345678"

def PlaceOnBoard(Queens, rows, cols):
    Board = [r+c for r in rows for c in cols]
    BoardDict = {i : "." for i in Board}
    counter = 0
    BoardPlaces = []
    for Queen in Queens:
        if Queen != ".":
            BoardDict[rows[counter]+Queen]= "Q"
            BoardPlaces.append(rows[counter]+Queen)
        counter += 1
    return BoardDict, BoardPlaces

def FitFunction(BoardDict, BoardPlaces, logger):
    #Tips
    #print(BoardDict[A2])
    AllQueenInteractions = 0
    for QueenPlace in BoardPlaces:
        if logger:
            print("QueenPlace:", QueenPlace)
        QueenNumber = int(QueenPlace[1])
        QueenLetter = QueenPlace[0]
        counter = 1
        
        for letter in rows:
            if letter == QueenLetter:
                break
            counter += 1
        for other in rows[counter::]:
            if BoardDict[other+QueenPlace[1]] == "Q":
                if logger:
                    print("Rows"+QueenPlace+" "+(other+QueenPlace[1]))
                AllQueenInteractions += 1

    parallell = QueenNumber+1
    for other in rows[counter::]:
        if (parallell > 8):
            break
        if BoardDict[other+str(parallell)] == "Q":
            if logger:
                print("Up "+QueenPlace+" "+(other+str(parallell)))
            AllQueenInteractions += 1
        parallell += 1

    parallell = counter+QueenNumber-1
    moreThan = parallell-len(Queens)
    cutList = rows
    if moreThan > 0:
        cutList = rows[moreThan:]
        parallell -= moreThan
    for other in cutList:
        if(parallell==QueenNumber):
            break
        if BoardDict[other+str(parallell)] == "Q":
            if logger:
                print("Down "+QueenPlace+" "+(other+str(parallell)))
            AllQueenInteractions += 1
        parallell -= 1

    AttackingLadies = 28-AllQueenInteractions
    if logger:
        print("Interactions:", AllQueenInteractions, "Score:", AttackingLadies)
    return AttackingLadies

def PlaceQueensRandom(numberOfQueens, numberOfBoards):
    QueensList = []
    for queensOnBoard in range(numberOfBoards):
        Queens = ""
        for Q in range(numberOfQueens):
            Queens += str(randint(1, numberOfQueens))
        QueensList.append(Queens)
    return QueensList

def NormalizeToPercent(Scores):
    sum = 0
    for score in Scores:
        sum += score
    
    percent = []
    for score in Scores:
        percent.append(score/sum*100)
    return percent

def CreateNewQueens(queens, percent, logger):
    selectQueens = []
    for counter in range(len(queens)):
        randomNumber = randint(0, 99)
        percentValue = 0
        for P in range(len(percent)):
            percentValue += percent[P]

            if randomNumber <= percentValue:
                if logger:
                    print("Random number:", randomNumber, "Board:", P+1)
                selectQueens.append(queens[P])
                break

    if logger:
        print("Selected:", selectQueens)
    
    if len(selectQueens) < 4:
        print("Selected:", selectQueens, queens, percent)
        input()
    
    newQueens = []
    startIndex = 0
    for counter in range(int(len(selectQueens)/2)):
        dividePlace = randint(1, len(selectQueens[0]))
        newQueens.append(selectQueens[counter+startIndex][:dividePlace]+selectQueens[counter+1+startIndex][dividePlace:])
        newQueens.append(selectQueens[counter+1+startIndex][:dividePlace]+selectQueens[counter+startIndex][dividePlace:])
        startIndex += 1

    for queen in range(len(newQueens)):
        qasList = list(newQueens[queen])
        for place in range(len(qasList)):
            randomNumber = randint(0, 10)
            if randomNumber == 5:
                qasList[place] = str(randint(1, 8))
                if logger:
                    print("Mutation:", queen, "=>", qasList, place)
        newQueens[queen] = "".join(qasList)
    if logger:
        print("New Queens:", newQueens)

    return newQueens

allQueens = PlaceQueensRandom((len(rows)), 4)

bestScore = 0
print(allQueens)
iteration = 1

while bestScore < 28:
    scores = []
    for oneQueen in allQueens:
        BoardDict, BoardPlaces = PlaceOnBoard(oneQueen, rows, cols)
        scores.append(FitFunction(BoardDict, BoardPlaces, True))
    
    for s in range(len(scores)):
        score = scores[s]
        if score > bestScore:
            print("New best score", score, "with", allQueens[s], "in iteration", iteration)
            bestScore = score

    if iteration%10 == 0:
        print(scores, "Iteration:", iteration)
    percent = NormalizeToPercent(scores)

    allQueens = CreateNewQueens(allQueens, percent, True)
    iteration += 1
