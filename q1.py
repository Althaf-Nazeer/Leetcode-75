    #You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#Return the merged string.

def mergeAlternately(word1,word2):
    len1=len(word1)
    len2=len(word2)
    word=""
    a=0
    b=0
    while (a<len1 and b<len2):
        word=word+word1[a]
        a=a+1
        word=word+word2[b]
        b=b+1
    if (a<len1):
        while (a<len1):
            word=word+word1[a]
            a=a+1
    if  (b<len2):
        while (b<len2):
            word=word+word2[b]
            b=b+1
    print(word)
word1=input("enter word1")
word2=input("enter word2")
mergeAlternately(word1,word2)
