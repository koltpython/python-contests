name = input()
surname = input()
major = input()
year = input()

# There are many ways to print with the format given in description
# Hi, I'm Jane Doe. I'm studying Sociology for 3 years.

# Idea 1: remove seperation and list elements as you like
print('Hi, I\'m ', name, ' ', surname, '. I\'m studying ', major, ' for ', year, ' years.', sep='')

# Idea 2: String concatenation,
# note that we need to cast if type of variables is not str
print('Hi, I\'m ' + name + ' ' + surname + '. I\'m studying ' + major + ' for ' + year + ' years.')

# Idea 3: Use string formatting
# More info here: https://www.programiz.com/python-programming/methods/string/format
# default arguments
print('Hi, I\'m {} {}. I\'m studying {} for {} years.'.format(name, surname, major, year))
# positional arguments
print('Hi, I\'m {0} {1}. I\'m studying {2} for {3} years.'.format(name, surname, major, year))
# you can mix order with positional arguments
print('Hi, I\'m {1} {0}. I\'m studying {3} for {2} years.'.format(surname, name, year, major))
# keyword arguments
print('Hi, I\'m {name} {surname}. I\'m studying {major} for {year} years.'.format(name=name, surname=surname, major=major, year=year))

# Idea 4: Use f strings, requires Python version 3.6 or more
# More info here: https://realpython.com/python-f-strings/
print(f'Hi, I\'m {name} {surname}. I\'m studying {major} for {year} years.')