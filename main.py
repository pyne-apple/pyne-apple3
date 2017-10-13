import math
import sys
import pandas as pd
import numpy as np

class stateData():
    def __init__(self, startState, reward, transitionsList):
        self.startState = startState
        self.reward = reward
        self.transitionsList = transitionsList


def main():
    if len(sys.argv) != 5:
        # (1) the number of states of the MDP, 
        # (2) the number of possible actions, 
        # (3) the input file as described above, and 
        # (4) the discount factor (γ).
        # python main.py 4 2 test.in 0.9
        print ("Please execute with 4 arguments <#States> <#Actions> <Input File> <Discount Factor>")
        exit()

    numStates = int(sys.argv[1])
    numActions = int(sys.argv[2])
    inputFileName = sys.argv[3]
    y = float(sys.argv[4])
    
    # Reading in data from input file
    with open(inputFileName) as inputFile:
        statesList = []
        actionsList = []
        for x in range(0, numActions, 1):
            actionsList.append('a' + (x + 1).__str__())
        statesReward = {}
        transitionDict = {}
        for line in inputFile:
            # Get data from line
            spaceSplit = line.replace('\n', '').replace(')', '').split(" (")
            #print (spaceSplit)

            # Get state and reward
            stateName, rewardString = spaceSplit[0].split()
            reward = int(rewardString)
            del spaceSplit[0]
            statesReward[stateName] = reward
            statesList.append(stateName)

        maxSumDF = pd.DataFrame.from_records([[None]*numStates for x in range(20)], columns=statesList)

        ##I'm sorry John! I really can't think of any other way of doing this!##
        ## I'm so ashamed of this duplicated code
        transition = pd.DataFrame.from_records(np.zeros((numActions,numStates)),index=actionsList, columns=statesList)
    with open(inputFileName) as inputFile:
        for line in inputFile:
            spaceSplit = line.replace('\n','').replace(')','').split(" (")
            stateName1, rewardString = spaceSplit[0].split()
            transitionDict[stateName1] = pd.DataFrame.from_records(np.zeros((numActions, numStates)), index=actionsList, columns=statesList)
            del spaceSplit[0]
            for each in spaceSplit:
                actionName, stateName, probString = each.split()
                transitionDict[stateName1].set_value(actionName, stateName, float(probString))
        print(transitionDict)
        #print(maxSumDF)



        for index, row in maxSumDF.iterrows():
            lastIndex = int(index) - 1
            lastIndexString = lastIndex.__str__()
            for state in statesList:
                #this is where the calclation happens
                #INSIDE THIS LOOP WE ACCESS EACH CELL IN THE MAXSUMDF
                maxingActionsList = []
                maxSumDF.at[index, state] = "p"
                for action in actionsList:
                    sum = 0
                    sum = statesReward[state]
                    insideSum = 0
                    for insideState in statesList:
                        ##this is to access the inside of transitionDict[state]
                        if (transitionDict[state].at[action, insideState] is not 0.0):
                            if (lastIndex < 0):
                                insideSum = insideSum + (transitionDict[state].at[action, insideState] * statesReward[insideState])
                            else:
                                insideSum = insideSum + (transitionDict[state].at[action, insideState] * maxSumDF.at[lastIndex, insideState])
                    sum = sum + (y*insideSum)
                    maxingActionsList.append(sum)
                maxSumDF.at[index, state] = max(maxingActionsList)
        print(maxSumDF)




if __name__ == "__main__":
    main()


