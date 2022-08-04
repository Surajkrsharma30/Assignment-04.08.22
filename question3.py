#write a python function that accepts a string and calculate the number of upper case letters and lower case letters.
#sample string:-'the quick Brow fox'
#expectrd output:-No of upper case characters : 3
#No of Lowere case characters : 12

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
        print("original string :",s)
        print("upper case charecters:",d["UPPER_CASE"])
        print("lower case charecters:",d["LOWER_CASE"])
string_test('The quick Brow Fox')