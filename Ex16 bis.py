boucle = 0

print("Calcul de distance de Hamming, attention il est nécessaire que les mots aient la meme longueur")


premier_mot = input("quel est le premier mot ? ")
deuxieme_mot = input("quel est le deuxieme mot ? ")

l_premier = len(premier_mot)
l_deuxieme = len(deuxieme_mot)

#=======================================================================================
#traitement du hammering
def superhamming(premier_mot, deuxieme_mot):
    total = 0
    boucle = 0
    analyse_hamming = "9"

    while boucle < l_premier :
        if premier_mot[boucle] == deuxieme_mot[boucle]:
            boucle += 1
            analyse_hamming = analyse_hamming + "1"
        else :
            boucle += 1
            analyse_hamming = analyse_hamming + "0"


    for i in analyse_hamming:
        if i == "0":
            total += 1
        else :
            pass
    return total
#=======================================================================================

#check si longueur same

if l_premier != l_deuxieme :
    print(" /!\ attention les mots ne possèdent pas la meme longueur /!\ ")
    exit(1)

#appel def + affichage resultat
hamming = superhamming(premier_mot, deuxieme_mot)
print("la distance de hamming est de : ", hamming)

