import random
from math import sqrt
from arbre import Arbre

random.seed(42)

points = []

for i in range(3):
    points.append({i+1:[random.randrange(5000),random.randrange(5000)]})


#print(points)

racine = Arbre({0:[0,0]})

def add_etage(arbre:Arbre,enfants:list):
    for item in enfants:
        newArbre = Arbre(item)
        arbre.add_kid(newArbre)
        newPoints = enfants.copy()
        newPoints.remove(item)
        if len(newPoints) > 0:
            add_etage(newArbre,newPoints)

add_etage(racine,points)

list_path = racine.get_path()
print(list_path)
list_distance = []
for item in racine.get_path():
    distance = 0
    tempo = []
    for point in item:
        coord = []
        for key,value in point.items():
            coord = value
            
        if len(tempo) > 0:
            distance += sqrt((coord[0]-tempo[0])**2 + (coord[1]-tempo[1])**2)
        tempo = coord
    list_distance.append(distance)
    print(item)
print(min(list_distance))
print(list_distance.index(min(list_distance)))
print(list_distance)
print(list_path[list_distance.index(min(list_distance))])