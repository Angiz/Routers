import numpy as np
import networkx as nx

import ctypes, ctypes.util

def dijkstra(matrix, m, n):
    xyz = int(input("Enter the source vertex"))
    cost = [[0 for x in range(m)] for x in range(1)]
    offsets = []
    offsets.append(xyz)
    elepos = 0
    for j in range(m):
        cost[0][j] = matrix[xyz][j]
    mini = 999
    for x in range(m - 1):
        mini = 999
        for j in range(m):
            if cost[0][j] <= mini and j not in offsets:
                mini = cost[0][j]
                elepos = j
        offsets.append(elepos)
        for j in range(m):
            if cost[0][j] > cost[0][elepos] + matrix[elepos][j]:
                cost[0][j] = cost[0][elepos] + matrix[elepos][j]
    print("The shortest path", offsets)
    print("The cost to various vertices in order", cost)

number_of_routers=int(input("Enter number of routers: "))
number_of_stations=int(input("Enter number of stations: "))

##sprawdzamy,czy parametry sa ok
if (number_of_routers <= 0 or number_of_stations <= 0):
    raise ValueError("False parameters")

routers = []  ##lista routerow
bandwidths = []  ##lista z przepustowosciami
stations = []  ##lista ze stacjami
distances = [] ##lista z odleglosciami
Times = [] ##lista z czasami polaczenia z routerem
G=nx.Graph()

##przypisujemy przepustowosc dla routerow. Zaczynamy od 1, poniewaz musi byc co najmniej 1 router. Do liczby routerow jest dodane 1,
##poniewaz w przeciwnym razie by wykonywalo do liczby routerow-1
for router in range(1, number_of_routers + 1):
    routers.append(router)
    G.add_node(router)
    bandwidth = int(input("Bandwidth for %d router(mb/s): " % router))
    bandwidths.append(bandwidth)
    if (bandwidth <= 0):  ##jesli przepustowosc jest falszywa, konczymy program
        raise ValueError ("False parameters of bandwidth")
print("routers: ", routers)
print("bandwidths: ",bandwidths)

for station in range(1, number_of_stations + 1):
    stations.append(1) ##1, aby nie falszowac wyniku w dalszej czesci programu
    G.add_node(station)
print("stations: ",stations)

##wszystkie mozliwosci przepustowosci dla stanowisk wynikajace z regul prawdopodobienstwa
bandwidth_for_station = [bandwidth * station for bandwidth in bandwidths for station in stations]

for i in range (len(bandwidth_for_station)):
    distance = int(input("Distance %d is(m): " % (i + 1)))
    T = int(input("Time(s) %d is: " % (i + 1)))
    if (T>0 and distance>0):
        distances.append(distance)
        Times.append(T)
    else:
       print("Distance/Time cannot be equal 0. Your router is broken probably :(")
       ##wstawiamy duza liczbe,aby program nie bral tego pod uwage przy wyborze najkrotszej sciezki
       ##POMYSLEC Z TYM ATOI, JAK STARCZY MI CZASU!
       str(distances.append(100000000000000000))
       str(Times.append(1000000000000000000000))
##umowna waga,ktora bierze pod uwage wszystkie czynniki
matrix = [[0 for x in range(number_of_stations)] for x in range(number_of_routers)]
weight= [bandwidth_for_station[k]*distances[k]*Times[k] for k in range(len(bandwidth_for_station))]
for i in range (len(weight)):
    G.add_weighted_edges_from(stations[i],routers[i],weight[i])
for i in range(number_of_routers):
    for j in range(number_of_stations):
        for weights in weight:
            matrix[i][j]=weight.get(weights)
            break

Weight_in_matr=np.mat(weight)
final_matrix=Weight_in_matr.reshape((len(stations)),(len(routers)))
print("bandwidths (final): ", bandwidth_for_station) ##ostateczna macierz, ktora bedzie poddana alg. Dijkstry
print("Distances: ",distances)
print("Times: ",Times)
print("Weight: ",weight)
print("Weight: ",matrix)
print("Final matrix:\n", final_matrix)


##dijkstra(final_matrix,number_of_stations,number_of_routers)