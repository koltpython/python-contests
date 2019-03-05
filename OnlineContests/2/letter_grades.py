letter = input()

grade = float(ord('E') - ord(letter[0]))

if len(letter) == 2:
    if letter[1] == "+" and grade != 4:
        grade += 0.3
    elif letter[1] == "-":
        grade -= 0.3

# if letter is 'F', our calculation gives -1
if grade > 0:
    print(grade)
else:
    print(0.0)