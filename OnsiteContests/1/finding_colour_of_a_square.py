col = input()
row = int(input())

col_num = ord(col) - ord('a') + 1

if (row + col_num) % 2 == 0:
    print('Black')
else:
    print('White')
