import copy


def getAllSets(hand):
    '''get all sets in a hand'''
    allSets = []
    for num in set(hand):
        if hand.count(num) >= 2:
            allSets.append([num]*hand.count(num))
    return allSets


def getAllRuns(hand):
    '''get all possible runs in a hand'''
    allRuns = []
    newRun=True
    run=[]
    hand=set(hand)
    for i in range(1,13):
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
    return allRuns


def getPossRuns(runs, length):
    '''get all possible runs of the specified length'''
    possRuns = []
    for run in runs:
        i = 0
        while length + i <= len(run):
            possRuns.append(run[i:length+i])
            i+=1
    return possRuns


def checkPhase(phase, allSets, allRuns):
    '''Check if the sets and runs complete the phase'''
    hasSet1, hasSet2, hasRun = False, False, False
    set1,set2,run = phases[phase]
    currentSets = copy.deepcopy(allSets)
    k=[]
    if set1 == 0:
        hasSet1 = True
    else:
        k = [s[0] for s in currentSets if len(s)==set1]
        for _set in currentSets:
            if len(_set) >= set1:
                hasSet1 = True
                for _ in range(set1):
                    _set.pop()
                break
    if set2 == 0:
        hasSet2 = True
    else:
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
            if k:
                if len(_run) >= run and not all(s in _run for s in k):
                    hasRun = True
                    break
            else:
                if len(_run) >= run:
                    hasRun = True
                    break
    return hasSet1 and hasSet2 and hasRun


# How many cards needed in each of the phases
# Set 1, Set 2, Run
# 0 means it's not needed
phases = {
    1: [3,3,0],
    2: [3,0,4],
    3: [4,0,4],
    4: [0,0,7],
    5: [0,0,8],
    6: [0,0,9],
    7: [4,4,0],
    #8 Skip phase 8
    9: [5,2,0],
    10:[5,3,0]
}


def checkAllPhases(hand):
    '''
    Takes a list of integers and displays which phases it qualifies for
    '''
    allRuns = getAllRuns(hand)
    allSets = getAllSets(hand)

    qualifiedHand = False

    for phase in phases:
        if checkPhase(phase, allSets, allRuns):
            qualifiedHand = True
            print(f"You qualify for phase {phase}.")

    if not qualifiedHand:
        print(f"Sorry, you do not qualify for any phases with a hand of {hand}")


if __name__ == "__main__":
    print("Welcome to the Phase 10 PhazeChecker! \n")

    validHand = False

    while not validHand:
        print("Enter your 10 numbers below and see which phases you qualify for. \n\
        (Enter all ten numbers seperated by spaces)")

        raw_hand = input()

        if all(x.isdigit() for x in raw_hand.split()):
            validHand = True
        else:
            print('Error. Please enter 10 numbers separated by spaces.')

    hand = [int(x) for x in raw_hand.split()]

    checkAllPhases(hand)