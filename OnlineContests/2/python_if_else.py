N = int(input())

if N % 2 == 1:
    print('Weird')
else:
    if 2 <= N <= 5:
        print('Not Weird')
    elif 6 <= N <= 20:
        print('Weird')
    elif 20 <= N:
        print('Not Weird')