mot_toocheck = input("taper le mots a vérifier")
check = 0

def checkpala(mot_toocheck):
    palindrome = 1
    longueur = len(mot_toocheck)
    #alignement des caracteres
    longueur -= 1
        # pour chaqu'une des lettres
    for i in mot_toocheck:
        #faire vérif en fonction de la boucle et de longueur -1
        if i == mot_toocheck[longueur]:
            longueur -= 1
        else:
            print("le mot n'est pas un palindrome")
            exit(1)
    return palindrome

check = checkpala(mot_toocheck)
print("le mot est un palindrome")
