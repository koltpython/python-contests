n = int(input())

# Opt1: Without map
scores_str = input().split()
scores = []
for score in scores_str:
    scores.append(int(score))

# Opt2: With map
# map is a function that takes another function and a collection
# e.g, list and applies function to all items in collection
# scores = map(int, input().split())

# By default, sort function order from smaller to bigger
# We want bigger to smaller, make reverse flag True
scores.sort(reverse=True)

score_first = scores[0]

# Can have many winners, we want runner-up
for score in scores:
    if score != score_first:
        print(score)
        break
