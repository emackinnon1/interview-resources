def longestSubStrDistinctChars(string, k):
    # global longest
    longest = 0
    start = 0
    char_map = {}
    longest_sub = ''
    # for char in string, insert into charater map
    # if more than k characters in map
    # current substring is longest
    # slide window forward and remove appropriate character

    for end, c in enumerate(string):
        if c not in char_map:
            char_map[c] = 1
        else:
            char_map[c] += 1
        while len(char_map.keys()) > k:
            char_map[string[start]] -= 1
            if char_map[string[start]] == 0:
                del char_map[string[start]]
            start += 1
        curr = end - start + 1
        need_change = longest > curr
        longest_sub = longest_sub if need_change else string[start:end + 1]
        longest = longest if need_change else curr
    return longest, longest_sub


print(longestSubStrDistinctChars("araaci", 2))
print(longestSubStrDistinctChars("araaci", 1))
print(longestSubStrDistinctChars("cbbebi", 3))
