import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('test_7.txt', 'r+') as file:
    for line in file:
        f_n, name, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
        i += 1
        if i >= 0:
            prof_aver = prof / i
    else:
        pr_sr = ({'Средняя прибыль компаний': round(prof_aver)})
        profit.update(pr_sr)
    print(f'Прибыль всех компании: - {prof:.2f}')
    print(f'Средняя прибыль всех компаний: - {round(prof_aver):.2f}')
    print(f'Сводные результаты компаний: - {profit}')

with open('test_7.txt.json', 'w+') as write_js:
    json.dump(profit, write_js)

js_str = json.dumps(profit)
print(f'Создан файл с расширением json со следующим содержимым:\n' f'{js_str}')
