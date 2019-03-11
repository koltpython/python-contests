# Function to split and join
def split_and_join(line):
    return '-'.join(line.split())

# This part is given and we cannot modify it
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)