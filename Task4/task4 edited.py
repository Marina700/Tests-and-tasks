import sys
script,massive_file = sys.argv
massive = open(massive_file, 'r', encoding = 'utf-8')
massive_list = list(map(str.strip, massive.readlines()))
int_massive = [int(i) for i in massive_list]
mid = sorted(int_massive)[len(int_massive) // 2]
print(sum(abs(i-mid) for i in int_massive))
