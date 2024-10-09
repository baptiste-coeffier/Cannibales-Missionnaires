# classe permettant de construire un arbre pour remonter de la solution à l'état initial
class Arbre:
    def __init__(self, n, p):
        self.Etat = n
        self.fils = []
        self.parent = p

    # permet de créer de nouveaux noeuds/feuilles 
    def ajout_branche(self, n, p):
        self.fils.append(Arbre(n, p))
    
    # différente méthode permettant de recupérer facilement les valeurs 
    def get_valeur(self): 
        return self.Etat
    
    def get_valeurBranche(self, i):
        return self.fils[i]
    
    def get_parent(self):
        return self.parent


# fonction permettant de vérifier si on est arriver à l'état du but
def but(tmpCg, tmpMg, bar):
    if tmpCg == 0 and tmpMg == 0 and bar == 'Droite':
        return True
    return False

# fonction verifiant si le nouvelle état ne viole pas les contraintes
def isvalid(tmpCg, tmpMg):
    # je récupère le nombre de missionnaire/cannibales à droite pour plus de faciliter
    tmpCd = n - tmpCg
    tmpMd = n - tmpMg
    # on regrade si on a pas dépasser les bornes de l'état
    if (tmpCg > n or tmpCg < 0 or tmpMg > n or tmpMg < 0):
        return False
    # on vérifie si on ne viole pas les contraintes
    elif (tmpCg > tmpMg and tmpMg > 0) or (tmpCd > tmpMd and tmpMd > 0):
        return False 
    return True

# fonction qui permet d'éliminer les états déjà explorer de la frontiere
def doublon():
    #on parcours tous les états de la frontière 
    for i in range(len(Frontiere)):
        # si on trouve un état de la frontiere dans explorer alors on le supprime de la frontiere
        if Frontiere[i] in Explorer:
            Frontiere.pop(i)
        i -= 1

def graphSearch():
    #on vérifie si on a un état dans la frontière, si non il n'y a pas de solution
    if Frontiere == [] :
        return False
    
    #on prends les valeurs du premier état de la file 
    Cg = Frontiere[0].get_valeur()[0]
    Mg = Frontiere[0].get_valeur()[1]
    bar = Frontiere[0].get_valeur()[2]
    
    # test pour savoir si on est arriver à la solution
    if but(Cg, Mg, bar): 
        return Frontiere[0]
        
    # loop de recherche
    i = p 
    while i>=1:
        a = 0 
        b = i 
        while (a<=i):
                
            # on test si l'état n'est pas déjà dans explorer 
            if([Cg+a, Mg+b, 'Gauche'] in Explorer) or ([Cg-a, Mg-b, 'Droite'] in Explorer) : 
               None
            # on différencie les cas où la barque est à Gauche ou à Droite
            elif(bar == 'Gauche') :
                # on test si on ne viole pas les contraintes
                if (isvalid(Cg-a, Mg-b)):
                    # on ajoute le nouvel état à la frontière 
                    Frontiere.append(Arbre([Cg-a, Mg-b, "Droite"], Frontiere[0]))
                    # on ajoute un fils au noeud que l'on est en train de toucher
                    Frontiere[0].ajout_branche([Cg-a, Mg-b, "Droite"], Frontiere[0])
            # on fait la même chose à droite
            elif(bar == 'Droite') :
                if (isvalid(Cg+a, Mg+b)):
                    Frontiere.append(Arbre([Cg+a, Mg+b, "Gauche"], Frontiere[0]))
                    Frontiere[0].ajout_branche([Cg+a, Mg+b, "Gauche"], Frontiere[0])
                    
            b = b-1
            a = a+1
        i = i-1

    # on ajoute l'état courant à explorer puis on le supprime de la frontiere 
    Explorer.append(Frontiere[0].get_valeur())
    Frontiere.pop(0)
    # on vérifie si des états de la frontière ne se trouve pas déjà dans Explorer 
    doublon()
    
    # on relance la fonction récursivement quand on a expanser le premier état de la frontière 
    return graphSearch()


def Chemin(s):
    deplacement = 0
    Phrase = f"Il y a {n - (s.get_valeur()[0])} Cannibale(s), {n - (s.get_valeur()[1])} Missionnaire(s) sur la rive Gauche et a barque à {p} places\n"
    Parent = s.get_parent()

    while Parent != None:
        cg = n - s.get_valeur()[0]
        mg = n - s.get_valeur()[1]
        # on va afficher le nombre qu'il reste sur la rive après chaque déplacement
        Phrase = Phrase + f"{deplacement}Il y a {n - cg} Cannibale(s) et {n - mg} Missionnaire(s) à Droite.\n"
        s = Parent
        Parent = s.get_parent()
        deplacement += 1
    print(Phrase)
    print(f"Il y a eu {deplacement} déplacements de la barque. \n")



# initialisation de la situation initial
n = int(input("Veuillez renseigner le nombre de Cannibales : "))
p = int(input("Ainsi que le nombre de place dans la barque: "))

nbMis = n
nbCan = n
barque = 'Gauche'

Etat_initial = [nbCan, nbMis, barque]

Frontiere = [Arbre(Etat_initial, None)]
Explorer = []

Solution = graphSearch()

# si graphsearch() renvoie false, alors il n'y a pas de solution, sinon on l'affiche
if (Solution == False):
    print("Il n'y a pas de solution")
else : 
    Chemin(Solution)
