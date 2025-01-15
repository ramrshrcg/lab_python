dict={ 
    'a':['b','c'],
    'b':['d','e'],
    'c':['f'],
    'd':['g'],
    'e':['h'],
    'f':['c'],
    'g':[],
    'h':[]
    }   

for node, neighbors in dict.items():
    print(f"{node}: {neighbors}")
