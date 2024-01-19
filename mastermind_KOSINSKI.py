import random

#Partie 1

#Fonction retourant la combinaison de couleur secrète au joueur choisit aléatoirement par l'ordinateur 
def code_secret():
    couleur=["gris","blanc","rose","orange","vert","bleu","rouge","jaune"] 
    combinaison=[] #initialisation de "combinaison" vide 
    n=1
    while n<5 : #remplissage de "combinaison" de 4 couleurs tirées aléatoirement 
        x=random.choice(couleur)
        combinaison.append(x) 
        n=n+1
    return combinaison  

#Procédure qui indique au joueur les possibilités de couleur du jeu 
def menu():
    print("Propositions de couleurs :")
    print("1-Rouge")
    print("2-Jaune")
    print("3-Bleu")
    print("4-Orange")
    print("5-Vert")
    print("6-Rose")
    print("7-Gris")
    print("8-Blanc")
       
#Fonction qui transforme la valeur réel(integer) entrée par l'utilisateur, suite 
#        aux propositions du menu, en couleurs(string) correspondante                     
def traduction_menu(x):
    if x==1 :
        x="rouge"
    elif x==2 :
        x="jaune"
    elif x==3 :
        x="bleu"
    elif x==4 :
        x="orange"
    elif x==5 :
        x="vert"
    elif x==6 :
        x="rose"
    elif x==7 :
        x="gris"
    elif x==8 :
        x="blanc"
    else :
        x=int(input("Entrer un nombre correspondant à une couleur PARMIS les propositions du menu "))
    return x

#Fonction qui renvoit la combinaison  de 4 couleurs proposée par le professeur  
#  utilisée uniquement pour tester le bon fonctionnement du programme
#  notamment pour jouer avec les différents cas possible
def code_secret_professeur():
    combinaison=[] #comme pour combinaison, on va remplir un tableau vide avec des couleurs choisit
    code_professeur = list(map(int, input("Enter une combinaison de 4 chiffres correspondant aux couleurs du menu : ").split()))
    if len(code_professeur) != 4 :
        print("Il semble qu'il y ai une petite erreur, faites un effort !")
        code_professeur = list(map(int, input("Enter une combinaison de 4 chiffres correspondant aux couleurs du menu : ").split()))
    for i in range(0,len(code_professeur)) :
        traduction_menu(code_professeur[i])
        x=traduction_menu(code_professeur[i])
        combinaison.append(x)
    return combinaison
      

#Fonction qui renvoit la combinaison  de 4 couleurs proposée par le joueur 
def code_joueur():
    proposition=[] #comme pour combinaison, on va remplir un tableau vide avec des couleurs choisit
    code_utilisateur = list(map(int,input("Enter une combinaison de 4 chiffres correspondant aux couleurs du menu : ").split()))
    if len(code_utilisateur) != 4 :
        print("Il semble qu'il y ai une petite erreur, faites un effort !")
        code_utilisateur = list(map(int, input("Enter une combinaison de 4 chiffres correspondant aux couleurs du menu : ").split()))
    for i in range(0,len(code_utilisateur)) :
        traduction_menu(code_utilisateur[i])
        x=traduction_menu(code_utilisateur[i])
        proposition.append(x)
    return proposition 
   
#Procédure qui renvoie après avoir balayé les 2 combinaisons (ordi et joueur),
#   si il y en a, le nombre de couleur que les 2 listes ont en commun  et
#   si il y en a, le nombre de couleur placées au même endroit dans les listes 
def comparaison(combinaison,proposition):
    position=0
    couleur=0
    c=0
    p=0
    existe="violet" #si une couleur existe pour pas la recompter dans "bonnes couleurs"
    while c<=len(combinaison)-1:
        while p<=len(proposition)-1:
            if combinaison[c]==proposition[p]:
                if c==p:
                    position=position+1
                if existe!=proposition[p]:
                    couleur=couleur+1
                    existe=proposition[p]
            p=p+1
        p=0
        c=c+1 
    c=0 # on remet les compteurs à  0 
    return [couleur, position]
        
#Procedure affichant le nombre de couleurs correctes et les nombres d'elements bien placees
def resultat(coul_pos):
    print("il y a ",coul_pos[0]," couleur(s) correcte(s)")
    print("il y a ",coul_pos[1]," élément(s) bien placé(s)")
    
#Fonction qui garde en mémoire les différentes combinaisons proposées par l'utilisateur, 
#  pour lui rappeler ce qu'il a déjà joué. 
def rappel(memoire,proposition) :
    memoire.append(proposition)
    return memoire

#Procedure qui tant que la variable position est differente de 4, i.e. le joueur n'a pas la 
#  combinaison correcte, rejoue : redemande une composition au joueur + compare cette nouvelle 
#  combinaison à celle proposée par l'ordinateur. 
#Destinée au mastermind_tricheur() car le joueur a accès au code dit secret fixé par l'ordinateur
def test_combinaison_correcte1(position, combinaison, proposition, memoire):
    coups=1
    while position!=4 : 
        print()
        menu()
        print()
        print("vous avez deja joué : ",memoire)
        coups=coups+1
        proposition=code_joueur()
        print("le code secret est ",combinaison)
        print("vous proposez :",proposition)
        comparaison(combinaison,proposition)
        coul_pos=comparaison(combinaison,proposition)
        resultat(coul_pos)  
        position=coul_pos[1]
        rappel(memoire,proposition)
    print("Gagne en ", coups," coups!")  

#Procedure qui tant que la variable position est differente de 4, i.e. le joueur n'a pas la 
#  combinaison correcte, rejoue : redemande une composition au joueur + compare cette nouvelle 
#  combinaison à celle proposée par l'ordinateur   
#Destinée au mastermind() classique, le code secret n'est pas visible   
#Plusieurs niveau de jeu : DEBUTANT, INTERMEDIAIRE, EXPERT
#Niv DEBUTANT : 18 coups possible pour trouver le code secret et remporter la partie
def test_combinaison_correcte2_debutant(position, combinaison, proposition, memoire):
    coups=1
    while position!=4 and coups < 18: 
        print()
        menu()
        print()
        print("vous avez deja joué : ",memoire)
        coups=coups+1 
        proposition=code_joueur()
        #print("le code secret est ",combinaison)
        print("vous proposez :",proposition)
        comparaison(combinaison,proposition)
        coul_pos=comparaison(combinaison,proposition)
        resultat(coul_pos) 
        print()
        position=coul_pos[1]
        rappel(memoire,proposition)
    if position==4 and coups<=18 :
        print("Gagne en ", coups," coups!")  
    elif position!=4 and coups==18 :
        print()
        print("Perdu!!")
        print("Ne baissez pas les bras! Il faut savoir que les bonnes choses prennent du temps...") 
        print("Nous attendons votre revanche!")
        print()
        print()

#Niv INTERMEDIAIRE : plus que 12 coups possible pour trouver le code secret et remporter la partie    
def test_combinaison_correcte2_intermediaire(position, combinaison, proposition, memoire):
    coups=1
    while position!=4 and coups < 12: 
        print()
        menu()
        print()
        print("vous avez deja joué : ",memoire)
        coups=coups+1
        proposition=code_joueur()
        #print("le code secret est ",combinaison)
        print("vous proposez :",proposition)
        comparaison(combinaison,proposition)
        coul_pos=comparaison(combinaison,proposition)
        resultat(coul_pos) 
        print()
        position=coul_pos[1]
        rappel(memoire,proposition)
    if position==4 and coups<=12 :
        print("Gagne en ", coups," coups!")   
    elif position!=4 and coups==12 :
        print()
        print("Perdu!!")
        print("Aïe, peut être trop ambicieux, essayer un niveau débutant...")  
        print("Nous attendons votre revanche!")
        print()
        print()

#Niv EXPERT : seulement 2 coups possible pour trouver le code secret et remporter la partie    
def test_combinaison_correcte2_expert(position, combinaison, proposition, memoire):
    coups=1
    while position!=4 and coups<2: 
        print()
        menu()
        print()
        print("vous avez deja joué : ",memoire)
        coups=coups+1
        proposition=code_joueur()
        #print("le code secret est ",combinaison)
        print("vous proposez :",proposition)
        comparaison(combinaison,proposition)
        coul_pos=comparaison(combinaison,proposition)
        resultat(coul_pos) 
        print()
        position=coul_pos[1]
        rappel(memoire,proposition)
    if position==4 and coups<=2 :
        print("Gagne en ", coups," coups!")  
    elif position!=4 and coups==2 :
        print()
        print("Perdu!!")
        print("Aïe, peut être trop ambicieux, essayer un niveau intermédiaire...")
        print("Nous attendons votre revanche!")
        print()
        print()

#Procedure qui tant que la variable position est differente de 4, i.e. le joueur n'a pas la 
#  combinaison correcte, rejoue : redemande une composition au joueur + compare cette nouvelle 
#  combinaison à celle proposée par le professeur 
#Destinée au mastermind_special_professeur() 
def test_combinaison_correcte3(position, combinaison, proposition, memoire):
    coups=1
    while position!=4 : 
        print()
        menu()
        print()
        print("vous avez deja joué : ",memoire)
        coups=coups+1
        proposition=code_joueur()
        print("le code secret est ",combinaison)
        print("vous proposez :",proposition)
        comparaison(combinaison,proposition)
        coul_pos=comparaison(combinaison,proposition)
        resultat(coul_pos) 
        position=coul_pos[1]
        rappel(memoire,proposition)
    print("Gagne en ", coups," coups!")  
    
#Le jeu version mauvais joueur, vous avez accès au code secret choisit par l'ordinateur 
def mastermind_tricheur(): 
    memoire=[]
    menu() 
    combinaison=code_secret()
    proposition=code_joueur()
    print("le code secret (ou presque...) est : ",combinaison)
    print("vous proposez :",proposition)
    memoire=rappel(memoire, proposition)
    comparaison(combinaison,proposition)
    coul_pos=comparaison(combinaison,proposition)
    resultat(coul_pos)
    position=coul_pos[1]
    test_combinaison_correcte1(position,combinaison,proposition, memoire)    
        
#Le jeu, le vrai! Nous avons pensez à tous le monde, à tout les niveaux 
#Pour les débutants
def mastermind_debutant(): 
    memoire=[]
    menu() 
    combinaison=code_secret()
    proposition=code_joueur()
    #print("le code secret (ou presque...) est : ",combinaison)
    print("vous proposez :",proposition)
    memoire=rappel(memoire, proposition)
    comparaison(combinaison,proposition)
    coul_pos=comparaison(combinaison,proposition) 
    resultat(coul_pos)
    position=coul_pos[1]
    test_combinaison_correcte2_debutant(position,combinaison,proposition,memoire) 

#Pour les intermédiaires    
def mastermind_intermediaire(): 
    memoire=[]
    menu() 
    combinaison=code_secret()
    proposition=code_joueur()
    #print("le code secret (ou presque...) est : ",combinaison)
    print("vous proposez :",proposition)
    memoire=rappel(memoire, proposition)
    comparaison(combinaison,proposition)
    coul_pos=comparaison(combinaison,proposition) 
    resultat(coul_pos)
    position=coul_pos[1]
    test_combinaison_correcte2_intermediaire(position,combinaison,proposition,memoire) 

#Pour les génies    
def mastermind_expert(): 
    memoire=[]
    menu() 
    combinaison=code_secret()
    proposition=code_joueur()
    #print("le code secret (ou presque...) est : ",combinaison)
    print("vous proposez :",proposition)
    memoire=rappel(memoire, proposition)
    comparaison(combinaison,proposition)
    coul_pos=comparaison(combinaison,proposition) 
    resultat(coul_pos)
    position=coul_pos[1]
    test_combinaison_correcte2_expert(position,combinaison,proposition,memoire) 

#Parce que vous nous l'avez demandé    
def mastermind_special_professeur():
    memoire=[]
    menu() 
    print()
    print("Commencez par le code secret (plus tellement secret)")
    combinaison=code_secret_professeur()
    print("le code secret est : ",combinaison)
    print()
    print("Au tour du joueur de tenter sa chance") 
    proposition=code_joueur()
    print("vous proposez :",proposition)
    memoire=rappel(memoire, proposition)
    comparaison(combinaison,proposition) 
    coul_pos=comparaison(combinaison,proposition)
    resultat(coul_pos)
    position=coul_pos[1]
    test_combinaison_correcte3(position,combinaison,proposition,memoire)  
    
#Procédure proposant au joueur les différents mode de jeu coder ci dessus
def menu_mode_de_jeu():
    print("Il y a trois mode de jeu proposé, les voici :")
    print()
    print("1-Le mastermind tricheur : suit les règles du jeu classique à la différence près que le joueur a accès au code secret choisit par l'ordinateur ")
    print()
    print("2-Le mastermind classique")
    print()
    print("3-Le mastermind special professeur : conçu specialement pour vous, pour défier notre code c'est à dire chercher, non pas trouver car il n'y en a pas, ces failles ")
    print()
    print("Si vous ne souhaiter pas jouer il vous suffit d'entrer n'importe quel autre nombre")

#Procédure indiquant les niveaux de jeu i.e. EXPERT, INTERMEDIAIRE, DEBUTANT, la différence 
# réside dans le nombre de coups limitant la partie 
# je contraint le nv expert à 2 coups pour montrer ce qu'il se passe : le programme s'arrête bien
def menu_niveau():
    print("Trois niveau de jeu dans cette version, les voici :")
    print()
    print("1-Si vous êtes expert dans le domaine, limité à 2 coups")
    print()
    print("2-Pour les bons mais pas expert, limité à 12 coups") 
    print()
    print("3-Vous commencez ? Voici LA version pour vous, limité à 18 coups")

#Fonction qui en fonction de l'indication de l'utilisateur sur son niveau de jeu 
# lance un mode de jeu plus ou moins compliqué i.e. le nombres de coups est +/- limité
def niveau(niv) :
    if niv==1 :
        print()
        print("Bienvenue dans le mode expert, vous avez 2 coups, bonne partie")
        print()
        mastermind_expert()
    elif niv==2 :
        print()
        print("Bienvenue dans le mode intermédiaire, vous avez 12 coups, bonne partie")
        print()
        mastermind_intermediaire()
    elif niv==3 :
        print()
        print("Bienvenue dans le mode débutant, vous avez 18 coups, bonne partie")
        print()
        mastermind_debutant()
    else :
        print("Je ne comprend votre choix, même si vous êtes un genie il vous faut choisir un mode existant...")
        niv=int(input("1, 2 ou 3 ? "))

#Procédure lançant le jeu avec le mode choisit par l'utilisateur
def mode_de_jeu(choix):
    if choix==1 :
        print()
        print("Nous voilà parti pour un mastermind tricheur")
        print()
        mastermind_tricheur()
    elif choix==2 :
        print()
        print("Choix judicieux, un classique, amusez vous bien")
        menu_niveau()
        niv=int(input("Choisissez un niveau vous correspondant : "))
        print()
        niveau(niv) 
    elif choix==3 :
        print()
        print("Presomptueux de votre part, j'en connais pas beaucoup qui préfèrent jouer contre eux mêmes...")
        print()
        mastermind_special_professeur()
    else :  
        print("Je comprend, vous vous dégonflez... Bonne journée alors")
        parties()
        
        
#----------PARTIE2--------------

#Partie 2 

#Fonction qui vérifie que les entiers renseignés sont compris entre 1 et 8
# Gestion d'erreur
def erreur(couleurs):
  valide=True
  for couleur in couleurs :
    if couleur not in range(1,9) :
      valide = False
  return(valide)

#Fonction qui retourne le code secret entrée par le joueur :
# l'utilisateur entre des chiffres correspondant à des couleurs en se basant sur le menu
# ces chiffres sont ensuite traduit en couleur
# une liset ede 4 couleurs est renvoyée : le fameux code secret
def code_secret_utilisateur():
        menu()
        secret=[]    
        couleur=str(input("Choisissez 4 couleurs du menu "))
        valide = False
        while valide == False :
          # Vérifie que l'entrée est composée de 4 chiffres
          if couleur.isdigit() and len(couleur)== 4 :
            couleurs = [int(i) for i in couleur]
            # Vérifie que les chiffres sont entre 1 et 8
            if erreur(couleurs):
              valide = True
            else :
                couleur=str(input("Erreur, Choisissez 4 couleurs du menu "))
          else :
              couleur=str(input("Erreur, Choisissez 4 couleurs du menu "))
        code=[int(couleur[0]),int(couleur[1]),int(couleur[2]),int(couleur[3])]
        for i in code:
            if i==1 :
                i = "Rouge"
                secret.append(i)
            if i==2 :
                i = "Jaune"
                secret.append(i)
            if i==3 :
                i ="Bleu"
                secret.append(i)
            if i==4 :
                i = "Orange"
                secret.append(i)
            if i==5 :
                i ="Vert"
                secret.append(i)
            if i==6 :
                i ="Rose"
                secret.append(i)
            if i==7 :
                i ="Gris"
                secret.append(i)
            if i==8 :
                i ="Blanc"
                secret.append(i)
        return secret
   
def combinaison_alea():
    couleur=["Gris","Blanc","Rose","Orange","Vert","Bleu","Rouge","Jaune"]
    combinaison=[] #initialisation de "combinaison" vide
    n=1
    while n<5 : #remplissage de "combinaison" de 4 couleurs tirées aléatoirement
        x=random.choice(couleur)
        combinaison.append(x)
        n=n+1
    return combinaison  
   
# Cette fonction va gérer une mémoire qui vient stocker les couleurs présentent dans le code secret
# L'ordinateur va proposé 8 combinaisons, chacune d'elle sera composé de 4 couleurs identique
# Une fois les couleurs présentent dans le code secret trouvée, on vient les placer dans une matrice
#  que cette fonction nous retourne
def couleurs_secretes(combinaison):
    memoire=[]
    couleurs=["Rouge","Jaune","Bleu","Orange","Vert","Rose","Gris","Blanc"]
    for c in couleurs:
        proposition =[c,c,c,c]
        print(proposition)
        coul_bien_place=comparaison_part2(combinaison,proposition)
        if coul_bien_place>0:
            for i in range (coul_bien_place):
                memoire.append(c)
    return memoire

#Cette fonction reprend le même principe que couleurs_secretes mais s'arrête dès que la mémoire contient 4 couleurs.
#Comme le nombre de coups varie pour cette fonction, elle retourne aussi le nombre de coups utilisés
def couleurs_secretes_efficaces(combinaison):
    coups = 0
    memoire=[]
    couleurs=["Rouge","Jaune","Bleu","Orange","Vert","Rose","Gris ","Blanc"]
    i = 0
    while len(memoire) < 4:
      c = couleurs[i] 
      proposition =[c,c,c,c]
      print(proposition)
      coul_bien_place=comparaison_part2(combinaison,proposition)
      coups += 1
      if coul_bien_place>0:
        for j in range (coul_bien_place):
            memoire.append(c)
      i+=1
    return memoire,coups
       
#Cette fonction renvoie des propositions tirées aléatoirement par l'ordinateur mais cette fois-ci
# les couleurs sont piochées dans la liste "memoire" qui a stockée les couleurs présentent
# dans le code secret, cela réduit considérablement le nombre de combinaison possible
def combinaison_couleurs_reduites(memoire):    
    proposition=[]
    n=1
    while n<5:
        x=random.choice(memoire)
        proposition.append(x)
        n=n+1
    return proposition

#Comme son nom l'indique cette fonction va comparer le code secret et la propositon de l'ordinateur
# elle retourne ensuite le nombre de couleurs bien placées
def comparaison_part2(secret,proposition):
    i=0
    coul_bien_place=0
    for i in range(4):
        if proposition[i]==secret[i]:
               coul_bien_place = coul_bien_place + 1
    return(coul_bien_place)

#Procédure qui determine la position des couleurs retenus i.e. celle présentent dans le code secret
# Utilisé dans l'heuristique efficace
# Cette fonction prend en entrée coups qui d épend de la fonction couleurs_secretes_efficaces
def position(coups,couleur,secret):
    inexistant=["Violet","Violet","Violet","Violet"]
    dechiffre=[0,0,0,0]
    indices_choisis = []
    for c in couleur[:3]:
      #On boucle sur les trois premières couleurs puisque la position de la quatrième couleur est déduite des 3 premières
      indices_restants = [i for i in range(4) if i not in indices_choisis]
      trouvé = False
      i = 0
      #Sur les n emplacements libres, on essaie les n-1 premiers.
      while trouvé == False and i< len(indices_restants)-1:
        coups = coups+1
        inexistant[indices_restants[i]] = c
        cbp = comparaison_part2(secret,inexistant)
        print (inexistant)
        inexistant = ["Violet","Violet","Violet","Violet"]
        if cbp == 1:
          trouvé = True
          dechiffre[indices_restants[i]] = c
          indices_choisis.append(indices_restants[i])
        i = i+1
      #Si la solution n'est pas parmi les n-1 premiers, alors c'est la nième.
      if i == len(indices_restants) -1 and trouvé == False:
        dechiffre[indices_restants[-1]] = c
        indices_choisis.append(indices_restants[-1])
   
    #L'emplacement de la dernière couleur est le dernier emplacement libre.
    dernier_indice = [i for i in range(4) if i not in indices_choisis]
    dechiffre[dernier_indice[0]] = couleur[3]
    print("Le code secret est donc : ",dechiffre)
    print("Trouvé en ",coups," coups")    


#Cette procédure invite l'ordinateur à rejouer une proposiion tant qu'il ne trouve pas
# le code secret, une fois ce dernier trouver elle nous renvoit le nombre de coups
# qu'il lui aura fallu
#Destiné à l'heuristique aleatoire
def test_combinaison_correcte_alea(secret,cbp):
    coups=1
    while cbp<4 :
        coups=coups+1
        combinaison=combinaison_alea() 
        cbp=comparaison_part2(secret,combinaison)
    print("Trouvé en ",coups," coups")

#Cette procédure est identique à celle au dessus à la différence près que l'ordi pioche aléatoirement
# mais dans une liste de maximum 4 couleurs (en effet il peut y avoir plusieurs couleurs identique dans
# le code secret)   & nbsp;
#Destiné à l'heuristique pas_completement_aleatoire
def test_combinaison_correcte_pas_completement_alea(secret,cbp,couleur) :
    coups=8
    while cbp<4 :
        coups=coups+1
        proposition=combinaison_couleurs_reduites(couleur)
        print("La proposition est :", proposition)
        cbp=comparaison_part2(secret,proposition)
    print("Trouvé en ",coups," coups")
       
#Heuristique 1 : l'aléatoire, l'ordinateur tire des combinasions aléatoirement dans la liste des
# 8 couleurs du jeu
def aleatoire():
    secret=code_secret_utilisateur()
    print("Le code secret est donc : ",secret)
    print()
    combinaison=combinaison_alea()
    print("L'ordinateur propose dans un premier temps :",combinaison)
    cbp=comparaison_part2(secret,combinaison)
    test_combinaison_correcte_alea(secret,cbp)

#Heuristique 2 : l'ordinateur determine dans un premier temps les couleurs presentent dans le code secret
# suite à cela, il tire aleatoirement des combinaisons seulement composé des couleurs secretes    
def pas_completement_aleatoire():
    secret=code_secret_utilisateur()
    print("Le code secret est donc : ",secret)
    print()
    couleur=couleurs_secretes(secret)
    print()
    print("Les couleurs présentent dans le code secret semblent être :",couleur)
    print()
    proposition=combinaison_couleurs_reduites(couleur)
    cbp=comparaison_part2(secret,proposition)
    test_combinaison_correcte_pas_completement_alea(secret,cbp,couleur)

#Heuristique 3 : tres efficace, elle reprend comme ci-dessus l es couleurs présentent dans le code secret
# puis les comparent une à une au code secret, une fois la position de la couleur trouvé on remplit une
# matrice avec les couleurs positionné au bon endroit
def efficace():
    secret=code_secret_utilisateur()
    print("Le code secret est donc : ",secret)
    print()
    couleur,coups=couleurs_secretes_efficaces(secret)
    print()
    print("Les couleurs présentent dans le code secret semblent être :",couleur)
    print()
    position(coups,couleur,secret)

#Procédure qui affiche les differentes heuristiques (3 au total)
def menu_heuristique():
    print("Il y a trois heuristique proposées, les voici :")
    print()
    print("1-Aléatoire, vous fixez un code secret, l'ordinateur propose aléatoirement des combinaisons, en  moyenne 4096 coups")
    print()
    print("2-Pas tout à fait aléatoire, même principe que l'heuristique 1 mais l'ordi determine les couleurs du code secret puis tire aléatoirement des combinaisons composé de ces couleurs, en moyenne 206 coups")
    print()
    print("3-Efficace, trouve les couleurs du code secret puis determine leur position, en moyenne 12 coups ")
    print()
    print("Si vous ne souhaiter pas jouer il vous suffit d'entrer n'importe quel autre nombre")

#Procedure qui lance l'heuristique choisit par l'utilisateur    
def mode_de_jeu_part2(choix):
    if choix==1 :
        print()
        print("Nous voilà parti pour le mode aléatoire")
        print()
        aleatoire()
    elif choix==2 :
        print()
        print("En avant pour cette heuristique")
        print()
        pas_completement_aleatoire()
    elif choix==3 :
        print()
        print("Vous êtes pressé ? Bon choix, allons-y")
        print()
        efficace()
    else :
        print("Quel dommage... Bonne journée, en espérant vous revoir bientôt")
        parties()

#Procédure qui lance la partie 1, suite au choix du joueur         
def partie1() :
    menu_mode_de_jeu() 
    choix=int(input("Entrer le chiffre correpondant à votre choix de mode de jeu "))
    mode_de_jeu(choix)
    while choix==3 or choix==2 or choix==1 :
        print()
        print("Revanche ??")
        print()
        menu_mode_de_jeu()
        choix=int(input("Entrer le chiffre correpondant à votre choix de mode de jeu "))
        mode_de_jeu(choix)

#Procédure qui lance la partie 2, suite au choix du joueur 
def partie2() :
    print()
    menu_heuristique()
    print()
    choix=int(input("Entrer un nombre "))
    mode_de_jeu_part2(choix)
    while choix==3 or choix==2 or choix==1 :
        print()
        print("On rejoue ?")
        print()
        menu_heuristique()
        choix=int(input("Entrer le chiffre correpondant à votre choix d'heuristique ")) 
        mode_de_jeu_part2(choix)

#Procédure qui demande au joueur de choisir entre la partie1 et la partie2 :
#Partie 1 : ordinateur fixe code secret => joueur chercher le code 
#Partie 2 : joueur fixe code secret => ordinateur cherche le code 
def parties() :
    print("Bienvenue dans notre mastermind, celui-ci est composé de deux parties :")
    print("1 - La partie 1, propose un jeu tel que vous, joueur essayer de trouver le code secret émit par l'ordinateur") 
    print("2 - La partie 2 quant à elle, vous propose de fixer un code secret, l'ordinateur doit le trouver")
    print()
    partie=int(input("Que voulez-vous jouer ? 1 ou 2 ? "))
    if partie==1 :
        print("PARTIE 1 ")
        partie1()
    elif partie==2 :
        print("PARTIE 2 ")
        partie2()
    else :
        print("Attention ! 1 ou 2 ")
        partie=int(input("Que voulez-vous jouer ? 1 ou 2 ? "))

#TEST
parties()


