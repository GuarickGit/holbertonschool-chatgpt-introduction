#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule le facteur (factorielle) d'un nombre entier positif en utilisant la récursion.

    Parameters:
        n (int): Un entier dont on souhaite calculer la factorielle. Doit être >= 0.

    Returns:
        int: La factorielle de n. Retourne 1 si n est égal à 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Récupère l'argument de ligne de commande, le convertit en entier et calcule sa factorielle
f = factorial(int(sys.argv[1]))
print(f)
