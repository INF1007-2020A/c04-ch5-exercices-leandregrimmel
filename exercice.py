#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt
from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        return number * -1


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    # string = "Il était une fois, huit petis canetons s'appellant respectivement "
    # for lettre_initiale in range(len(prefixes)):
    #     string += prefixes[lettre_initiale]
    #     string += suffixe
    #     if lettre_initiale < (len(prefixes) - 1):
    #         string += ", "
    #     else:
    #         string += ". "
    #
    # return [string]

    word_list = []
    for pre in prefixes:
        word_list.append(pre + suffixe)

    return word_list


def is_prime(number: int) -> bool:
    for i in range(2, number // 2):
        if number % i == 0:
            return False

    return True


def prime_integer_summation() -> int:
    prime = [2, 3, 5]
    number = 6

    while len(prime) < 100:
        if is_prime(number):
            prime.append(number)

        number += 1

    return sum(prime)


def factorial(number: int) -> int:
    fact = 1
    for i in range(2, number + 1):
        fact *= i

    return fact


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        print(i, end=", ")
    print()


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance = []

    for i in range(len(groups)):
        acceptance_count = 0
        if 3 <= len(groups[i]) > 10:
            acceptance_count += 1

        adults = 0
        for j in groups[i]:
            if groups[i][j] > 18:
                adults += 1
        if adults == len(groups[i]):
            acceptance_count += 1

    return acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
        [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
        [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
