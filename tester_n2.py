import copy


def return_exam_order_list(listes_sorties_echeances, counter):
    day_map = make_day_possible_exam_map(listes_sorties_echeances[0], listes_sorties_echeances[1])
    exam_order = get_liste_from_map(day_map, counter)
    return exam_order


def make_day_possible_exam_map(liste_sortie, liste_echeance):
    day_map = {}
    number_of_possible_days = len(liste_sortie)
    for k in range(0, number_of_possible_days):
        day_map[k] = []
    for i in range(0, number_of_possible_days):
        min = liste_sortie[i]
        max = liste_echeance[i]
        for j in range(min, max+1):
            day_map[j].append(i)
    return day_map


def get_liste_from_map(day_map, counter):
    exam_day = 0
    for exam_number in day_map[0]:
        day_map_without_exam = get_map_without_exam_number(day_map, exam_number)
        new_list = put_next_exam_in_list(day_map_without_exam, exam_day + 1, [exam_number], counter)
    return new_list


def put_next_exam_in_list(day_map, day, old_list, counter):
    counter.add()
    for exam_number in day_map[day]:
        day_map_without_exam = get_map_without_exam_number(day_map, exam_number)
        old_list.append(exam_number)
        if(len(old_list) == len(day_map)):
            return old_list
        else:
            old_list = put_next_exam_in_list(day_map_without_exam, day + 1, old_list, counter)
            if (len(old_list) == len(day_map)):
                return old_list
            old_list.pop()
    return old_list


def get_map_without_exam_number(day_map, exam_number):
    day_map_without_exam = copy.deepcopy(day_map)
    for day, exam_list in day_map_without_exam.items():
        try:
            exam_list.remove(exam_number)
        except ValueError:
            pass
    return day_map_without_exam


def put_back_exam_in_map(day_map, exam_number):
    pass