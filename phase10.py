deck = list(range(1,13))*8

import random
import copy

def getAllSets(hand):
    allSets = []
    for num in set(hand):
        if hand.count(num) >= 2:
            allSets.append([num]*hand.count(num))
#             print(num, hand.count(num))
    print(allSets, 'all sets')
    return allSets


def getAllRuns(hand):
    allRuns = []
    newRun=True
    run=[]
    hand=set(hand)
    for i in range(1,13):
#         print(i,newRun)
        if newRun and i in hand:
            run=[i]
            newRun=False
        elif i-1 in run:
            if i in hand:
                run+=[i]
            else:
                if len(run)>=2:
                    allRuns.append(run)
                run=[]
                newRun=True
    else:
        if len(run)>=2:
            allRuns.append(run)  
    print(allRuns)
    return allRuns


def getPossRuns(runs, length):
    possRuns = []
    for run in runs:
        i = 0
        while length + i <= len(run):
            possRuns.append(run[i:length+i])
#             print(run[i:length+i])
            i+=1
#     print(possRuns)
    return possRuns

phases = {
    #Set 1, Set 2, Run
    1: [3,3,0],
    2: [3,0,4],
    3: [4,0,4],
    4: [0,0,7],
    5: [0,0,8],
    6: [0,0,9],
    7: [4,4,0],
    #8
    9: [5,2,0],
    10:[5,3,0]
}

def checkPhase(phase):
    hasSet1, hasSet2, hasRun = False, False, False
    set1,set2,run = phases[phase]
#     print(set1,set2,run)
    currentSets = copy.deepcopy(allSets)
#     print('currentset',currentSets)
    if set1 == 0:
        hasSet1 = True
    else:
        for _set in currentSets:
            if len(_set) >= set1:
                hasSet1 = True
                for _ in range(set1):
                    _set.pop()
                break
#                 currentSets.remove(_set)
    if set2 == 0:
        hasSet2 = True
    else:
#         print("sets",currentSets)
        for _set in currentSets:
            if len(_set) >= set2:
                hasSet2 = True
                for _ in range(set2):
                    _set.pop()
                break
                
    if run == 0:
        hasRun = True
    else:
        for _run in getPossRuns(allRuns, run):
            if len(_run) >= run:
                hasRun = True
                break
#     print(hasSet1,hasSet2,hasRun)
    return hasSet1 and hasSet2 and hasRun

random.shuffle(deck)
print(sorted(deck[:10]))
# hand = deck[:10]
hand = [2,3,4,5,5,5,7,7,7]
allRuns = getAllRuns(hand)
allSets = getAllSets(hand)
checkPhase(7)
# print('new',allRuns, allSets)
for phase in phases:
    print(phase, checkPhase(phase))
    