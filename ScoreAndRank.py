id = eval(input("Enter the id :"))
score = eval(input("Enter the scores :"))
sorted_score = sorted(score, reverse=True)
print("\n")
print("Score : ", sorted_score)
j = 1
rank = []
for ind in range(0, len(sorted_score)):
    if sorted_score[ind] == sorted_score[ind-1]:
        rank.append(rank[-1])
    else:
        rank.append(j)
    j = rank[-1]+1
print("Rank : ", rank)

