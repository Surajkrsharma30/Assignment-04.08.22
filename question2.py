#--------------------------assignment 2 ------------------------------
#sample string:"1234abcd"
#expected output:"dcba4321"

def string_reverse(str1):
    rstr = ''
    index = len(str1)
    while index > 0:
        rstr += str1[ index - 1 ]
        index = index - 1
    return rstr
print(string_reverse('1234abcd'))

