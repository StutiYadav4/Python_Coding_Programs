def countAndSay(n):
    if n == 1:
        return "1"

    def next_term(term):
        result = []
        i = 0
        while i < len(term):
            count = 1
            while i + 1 < len(term) and term[i] == term[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + term[i])
            i += 1
        return ''.join(result)
    current_term = "1"
    for _ in range(n - 1):
        current_term = next_term(current_term)
    return current_term

print(countAndSay(4))
print(countAndSay(1))
print(countAndSay(5))






