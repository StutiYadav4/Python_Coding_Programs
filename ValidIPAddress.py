def restoreIpAddresses(s):
    def is_valid(segment):
        if len(segment) > 1 and segment[0] == '0':
            return False
        return 0 <= int(segment) <= 255

    def backtrack(start=0, path=[]):
        if len(path) == 4:
            if start == len(s):
                result.append('.'.join(path))
            return

        for length in range(1, 4):
            if start + length <= len(s):
                segment = s[start:start + length]
                if is_valid(segment):
                    backtrack(start + length, path + [segment])

    result = []
    backtrack()
    return result


print(restoreIpAddresses("25525511135"))
print(restoreIpAddresses("0000"))
print(restoreIpAddresses("101023"))