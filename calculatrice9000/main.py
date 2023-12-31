def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Erreur : Division par zéro.")

def afficher_historique(historique):
    print("Historique des calculs:")
    for i, calcul in enumerate(historique, 1):
        print(f"{i}. {calcul}")

def calculatrice():
    historique = []

    while True:
        try:
            # Demander à l'utilisateur les deux nombres et l'opération
            entree = input("Entrez le premier nombre (ou 'q' pour quitter) : ")

            # Vérifier si l'utilisateur souhaite quitter
            if entree.lower() == 'q':
                break

            nombre1 = float(entree)
            operateur = input("Entrez l'opération (+, -, *, /) : ")
            nombre2 = float(input("Entrez le deuxième nombre : "))

            # Vérifier l'opérateur et effectuer l'opération appropriée
            if operateur == '+':
                resultat = addition(nombre1, nombre2)
            elif operateur == '-':
                resultat = soustraction(nombre1, nombre2)
            elif operateur == '*':
                resultat = multiplication(nombre1, nombre2)
            elif operateur == '/':
                resultat = division(nombre1, nombre2)
            else:
                raise ValueError("Erreur : Opération non prise en charge.")

            # Enregistrer le calcul dans l'historique
            calcul = f"{nombre1} {operateur} {nombre2} = {resultat}"
            historique.append(calcul)

            # Afficher le résultat
            print("Le résultat est :", resultat)

        except ValueError as e:
            print(f"Erreur : {e}")
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")

    # Afficher l'historique avant de quitter
    afficher_historique(historique)

# Exécuter la calculatrice
calculatrice()
