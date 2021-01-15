#1. Countdown
def countdown(x):
    list = []
    for i in range(x, -1, -1):
        list.append (i)
    return list
print (countdown(10))

#2. Print and Return
def num(a,b):
    print (a)
    return (b)
print (num(31,2))

#3. First Plus Length
def first_length(list):
    return list[0] + len(list)
print(first_length([5,4,3,2,1]))

#4. Values Greater than Second
def values_greater(orig_list):
    temp = []
    second_val = orig_list[1]
    for x in range(0, len(orig_list), 1):
        if orig_list(x) > second_val:
            temp.append (orig_list(x))
    if len(temp) > 2:
        print(len(temp))
        return temp
    elif len(temp) < 2: 
        return False
print(values_greater([1,2,5,3,4]))

#5. This Length, That Value
def this_that(a,b):
    temp = []
    for x in range(0, a, 1):
        temp.append(b)
    return temp
print(this_that(3,5))