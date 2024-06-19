s = input("Enter the string: ")
c = input("Enter the character: ")
n = len(s)
left_dist = [n] * n
right_dist = [n] * n

closest = -n
for i in range(n):
    if s[i] == c:
        closest = i
    left_dist[i] = i - closest

closest = 2 * n
for i in range(n - 1, -1, -1):
    if s[i] == c:
        closest = i
    right_dist[i] = closest - i
answer = [min(left_dist[i], right_dist[i]) for i in range(n)]
print(answer)



