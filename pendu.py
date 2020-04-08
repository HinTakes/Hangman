#########################################################
# Jeu Pendu
# Date: 04/04/2020
# Createur : Takwa Daghbouj, 2683136
#########################################################

# Les imports
import random
import os

# Initialisation des variables:

dictionnaire = []   #cette variable va servir comme une liste de mots appellés à partir d'un fichier texte

tentatives= []  #cette variable stocke les reponses du joueur

caracteresTrouves = []  #cette variable va sauvegarder le progres du joueur tant qu'on essaie de deviner le mot

mot_cache = ""   #le mot caché à deviner



# Role    : Permet de tirer aléatoirement un mot de la liste.
# Param   : Rien
# Retour  : Un mot
def motCache(niveau):

    if niveau == 1:
        while True:
            mot_cache = dictionnaire[random.randint(0, len(dictionnaire))]
            # affectation d'un mot de la liste dictionnaire pr l'intermediaire d'un entier/rang aléatoire
            if len(mot_cache) <= 4 :
                break
            #le boucle se termine lorsque le mot choisit répond à la longeur de mot correspondante au niveau

    elif niveau == 2:
         #meme principe:
        while True:
            mot_cache = dictionnaire[random.randint(0, len(dictionnaire))]
            if len(mot_cache) <= 6 and len(mot_cache) > 4 :
                break

    elif niveau == 3:
         #meme principe
        while True:
            mot_cache = dictionnaire[random.randint(0, len(dictionnaire))]
            if len(mot_cache) > 6 :
                break

    return mot_cache


# Role    : Permet de saisir et retourner un caractere
# Param   : Rien
# Retour  : Un mot
def saisirCaractere():
    while True:
        caractere = str(input("Saisir un caractere: ")).upper()
        #saisie du caractere à vérifier, la fonction upper permet de faciliter la comparaison

        alphabet= ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z')

        if not caractere in alphabet:
            print("Saisissez une lettre de l'alphabet")
        # condition pour assurer la saisie d'un caractere valide

        elif caractere in tentatives:
            print("Caractere deja saisie!!")
        # condition pour éviter la répétiton des saisie

        else:
            return caractere



# Role    : Ajouter le caractere dans la liste des caracteres trouvés
# Param   : Caractere
# Retour  : Une chaine de caracteres representant l'affichage
def afficherCAr(caractere):
    global caracteresTrouves


    for i in range(len(mot_cache)):                     #ce boucle compare le caractére du param avec les lettres du mot caché puis :
    
        if caractere == mot_cache[i]:                   #   "dévoile" le caractere moyennant sa position dans mot_cache 
            caracteresTrouves[i] = caractere            #   en l'affectant à caracteresTrouves
    
    return caracteresTrouves


# Role    : Effacer lecran
# Param   : Rien
# Retour  : Rien
def effacerEcran():
    os.system('cls')


# Rôle   : Afficher le pendu selon le nombre d'erreurs commises.
# Param  : un entier representant le nombre d'erreurs.
# Retour : Aucun. Affichage de l'homme pondu.
def affichage(nbErr):
    if nbErr == 8:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |       |")
        print(" |      /|\\")
        print(" |       |")
        print(" |      / \\")
        print(" |       ")
        print("---       ")
    elif nbErr == 7:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |       |")
        print(" |      /|\\")
        print(" |       |")
        print(" |      / ")
        print(" |       ")
        print("---       ")
    elif nbErr == 6:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |       |")
        print(" |      /|\\")
        print(" |       |")
        print(" |       ")
        print(" |       ")
        print("---       ")
    elif nbErr == 5:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |       |")
        print(" |      /|\\")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("---       ")
    elif nbErr == 4:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |       |")
        print(" |      / \\")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("---       ")
    elif nbErr == 3:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |       |")
        print(" |      / ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("---       ")
    elif nbErr == 2:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |       |")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("---       ")
    elif nbErr == 1:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("---       ")
    else:
        print("  _______")
        print(" |       |")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("---       ")

# Rôle   : Choisir un niveau de difficulté
# Param  : rien
# Retour : un entier representant le niveau
def niveauDifficulte():
    niveau = 0

    while True:

        niveau = int(input("Veuillez choisir un niveau de difficulté (1 : Facile / 2 : Moyen / 3 : Difficile) : "))

        if niveau in [1,2,3] :
            return niveau
        else :
            print("Saisie incorrecte!!")
            
    #meme principe de saise: le boucle ne va retourner une valeur que lorsque ca tombe dans la plage des saisies permises
    
# Rôle   : Donner l'ption de rejouer ou quitter
# Param  : rien
# Retour : True ou False, selon le choix
def rejouer():
    global tentatives, caracteresTrouves, mot_cache
    while True:
        choix=input('Voulez vous rejouer? (O: Oui / N: Non):').upper()
        if choix in ["O", "N"]:
            break
    # saisie d'une réponse valide : oui ou non
    
    if choix == "N":            #Si le choix est non, la fonction va retourner un faux et s'arreter
        return False
    
    # Si le joueur choisit de recommencer:
    # On remet toutes les variables aux valeurs de départ:
    tentatives= []
    caracteresTrouves= []
    mot_cache = ""

    return True

# Rôle   : jouer
# Param  : rien
# Retour : corps du jeu
def jouer():

    global dictionnaire, caracteresTrouves, mot_cache

    with open("words.txt", "r") as f:
        dictionnaire = f.readlines()
    #la commande permet la lecture d'un 'dictionnaire' contenant tous les mots aléatoires possibles

    continuer = True

    while continuer:
        
        #Définition des élements du jeu:
        
            
        niveau = niveauDifficulte()
        #saisie d'un niveau de difficulté correct

        mot_cache = motCache(niveau).upper()
        #appel à la fonction de tirage de mot, upper permet de faciliter la comparaison

        for i in range(len(mot_cache)-1):
            caracteresTrouves.append("_")
        #rassembler le mot dévoilé caracteresTrouves dans son état vacant

        nbErr= 0
        caractere= ""

        while True:
            
            #affichage de l'interface de jeu:
            effacerEcran()                          

            print(caracteresTrouves)

            affichage(nbErr)

            if not "_" in caracteresTrouves:                            
                print("Bravo ! Vous avez trouvez le mot caché.")
                continuer = rejouer() #on assigne à cette varieble une valeur selon le choix du joueur de continuer ou pas
                break
                # le boucle s'arrete lorsque tous les caracteres de caracteresTrouves sont dévoilés/il existe plus d'espaces vacants à deviner
            
            if nbErr==8:
                print("Oh non! l'homme est pendu!")
                print("Le mot était ", mot_cache)
                continuer = rejouer()
                break
                #le boucle s'arrete lorsque le nombre d'erreurs permis est atteint

            print (tentatives)
            #affichage des tentatives essayés pour faciliter le jeu
            
            caractere = saisirCaractere()
            #saisie d'un caractere tant que le jeu n'est pas fini
            tentatives.append(caractere)
            #ajout de chaque tentatives à l'historique

            if caractere in mot_cache:                  #si la lettre choisit est dans le mot:
                afficherCAr(caractere)                  #   on affiche la lettre dans caractereTrouves
            
            else:                                       #sinon: il s'agit d'un tour perdu
                nbErr +=1



if __name__ == "__main__":
    jouer()
