# TODO: Lire le nom (str)
nom = str(input("Entrez votre nom complet : ")).title()
# TODO: Lire les 4 valeurs (int)
try:
    match_football = int(input("Entrez le nombre de matchs de football des Carabins suivis cet automne : "))
    duree_football = int(input("Entrez la duree moyenne d'un match de football suivi (en minutes) : "))
    match_soccer = int(input("Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "))
    duree_soccer = int(input("Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "))
# TODO: Valider les donnees (matchs >= 0, durees > 0)
    if match_football < 0 or match_soccer < 0 : print("Erreur - donnees invalides.")
    if duree_football <= 0 or duree_soccer <= 0 : print("Erreur - donnees invalides.")
# TODO: Calculer les minutes totales (football, soccer, total)
    total_football = match_football*duree_football
    total_soccer = match_soccer*duree_soccer
    total = total_soccer + total_football
# TODO: Convertir en heures/minutes et afficher exactement 4 lignes
    watch_football = f"{int(total_football/60)}h{(total_football%60):02d}min"
    watch_soccer = f"{int(total_soccer/60)}h{(total_soccer%60):02d}min"
    watch = f"{int(total/60)}h{(total%60):02d}"
    print(f"""Bonjour {nom}
        Football (Carabins): {match_football} match(s), {watch_football} de visionnage
        Soccer (Carabins): {match_soccer} match(s), {watch_soccer} de visionnage
        Total: {watch}""")
except ValueError:
    print("Erreur - donnees invalides.")