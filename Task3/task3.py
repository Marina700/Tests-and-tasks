import json, sys
script, values, tests, results = sys.argv
print('Введите путь к файлу с данными')
values=input()
print('Введите путь к файлу с данными теста' )
tests=input()
print('Введите путь к файлу с результатами' )
results=input()
with open(values, 'r', encoding='utf-8') as file:
    val = json.load(file)
with open(tests, 'r', encoding='utf-8') as file:
    te = json.load(file)
tests_dict = {item['id']: item for item in te['tests']}
te['tests'] = tests_dict
val_dict = {item['id']: item for item in val['values']}
val['values'] = val_dict
for d in te.values():
    for key in (val.keys() & d.keys()):
        d[key] = te[key]
        if te[d]['value'] == '':
            te[d]['value']=val['value']
with open(results, 'w', encoding='utf-8') as file:
    json.dump(te, file, ensure_ascii=False, indent=4)
