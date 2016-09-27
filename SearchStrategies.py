from collections import defaultdict

class node:                                                                 #Creating a class known as node
    def __init__(self,STATE,PARENT,ACTION,PATHCOST):                        #Defining Class Attributes
        self.state=STATE
        self.parent=PARENT
        self.action=list(ACTION)
        self.pathCost=int(PATHCOST)


adjacencyMatrix=defaultdict(list)                                           #Creating an Adjacency Matrix of Type Dictionary
                                                                            #where values are of type list
fileObject=open('Dataset.txt','r',encoding='LATIN-1')                       #Reading the dataset from the text file
dataset=list(fileObject)

for i in range(len(dataset)):                                               #Filling the data from the text file into a dictionary
    for j in range(0,2):
        key=dataset[i].split(',')[j]
        if key in adjacencyMatrix.keys():
            if j==0:
                adjacencyMatrix[key].append(dataset[i].split(',')[1])
            else:
                adjacencyMatrix[key].append(dataset[i].split(',')[0])
        else:
            if j==0:
                adjacencyMatrix[key].append(dataset[i].split(',')[j+1])
            else:
                adjacencyMatrix[key].append(dataset[i].split(',')[j-1])

def initializeFrontier(initialState):                                       # Function to Initialize Frontier
    queue = []
    queue.append([initialState])
    return queue

def goalTest(finalnodeState,finalState):                                    #Function to test Goal
    if finalnodeState == finalState:
        return 1

def expandNode(nodes,frontier,exploredSet,newPath):                          #Function to Expand Node

    for adjacent in adjacencyMatrix.get(nodes,[]):
        if adjacent not in frontier and adjacent not in exploredSet:
            expandedNodes=list(newPath)
            expandedNodes.append(adjacent)
            updateFrontier(expandedNodes,frontier)
    return frontier

def updateFrontier(expandedNodes,frontier):                                  #Function to Update Frontier
    frontier.append(expandedNodes)

def calculatePathCost(newPath):                                              #Function to Calculate Path Cost
    pathCost=0
    if len(newPath)<2:
        return 1
    for i in range(len(dataset)):
        for j in range(len(newPath)):
            if newPath[j-1] in dataset[i] and newPath[j] in dataset[i]:
                pathCost+=int(dataset[i].split(',')[2])
                if len(newPath)==2:
                    break
    return pathCost


def graphSeacrh(initialState,finalState,searchStrategy):                     #General function for graphSearch where we provide
                                                                             #source,destination and the search Strategy as input
    frontier=initializeFrontier(initialState)
    newnode=node
    pathAddress=0
    cost=0
    exploredSet = []
    while frontier:
        if frontier==[]:
            print('Cannot Search, Graph is Empty')
        else:
            if searchStrategy=='bfs':
                pathAddress=0
            elif searchStrategy=='dfs':
                pathAddress=-1
            else:
                for i in range(0,len(frontier)):
                    lowestCost=calculatePathCost(frontier[i])
                    if lowestCost<cost or i==0:
                        cost=lowestCost
                        pathAddress=i
            newPath=frontier.pop(pathAddress)                                #Popping the element from the stack or the queue
            newnode.state=newPath[-1]                                        #according to the search strategy
            newnode.parent=newPath[len(newPath)-2]
            newnode.pathCost=calculatePathCost(newPath)                      #Calculating path cost
            test=goalTest(newnode.state,finalState)                          #Testing Goal
            if test==1:
                return newPath,newnode.pathCost
            else:
                exploredSet.append(newnode.state)                            #Updating the Explored Set
                frontier=expandNode(newnode.state,frontier,exploredSet,newPath)             #Updating the Frontier


def ChooseNode():                                                            #Function to take input from the user and implement
    source=input('Enter the Starting City: ')                                #the search strategies by passing diffrent values in
    destination=input('Enter the Destination City: ')                        #the graphSearch function
    searchstrategy=['bfs','dfs','ucs']
    for x in range(len(searchstrategy)):
        if x==0:
            print('\n'+'Breadth First Search')
            print(graphSeacrh(source,destination,searchstrategy[0]))
        elif x==1:
            print('\n'+'Depth First Search')
            print(graphSeacrh(source, destination, searchstrategy[1]))
        else:
            print('\n'+'Uniform Cost Search')
            print(graphSeacrh(source, destination, searchstrategy[2]))


ChooseNode()                                                                #Calling the ChooseNode function to implement all the Algorithms



