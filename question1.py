
#----------------------------assignment 3------------------------------------------#
#write a python function to sum all the numbers in a list.
#sample list:(8,2,3,0,7)
#expected output:20


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8,2,3,0,7)))


