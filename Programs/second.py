"""
Write a function demystify(word) that takes a string composed of the characters 
"l" and"1" and returns the string formed by replacing each instance of"l" by"a"
and each instance of "1" by "b".
"""
def demystify(word):
    w=""
    for i in range(len(word)):
        ch=word[i]
        if ch=='l':
            ch='a'
            w=w+ch
        elif ch=='1':
            ch='b'
            w=w+ch
        else:
            w=w+ch
    return w
print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
