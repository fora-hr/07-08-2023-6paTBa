import json 
from datetime import datetime

with open('competitors2.json', encoding='UTF-8') as f_file:
    competitors_json = f_file.read()

with open('results_RUN.txt', encoding='UTF-8') as f_file:
    result = f_file.read()

competitors = json.loads(competitors_json)


result = result.split('\n')
result[0] = result[0].replace('\ufeff','')
result.pop(-1)
result = sorted(result, key=lambda x: (int(x.split()[0]), x.split()[1]))

table = [] 

for i in range(0, len(result), 2):
    time = datetime.strptime(result[i].split()[2], '%H:%M:%S,%f') - datetime.strptime(result[i+1].split()[2], '%H:%M:%S,%f')
    table.append([result[i].split()[0], time])
table = sorted(table, key=lambda x: x[1])

print('| Занятое место | Нагрудный номер |    Имя    |  Фамилия  |  Результат |')
print('|---------------|-----------------|-----------|-----------|------------|')
i = 1
for x in table:
    time = (datetime.strptime(str(x[1]), "%H:%M:%S.%f")).strftime("%H:%M:%S.%f")
    print('|','|'.join([
        f'{str(i):14}',
        f'{x[0]:17}',
        f'{competitors[x[0]]["Surname"]:11}',
        f'{competitors[x[0]]["Name"]:11}',
        f'{time[:-4]:9}',
    ]), '|')
    i += 1