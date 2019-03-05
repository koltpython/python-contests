a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print('A triangle with edges ({},{},{}) can exist.'.format(a, b, c))
else:
    print('A triangle with edges ({},{},{}) cannot exist.'.format(a, b, c))
