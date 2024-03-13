import os
import sys
from random import randint

# Cette fonction fournit des informations générales sur le programme.
def presentation (): 
    print("\n" + 53*"=")  
    print( "= generateur-sequences.py")
    print("= Ce programme permet de générer un jeu de séquences")
    print ("= Auteure   : Nathalia Cruz (GOMN13318509)")
    print ("= Date      : Automme 2023")
    print ("= Version   : 01")
    print ("= Cours     : INF812")
    print(53*"=" + "\n")   

# Cette fonction définit les valeurs par défaut du programme. 
# Si l’utilisateur ne fournit pas les arguments de la ligne de commande, 
# les valeurs par défaut suivantes sont utilisées:
# - output.txt comme fichier de sortie, 
# - fasta comme format de fichier de sortie, 
# - génération de 10 séquences, 
# - séquences de taille 30,
# - espece comme nom de l’espèce
def initialisation ():
    outputfile = "output.txt" 
    tailleSequences = 30
    nbSequences = 10
    formatOutput = "fasta"
    nomEspece = "espece"

    return (outputfile, tailleSequences, nbSequences, formatOutput, nomEspece)

# Cette fonction reçoit une chaîne de caractères et la sépare en clé et en valeur.
def extraireArgument (argument):
    argument_list = argument.split ("=")
    key = argument_list[0]
    value = ""
    if len (argument_list)>1:
        value = argument_list[1]
    return (key,value)

# Cette fonction valide si le fichier spécifié existe déjà.
def valideOutputFile (nom_fichier):
    fichier_exists = os.path.exists (nom_fichier)
    if fichier_exists:
        quitterProgramme ("Le fichier ne doit pas exister : " + nom_fichier + " existe.")
    else:
        return nom_fichier

# Cette fonction valide si le argument informée est un nombre entier positif.     
def valideEntierPositif (chaine_value):
    if chaine_value.isdigit() == False:
        quitterProgramme ( "Option invalide : " + chaine_value + " n'est pas un entier.")  
    entier_value = int(chaine_value)
    if entier_value <=0:
        quitterProgramme ( "Option invalide : " + chaine_value + " n'est pas un entier positive.")    
    return entier_value

# Cette fonction valide si le format informée est fasta ou phylip.
def valideFormatOutfile (format):
    if format == "fasta" or format == "phylip":
        return format
    else:
        quitterProgramme ( "Option invalide : " + format + " n'est pas un format valide.")

# Cette fonction valide si la espece informée n'est pas un nombre ou vide.
def valideNomEspece (nom_espece):
    if nom_espece.isdigit() or len(nom_espece) == 0:
        quitterProgramme ( "Option invalide : " + nom_espece + " n'est pas un nom valide.") 
    return nom_espece

# Cette fonction fournit des options de la ligne de commande.
def help (): 
    print ("Liste des options de la ligne de commande :")
    print ("    -fichierSortie : nom du fichier de sortie. Le fichier ne doit pas exister. Si l’option n’est pas fournit le fichier par défaut sera output.txt.")
    print ("    -formatSortie : fasta ou phylip. Format du fichier de sortie.")
    print ("    -tailleSequences : entier. Taille des séquences")
    print ("    -nbSequences : entier. Nombre de séquences à générer")
    print ("    -nomEspece : chaine de caractère. Format du nom des espèces. Un compteur sera utilisé pour chaque séquence.")
    print ("    -aide : affichage de l’aide. Description des différentes options.")

# Cette fonction permet de générer un jeu aléatoire de séquence ADN.
def genererJeuSequences (tailleSequences, nbSequences): 
    dict_bases = {0:"A", 1: "T", 2: "C", 3:"G"}
    liste_sequences = []
    for index_seq in range(nbSequences):
        sequence = ""
        for index_taille in range (tailleSequences):
            base = randint(0,3)
            sequence = sequence + dict_bases[base]
        liste_sequences.append(sequence)
    return liste_sequences

# Cette fonction permet sauvegarder une liste de séquence ADN dans un fichier avec le format phylip ou fasta.
def sauvegarderSequences (liste_sequences, outputfile, formatOutput, nomEspece):
    fh = open(outputfile, "w")
    if formatOutput == "phylip":
        print (str(len(liste_sequences)) + " " + str(len(liste_sequences[0])), file = fh)
   
    for index in range (len(liste_sequences)):
        if formatOutput == "phylip":
            print (nomEspece + str(index+1) + " " + liste_sequences[index], file = fh)
        else:
            print ("> " + nomEspece + str(index+1) + "\n" + liste_sequences[index], file = fh)
    fh.close

# Cette fonction permet quitter le programme avec une message d'erreur.
def quitterProgramme (message_erreur):
    print(message_erreur)
    sys.exit()

