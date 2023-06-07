class Arbre:

    def __init__(self,valeur) -> None:
        self.valeur = valeur
        self.enfants = []

    def add_kid(self,kid):
        self.enfants.append(kid)

    def is_leaf(self):
        return True if len(self.enfants) == 0 else False
    
    def parcours_profondeur(self):
        listEnfants = []
        if not(self.is_leaf()):
            for enfant in self.enfants:
                for elem in enfant.parcours_profondeur():
                    listEnfants.append(elem)
        listEnfants.append(self.valeur)
        return listEnfants
        
    def parcours_largeur(self,list=[]):
        listAttente = []
        list.append(self.valeur)
        if not(self.is_leaf()):
            listAttente = self.enfants
            for item in listAttente:
                list.append(item.valeur)
                if not(item.is_leaf()):
                    for enfant in item.enfants:
                        listAttente.append(enfant)
        return list
            
    def get_depth(self):
        if self.is_leaf():
            return 1
        liste_profondeur = [child.get_depth() for child in self.enfants]
        return max(liste_profondeur) + 1
    
    def loop(self,liste):
        new_list = []
        loop = False
        for item in liste:
            if type(item) == list:
                new_list = new_list + item
                loop = True
            else:
                new_list.append(item)
        return self.loop(new_list) if loop else new_list


    
    def get_path(self):
        list_path = [self.valeur]
        if not(self.is_leaf()):
            new_list_path = []
            for enfant in self.enfants:
                retour_child = enfant.get_path()
                if len(retour_child) > 1:
                    for item in retour_child:
                        if type(item) == list and len(item) > 1:
                            new_list_path.append(list_path.copy() + self.loop(item))
                        else:
                            new_list_path.append(list_path.copy() + item)
                else:
                    new_list_path.append(list_path.copy() + retour_child)
            return new_list_path    
        return list_path


    


        



#newArbre = Arbre(1)
#
#newArbre.add_kid(Arbre(2))
#newArbre.add_kid(Arbre(3))
#newArbre.add_kid(Arbre(4))
#
#nb = 5
#
#for element in newArbre.enfants:
#    element.add_kid(Arbre(nb))
#    element.add_kid(Arbre(nb+1))
#    nb += 2
#
#for element in newArbre.enfants:
#    for e in element.enfants:
#        e.add_kid(Arbre(nb))
#        e.add_kid(Arbre(nb+1))
#        nb += 2
#
#print(newArbre.parcours_profondeur())
#print(newArbre.parcours_largeur())