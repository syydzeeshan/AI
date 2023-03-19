#Breadth first search algo for romanian map problem

import queue as q
from RMP import dict_gn
def bfs(current_city, goal_city, explored_list, exploration_queue):
    explored_list.append(current_city)
    goal_reached = False
    if current_city == goal_city:
         return explored_list, True
    for each_city in dict_gn[current_city].keys():
        if each_city not in explored_list and each_city not in exploration_queue.queue:
             exploration_queue.put(each_city)
    try:
         explored_list, goal_reached = bfs(exploration_queue.get(False), goal_city, explored_list, exploration_queue)
    except q.Empty:
        return explored_list, False
    if goal_reached:
        return explored_list, True
    return explored_list, False
        
    
def main():
    start_city = 'Arad'
    goal_city = 'Bucharest'
    explored_list = []
    exploration_queue = q.Queue()
    exploration_queue.put(start_city)
    goal_reached = False
    explored_list, goal_reached = bfs(exploration_queue.get(False),goal_city, explored_list, exploration_queue)
    if not goal_reached:
         print('Could not find', goal_city)
    print(explored_list)
    
main()            

##RMP.py
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
##
##      
##
