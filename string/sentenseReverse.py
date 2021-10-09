## Given an input string, reverse the string word by word.
## string could be " the sky is blue" or "  the   sky is        blue" => "blue is sky the"
import re
def reverseWords(s):
    # ## 1st Approach
    # s = re.sub('\s+', ' ', s)
    # s = s.strip()
    # s = list(map(str, s.split(" ")))
    # s.reverse()
    # s = (" ".join(s))
    # s = str(s)
    # return s
    # ## 2nd Approach
    # word = s.split()
    # word.reverse()
    # return " ".join(word)

    # ##3rd Approach
    # word=s.split()
    # res=""
    # n=len(word)-1
    # while n>=0:
    #     res+=word[n] + " "
    #     n-=1
    # return res[:-1]

    ##4th Approach
    i=0
    words = []
    length = len(s)
    while i<length:
        if s[i] not in ' ':
            word_start = i
            while i<length and s[i] not in ' ':
                i+=1
            words.append(s[word_start:i])
        i+=1
    return " ".join(reversed(words))



print(reverseWords('the              sky    is blue'))