import copy


def return_exam_order_list(listes_sorties_echeances, counter):
    start_map = make_start_day_possible_exam_map(listes_sorties_echeances[0], listes_sorties_echeances[1])
    exam_order = get_liste_from_start_map(start_map, counter)
    return exam_order


def make_start_day_possible_exam_map(liste_sortie, liste_echeance):
    map_of_echeance_number_tuples_by_start = {}
    number_of_possible_start_days = len(liste_sortie)
    for k in range(0, number_of_possible_start_days):
        map_of_echeance_number_tuples_by_start[k] = []
    for i in range(0, len(liste_sortie)):
        map_of_echeance_number_tuples_by_start[liste_sortie[i]].append([liste_echeance[i], i])
    for start_day, echeance_number_tuple_list in map_of_echeance_number_tuples_by_start.items():
        map_of_echeance_number_tuples_by_start[start_day] = sorted(echeance_number_tuple_list, key=lambda x: x[0])
    return map_of_echeance_number_tuples_by_start


def get_liste_from_start_map(map_of_echeance_number_tuples_by_start, counter):
    start_day = 0
    for echeance_number_tuple in map_of_echeance_number_tuples_by_start[start_day]:
        day_map_without_start_day = get_map_with_this_day_merged_with_next_day(map_of_echeance_number_tuples_by_start, echeance_number_tuple, start_day)
        new_list = put_next_exam_in_list(day_map_without_start_day, start_day + 1, [echeance_number_tuple[1]], counter)
    return new_list


def put_next_exam_in_list(map_of_echeance_number_tuples_by_start, start_day, old_list, counter):
    counter.add()
    for echeance_number_tuple in map_of_echeance_number_tuples_by_start[start_day]:
        day_map_without_start_day = get_map_with_this_day_merged_with_next_day(map_of_echeance_number_tuples_by_start, echeance_number_tuple, start_day)
        old_list.append(echeance_number_tuple[1])
        if(len(old_list) == len(map_of_echeance_number_tuples_by_start)):
            return old_list
        else:
            old_list = put_next_exam_in_list(day_map_without_start_day, start_day + 1, old_list, counter)
            if (len(old_list) == len(map_of_echeance_number_tuples_by_start)):
                return old_list
            old_list.pop()
    return old_list


def get_map_with_this_day_merged_with_next_day(map_of_echeance_number_tuples_by_start, echeance_number_tuple, start_day):
    merged_start_map = copy.deepcopy(map_of_echeance_number_tuples_by_start)
    merged_start_map[start_day].remove(echeance_number_tuple)
    if(start_day<len(map_of_echeance_number_tuples_by_start)-1):
        merged_start_map[start_day+1].extend(merged_start_map[start_day])
        merged_start_map[start_day+1] = sorted(merged_start_map[start_day+1], key=lambda x: x[0])

    merged_start_map[start_day] = []

    return merged_start_map
