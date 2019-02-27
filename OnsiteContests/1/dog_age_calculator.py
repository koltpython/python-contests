age = float(input())

if age < 0:
    print('Invalid')
elif age <= 2:
    print(age * 10.5)
else:
    print(21 + 4.0 * (age - 2))
