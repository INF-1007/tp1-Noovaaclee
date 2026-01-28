# -*- coding: utf-8 -*-
# Exercice 01 - Bilan de visionnage Carabins (gabarit)
"""
Objectif :
- DEMANDER : nom complet, matchs football, duree football, matchs soccer, duree soccer
- Valider : matchs >= 0 et durees > 0 (entiers)
- Convertir les minutes en format HhMM (minutes sur 2 chiffres)
- Afficher EXACTEMENT 4 lignes :
    Bonjour {nom}
    Football (Carabins): {A} match(s), {Hf}h{Mf:02d} de visionnage
    Soccer (Carabins): {B} match(s), {Hs}h{Ms:02d} de visionnage
    Total: {Ht}h{Mt:02d}

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS a utiliser :
1) "Entrez votre nom complet : "
2) "Entrez le nombre de matchs de football des Carabins suivis cet automne : "
3) "Entrez la duree moyenne d'un match de football suivi (en minutes) : "
4) "Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "
5) "Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "
"""

# TODO: Lire le nom (str)
nom = str(input("Entrez votre nom complet : "))
# TODO: Lire les 4 valeurs (int)
try:
    match_football = int(input("Entrez le nombre de matchs de football des Carabins suivis cet automne : "))
    duree_football = int(input("Entrez la duree moyenne d'un match de football suivi (en minutes) : "))
    match_soccer = int(input("Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "))
    duree_soccer = int(input("Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "))
except ValueError:
    print("Erreur - donnees invalides.")
# TODO: Valider les donnees (matchs >= 0, durees > 0)
try:
    if match_football or match_soccer < 0 : print("Erreur - donnees invalides.")
    if duree_football or duree_soccer <= 0 : print("Erreur - donnees invalides.")
except ValueError:
    print("Erreur - donnees invalides.")
# TODO: Calculer les minutes totales (football, soccer, total)
total_football = match_football*duree_football
total_soccer = match_soccer*duree_soccer
total = total_soccer + total_football
# TODO: Convertir en heures/minutes et afficher exactement 4 lignes
watch_football = f"{int(total_football/60)}h{total_football%60}min"
watch_soccer = f"{int(total_soccer/60)}h{total_soccer%60}min"
watch = f"{int(total/60)}h{total%60}"
print(f"""Bonjour {nom}
      Football (Carabins): {match_football} match(s), {watch_football} de visionnage'
      Soccer (Carabins): {match_soccer} match(s), {watch_soccer} de visionnage\
      Total: {watch}""")