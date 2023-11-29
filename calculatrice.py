historique_calculs = []

def calculatrice():
    global historique_calculs
    
    operation = input("Entrez l'opération à effectuer (+, -, *, /) ou 'historique' pour afficher l'historique ou 'effacer' pour effacer l'historique : ")

    if operation == 'historique':
        if historique_calculs:
            print("Historique des calculs :")
            for calcul in historique_calculs:
                print(calcul)
        else:
            print("L'historique est vide.")
        calculatrice() # Redémarrer la calculatrice
        return
    elif operation == 'effacer':
        historique_calculs.clear()
        print("L'historique a été effacé.")
        calculatrice() # Redémarrer la calculatrice
        return

    if operation not in ['+', '-', '*', '/']:
        print("Opération non valide. Veuillez entrer une opération correcte.")
        calculatrice() # Redémarrer la calculatrice
        return

    try:
        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))
    except ValueError:
        print("Veuillez entrer des nombres valides.")
        calculatrice() # Redémarrer la calculatrice
        return

    if operation == '/' and nombre2 == 0:
        print("Erreur : Division par zéro impossible.")
        calculatrice() # Redémarrer la calculatrice
        return

    # Effectuer l'opération demandée
    if operation == '+':
        resultat = nombre1 + nombre2
    elif operation == '-':
        resultat = nombre1 - nombre2
    elif operation == '*':
        resultat = nombre1 * nombre2
    elif operation == '/':
        resultat = nombre1 / nombre2

    calcul = f"{nombre1} {operation} {nombre2} = {resultat}"
    historique_calculs.append(calcul) # Ajouter le calcul à l'historique
    print(f"Le résultat de {calcul} est égal à : {resultat}")

    calculatrice() # Redémarrer la calculatrice pour une nouvelle opération

# Appel de la fonction calculatrice
calculatrice()


