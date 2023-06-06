class Arbre:

    def __init__(self,valeur) -> None:
        self.valeur = valeur
        self.enfants = []

    def add_kid(self,kid):
        self.enfants.append(kid)

    def be_leaf(self):
        return True if len(self.enfants) == 0 else False
    
    def parcours_profondeur(self):
        listEnfants = []
        if not(self.be_leaf()):
            for enfant in self.enfants:
                for elem in enfant.parcours_profondeur():
                    listEnfants.append(elem)
        listEnfants.append(self.valeur)
        return listEnfants
        
    def parcours_largeur(self,list=[]):
        listAttente = []
        list.append(self.valeur)
        if not(self.be_leaf()):
            listAttente = self.enfants
            for item in listAttente:
                list.append(item.valeur)
                if not(item.be_leaf()):
                    for enfant in item.enfants:
                        listAttente.append(enfant)
        return list
            

            

    


        



newArbre = Arbre(1)

newArbre.add_kid(Arbre(2))
newArbre.add_kid(Arbre(3))
newArbre.add_kid(Arbre(4))

nb = 5

for element in newArbre.enfants:
    element.add_kid(Arbre(nb))
    element.add_kid(Arbre(nb+1))
    nb += 2

for element in newArbre.enfants:
    for e in element.enfants:
        e.add_kid(Arbre(nb))
        e.add_kid(Arbre(nb+1))
        nb += 2

print(newArbre.parcours_profondeur())
print(newArbre.parcours_largeur())