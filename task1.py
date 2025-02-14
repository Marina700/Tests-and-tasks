n = int(input()) #длина  массива
m = int(input()) #длина шага обхода
current_List = m * [int(i) for i in range(1, n + 1)] #массив который получился по факту с 1
step = [' '] #текущий шаг
total_List = [] #все шаги
count = 0
while step[-1] != 1:
    step.clear()
    for i in range(count, m + count):
        step.append(current_List[i])
        count += 1
    step_copy = step.copy()
    total_List.append(step.copy())
    count -= 1
for j in range(len(total_List)):
    print(total_List[j][0], end='')