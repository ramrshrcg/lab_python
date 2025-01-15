
from queue import PriorityQueue
import pprint
import math
G = {
    "Biratnagar": {"Itahari": 22, "Rangeli": 25, "Biratchowk":30},
    "Itahari": {"Biratnagar": 22, "Dharan": 20, "Biratchowk": 11},
    "Dharan": {"Itahari": 20},
    "Biratchowk": {"Itahari": 11, "Kanepokhari": 10,"Biratnagar":30},
    "Rangeli": {"Biratnagar": 25, "Kanepokhari": 25,"Urlabari":40},
    "Kanepokhari": {"Rangeli": 25, "Biratchowk": 10, "Urlabari": 12},
    "Urlabari": {"Kanepokhari": 12, "Damak": 6,"Rangeli":40},
    "Damak": {"Urlabari": 6}
}

h={
    'Biratnager':46,
    'Itahari':39,
    'Dharan':41,
    'Rangeli':28,
    'Biratchowk':29,
    'Kanepokhari':17,
    'Urlabari':6,
    'Damak':0
}

def aStar(G, h, start, goal):
    #instantiate a priority queue
    PQ=PriorityQueue()
    #instantiate a dict to keep track of predecessor
    prev=dict()
    #instantiate a set to keep track of visited site
    visited=set()
    #enqueue the starting the state into the priority w=queue and set its predecessor to ""
    #while enquing we use the tuple (fscore, (state, gscore))
    PQ.put((0+h[start],(start, 0)))
    prev[start]=""
    #repeat until the priorityqueue is not empty
    while(not PQ.empty()):
        outstateFScore,(outState, outStateGScore)=PQ.get()
        #mark the outstate as visited
        visited.add(outState)
        if(outState==goal):
            return True, prev, outstateFScore
        for chimeki in G[outState].keys():
            if chimeki not in visited:
                chimekiGScore= outStateGScore+G[outState][chimeki]
                PQ.put((chimekiGScore+h[chimeki],(chimeki, chimekiGScore)))
                prev[chimeki]=outState
    return False, prev, -math.inf

def reconstruct_path(G, prev, goal):
    path=goal
    while  prev[goal]!= " ":
        path = prev[goal] + " -> "+ path
        goal = prev[goal]
    return path


start= "Biratnager"
goal = 'Damak'
goalFound, prev, cost=aStar(G, h,start,goal)

if (goalFound):
    pprint.pprint(prev)
    print("cost=", cost)
else:
    print("no solution found")
