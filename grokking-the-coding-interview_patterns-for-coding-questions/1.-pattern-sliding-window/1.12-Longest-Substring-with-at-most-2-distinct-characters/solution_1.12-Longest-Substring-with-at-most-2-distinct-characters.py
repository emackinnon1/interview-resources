def longest_with_two_distinct(string):
    total = 0
    start = 0
    longest = ''
    h = {}
    
    for end, c in enumerate(string):
        if not h.get(c):
            h[c] = 0
        h[c] += 1
        while len(h.keys()) > 2:
            strt_c = string[start]
            h[strt_c] -= 1
            if h[strt_c] == 0:
                del h[strt_c]
            start += 1
        window = end - start + 1
        total = max(window, total)

            

    return total, h


print(longest_with_two_distinct('eceba')) #3
print(longest_with_two_distinct('ccaabbb')) #5