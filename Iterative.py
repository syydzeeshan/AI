#AIM: Implement IDDFS(Iterative Deepening Depth-First Search).

import queue as Q
from RMP import dict_gn

start='Arad'
goal='Bucharest'
result=''

def DLS(city, visitedstack, startlimit, endlimit):
    global result
    found=0
    result=result+city+' '
    visitedstack.append(city)
    if city==goal:
        return 1
    if startlimit==endlimit:
        return 0
    for eachcity in dict_gn[city].keys():
        if eachcity not in visitedstack:
            found=DLS(eachcity, visitedstack, startlimit+1, endlimit)
            if found:
                return found

def IDDFS(city, visitedstack, endlimit):
    global result
    for i in range(0, endlimit):
        print("Searching at Limit: ",i)
        found=DLS(city, visitedstack, 0, i)
        if found:
            print("Found")
            break
        else:
            print("Not Found! ")
            print(result)
            print("-----")
            result=' '
            visitedstack=[]

def main():
    visitedstack=[]
    IDDFS(start, visitedstack, 9)
    print("IDDFS Traversal from ",start," to ", goal," is: ")
    print(result)


main()


##RMP.py
##
##dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
##         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
##         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
##         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}
##
##dict_gn=dict(
##Arad=dict(Zerind=75,Timisoara=118,Sibiu=140),
##Bucharest=dict(Urziceni=85,Giurgiu=90,Pitesti=101,Fagaras=211),
##Craiova=dict(Drobeta=120,Pitesti=138,Rimnicu=146),
##Drobeta=dict(Mehadia=75,Craiova=120),
##Eforie=dict(Hirsova=86),
##Fagaras=dict(Sibiu=99,Bucharest=211),
##Giurgiu=dict(Bucharest=90),
##Hirsova=dict(Eforie=86,Urziceni=98),
##Iasi=dict(Neamt=87,Vaslui=92),
##Lugoj=dict(Mehadia=70,Timisoara=111),
##Mehadia=dict(Lugoj=70,Drobeta=75),
##Neamt=dict(Iasi=87),
##Oradea=dict(Zerind=71,Sibiu=151),
##Pitesti=dict(Rimnicu=97,Bucharest=101,Craiova=138),
##Rimnicu=dict(Sibiu=80,Pitesti=97,Craiova=146),
##Sibiu=dict(Rimnicu=80,Fagaras=99,Arad=140,Oradea=151),
##Timisoara=dict(Lugoj=111,Arad=118),
##Urziceni=dict(Bucharest=85,Hirsova=98,Vaslui=142),
##Vaslui=dict(Iasi=92,Urziceni=142),
##Zerind=dict(Oradea=71,Arad=75)
##)

