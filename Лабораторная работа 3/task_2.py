# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, space=','):
    string1 = set(str1.split(space))
    string2 = set(str2.split(space))
    common = list(string1.intersection(string2))
    common.sort()
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
find_common_participants(participants_first_group, participants_second_group, '-')
# TODO Провеьте работу функции с разделителем отличным от запятой
