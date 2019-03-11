s = input()
vowels='AEIOU'
kevin_score = 0
stuart_score = 0

# there is (len(s) - i) substrings
# starting from index i in s
for index in range(len(s)):
    if s[index] in vowels:
        kevin_score += len(s) - index
    else:
        stuart_score += len(s) - index

if kevin_score > stuart_score:
    print('Kevin {}'.format(kevin_score))
elif kevin_score < stuart_score:
    print('Stuart {}'.format(stuart_score))
else:
    print('Draw')