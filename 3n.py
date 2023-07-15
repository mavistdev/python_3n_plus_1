n = int(input('Число: '))
print(f'Исходное число - {n}')
moves = 0
i = n

def writelog(text, allow = True, disallowtext = None): #будет перенесено в либу mavist
    if allow:
        file = open("3nlog.txt", "a")
        file.write(f'\n {text}')
        file.close()

while n != 1:
	if n % 2 == 0:
		n = n // 2
		print(n)
		moves += 1
	else:
		n = n * 3 + 1
		print(n)
		moves += 1

print(f'Количество ходов - {moves}')
waitlog = f'''---
Исходное число - {i}
Количество ходов - {moves}
---'''
writelog(f'{waitlog}')
