# Všeobecná Divide-and-conquer funkcia

# problem - Problém, ktorý chceme riešiť (vstupné dáta)
# indiv - Vracia True, ak sa (pod)problém nedá viac deliť
# divide - Delí (pod)problém na list podproblémov
# solve - Rieši (pod)problém, ktorý sa nedá viac deliť
# combine - Skombinujé vyriešené podproblémy

def divide_and_conquer(problem, indiv, divide, solve, combine):
    def dc(prob):
        if indiv(prob):
            return solve(prob)
        return combine(prob, list(map(dc, divide(prob))))

    return dc(problem)


# Použitie divide_and_conquer funkcie na vytvorenie MergeSortu

# problem - Vstupné pole čísel
# indiv - (Pod)problém sa nedá viac deliť ak má list dĺžku 1
# divide - Delí list na dve rovnaké polovice
# solve - V tomto prípade solve len vracia jednoprvkové pole,
#        'reálne' riešenie problému sa vykonáva pri combine,
#         kde sa jednoprvkové polia zoradia
# combine - Skombinuje a správne zoradí jednoprvkové polia 

def mergesort(lst):
    def merge(lst1, lst2):
        if not lst1: return lst2
        if not lst2: return lst1

        if lst1[0] <= lst2[0]:
            return [lst1[0]] + merge(lst1[1:], lst2)
        else:
            return [lst2[0]] + merge(lst1, lst2[1:])

    indiv = lambda p: len(p) <= 1
    divide = lambda p: [p[:len(p) // 2], p[len(p) // 2:]]
    solve = lambda p: p
    combine = lambda _, s: merge(s[0], s[1])
    return divide_and_conquer(lst, indiv, divide, solve, combine)


# Použitie divide_and_conquer funkcie na vytvorenie QuickSortu

def quicksort(lst):
    indiv = lambda p: len(p) <= 1
    divide = lambda p: [[i for i in p[1:] if i <= p[0]], [i for i in p[1:] if i > p[0]]]
    solve = lambda p: p
    combine = lambda p, s: s[0] + [p[0]] + s[1]
    return divide_and_conquer(lst, indiv, divide, solve, combine)

# Test funkčnosti

from random import randint

random_lst = [randint(0, 100) for _ in range(1000)]
print('Pôvodný list', random_lst, '\n')
print('Mergesort', mergesort(random_lst), '\n')
print('Quicksort', quicksort(random_lst))
