# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets (gabarit)
"""
Objectif :
- DEMANDER : n (int) et statut etudiant (O/N)
- Options :
    24 billets : 66.00$
    12 billets : 36.00$
     5 billets : 15.75$
     1 billet  :  3.60$
- Reduction : si etudiant = O, appliquer 12% de reduction sur le cout des forfaits uniquement.
  Les billets unitaires ne sont pas reduits.

But :
- Acheter au moins n billets
- Minimiser le prix total
- En cas d'egalite sur le prix : choisir le plus petit total de billets, puis le plus petit nombre de billets unitaires

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT 6 lignes :
    Forfaits de 24 billets - A
    Forfaits de 12 billets - B
    Forfaits de 5 billets - C
    Billets unitaires - D
    Total billets - T
    Prix total - PPP.PP$

Prompts EXACTS :
1) "Entrez le nombre de billets necessaires : "
2) "Entrez le statut etudiant (O/N) : "

Conseil :
- Une solution simple consiste a tester plusieurs combinaisons de forfaits avec des boucles (bruteforce).
"""

# TODO: Lire n (int) et statut (str)
try: 

    n=int(input("Entrez le nombre de billets necessaires : ")) 

    statut=str(input("Entrez le statut etudiant (O/N) : "))

except ValueError: 

    print("Erreur - donnees invalides.") 

# TODO: Validation (n >= 0 et statut dans {O, N}) 

if n>=0 and (statut.lower() == "o" or statut.lower() == "n"):

    a = n//24
    e = n%24
    b = e//12
    f = e%12
    c = f//5
    d = f%5
    t = a+b+c+d

    if statut.lower() == "n":
        p = a*66 + b*36 + c*15.75 + d*3.6
    else:
        p = 0.88*(a*66+b*36+c*15.75)+d*3.6

# TODO: Calculer et afficher le resultat exact (6 lignes)

    print(
f"""Forfaits de 24 billets - {a}
Forfaits de 12 billets - {b}
Forfaits de 5 billets - {c}
Billets unitaires - {d}
Total billets - {n}
Prix total - {p:.2f}$""")

# TODO: Chercher la meilleure combinaison (A, B, C, D)

else:

    print("Erreur - donnees invalides.") 