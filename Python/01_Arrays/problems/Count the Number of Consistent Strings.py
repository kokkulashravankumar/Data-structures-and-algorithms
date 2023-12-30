def countConsistentStrings(allowed, words):
    print(allowed)
    value = list(allowed.strip(""))
    v = []
    count = 0
    for i in range(len(words)):
        for j  in range(len(value)):
            if value[j] not in words[i]:
                count = count + 1
                v.append(count)
            else:
                count = 0
    print(v)
    return len(v)


# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
#Output: 2
allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# allowed = "cad"
# words = ["cc","acd","b","ba","bac","bad","ac","d"]
#Output: 4

print(countConsistentStrings(allowed,words))