def match_words(words):
    cfr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            cfr += 1
            lst.append(word)

    print("list of words with first same and last character\n lst")
    return cfr

count = match_words(['dbg', 'lml',  ' qpr ', ' dyd ', ' 1231 ', ' 1234 '])
print("count of words with first same and last character\n count")