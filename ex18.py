ADN_ColoMoutarde = "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC"
ADN_MlleRose = "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"
ADN_MmePervenche = "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC"
ADN_MLeblanc = "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"

Segment_coupable_A = "CATA"
Segment_coupable_B = "ATGC"

ADN = "attente de valeur"
SansCATA = "attente de valeur"

selection = 0
# fonction poour analyse
def analyse(adn):
    if Segment_coupable_A in adn:
        # retrai du segment si ca match
        SansCATA = (adn.replace("CATA", "XXXX"))
        if Segment_coupable_B in SansCATA:
            print("Cette personne est la couplable, les deux segments correspondent !")
            print("")
        else:
            print("cela ne correspond pas")
            print("")
    else:
        print("cela ne correspond pas")
        print("")

    return

print("ADN analyser")
print("Chargement de  la base de données avec les ADNs des suspects")
print("Chargement des traces ADNs")

#Selecteur de choix

while selection != "9":
    selection = 0

    print("Quel ADN souhaitez-vous analyser ?")
    print("1 pour Colonel Moutarde")
    print("2 pour Mlle Rose")
    print("3 pour Mme Pervenche")
    print("4 pour M Leblanc")
    print("9 pour quitter l'utilitaire d'analyse")
    selection = input("Quel est votre choix ?  ")
    print("")


    if selection == "1" :
        ADN = ADN_ColoMoutarde
        analyse(ADN)

    elif selection == "2" :
        ADN = ADN_MlleRose
        analyse(ADN)

    elif selection == "3" :
        ADN = ADN_MmePervenche
        analyse(ADN)

    elif selection == "4" :
        AND = ADN_MmePervenche
        analyse(ADN)

    elif selection == "9" :
        print("fermeture de l'utilitaire")

    else :
        print("votre choix n'est pas dans la selection, merci de bien faire attention aux choix disponible")
