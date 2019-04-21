from tester_nlogn import return_exam_order_list
import called_time

def tester():
    counter = called_time.Counter()
    #premier array = dates de sortie
    #deuxieme array = dates d'echeance
    #[exam0, exam1, exam2, exam3, exam4, exam5]

    # listes_sorties_echeances = [[1, 1, 0, 2, 0], [2, 2, 4, 4, 1]]
    #reponse [4, (0-1), (0-1), (2-3), (2-3)]

    # listes_sorties_echeances = [[0, 0, 1, 1, 2, 2], [5, 5, 4, 4, 3, 3]]
    #reponse [(0-1), (2-3), (4-5), (4-5), (2-3), (0-1)]

    listes_sorties_echeances = [[2, 0, 0, 0, 3, 3], [3, 2, 2, 2, 5, 4]]
    #reponse [(1-2-3), (1-2-3), (1-2-3), 0, 5, 4]


    return_exam_order_list(listes_sorties_echeances, counter)
    print(return_exam_order_list(listes_sorties_echeances, counter))
    print("\n" + str(counter.count))

tester()
