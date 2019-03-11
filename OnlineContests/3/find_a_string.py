def count_substring(string, sub_string):
    sub_len = len(sub_string)
    count = 0
    for start in range(len(string) - sub_len + 1):
        if sub_string == string[start:(start + sub_len)]:
            count += 1
    return count
    # Note that str.count() does not work since it counts
    # noncolliding instances, for example
    # 'ABCDCDC'.count('CDC') gives 1, since instances collide


# This part is given and we cannot modify it
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)