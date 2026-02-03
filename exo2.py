FACTEURS = [1.30, 1.15, 1.05, 0.95, 0.95, 1.05, 1.15, 1.30]
personnes = []
try:
    for i in range(8):
        personnes.append(int(input(f"Veuillez entrer le nombre de personnes dans la section {i+1}: ")))
    presence_negatif = False
    for nombre in personnes:
        if nombre < 0: presence_negatif = True
    if presence_negatif == True:
        print("Erreur - donnees invalides.")
    else:
        intensites = []
        for i in range(8):
            intensites.append(personnes[i]*FACTEURS[i])
        maxI = max(intensites)
        niveaux = []
        if maxI == 0: niveaux = [0]*8
        else:
            for i in range(8):
                niveaux.append(int((intensites[i]/maxI)*10 + 0.5))
        for i in range(10):
            print(f"{str(10-i) :>2} | ", end= "")
            for j in range(8):
                if niveaux[j] >= 10-i:
                    print("❚ ", end="")
                else: print(". ", end="")
            print()
        print("     A B C D E F G H\n")
except ValueError:
    print("Erreur - donnees invalides.")