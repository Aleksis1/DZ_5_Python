# Необходимо создать (не программно) текстовый файл,
# каждая строка описывает учебный предмет и наличие занятий по этому предмету и их количество.
# вывсти на экран

subj = {}
with open('test_6.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(practice)
    print(f'Общее количество часов по предмету: - \n{subj}')
