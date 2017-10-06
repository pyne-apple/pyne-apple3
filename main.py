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

    numStates = sys.argv[1]
    numActions = sys.argv[2]
    inputFileName = sys.argv[3]
    y = sys.argv[4]
    
    # Reading in data from input file
    with open(inputFileName) as inputFile:

        for line in inputFile:
            # Get data from line
            spaceSplit = line.replace('\n', '').replace(')', '').split(" (")
            # spaceSplit = re.split(r" \(", line.replace('\n', '').replace(')', ''))

            # Get state and reward
            stateName, rewardString = spaceSplit[0].split()
            reward = int(rewardString)
            del spaceSplit[0] 

            # print(spaceSplit)



if __name__ == "__main__":
    main()


