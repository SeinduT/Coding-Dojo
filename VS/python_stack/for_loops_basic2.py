#1. Biggie Size
def biggie_size(orig_list):
    for x in range(1, len(orig_list), 1):
        if orig_list[x] > 0:
            orig_list[x] = "big"
    return orig_list

print(biggie_size([-1,5,-6,3,0]))

#2. Count Positives
def count_positives(list):
    temp = 0
    for val in list:
        if val > 0:
            temp += 1
    list[len(list) - 1] = temp
    return list

print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))

#3. Sum Total
def sum_total(list):
    total = 0
    for val in list:
        total += val
    return total

print(sum_total([2, 6, 4, 3]))
print(sum_total([7, 5, -4]))

#4. Average 
def average(list):
    total = 0
    for val in list:
        total += val
    return float(total) / float(len(list))

print(average([2, 3, 5, 7]))

#5. Length 
def length(list):
    count = 0
    for val in list:
        count += 1
    return count

print(length([5, 21, 4, -32]))
print(length([]))

#6. Minimum 
def minimum(list):
    if len(list) == 0:
        return False
    result = list[0]
    for val in list:
        if val < result:
            result = val
    return result

print(minimum([22, 3, 9, -8]))
print(minimum([]))

#7. Maximum
def maximum(list):
    if len(list) == 0:
        return False

    result = list[0]
    for val in list:
        if val > result:
            result = val
    return result

print(maximum([33, 7, 5, -12]))
print(maximum([]))

#8. Ultimate Analysis 
def ultimate_analysis(list):
    result = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(list) == 0:
        return result
    else:
        result['sum_total'] = 0
        result['maximum'] = list[0]
        result['minimum'] = list[0]
    
    for val in list:
        if val > result['maximum']:
            result['maximum'] = val
        elif val < result['minimum']:
            result['minimum'] = val

        result['sum_total'] += val
        result['length'] += 1
    result['average'] = result['sum_total'] / len(list)

    return result

print(ultimate_analysis([23, 8, 6, -10]))
print(ultimate_analysis([]))

#9. Reverse List
def reverse_list(list):
    half_len = int(len(list) / 2)
    for i in range(half_len):
        list[i] , list[len(list) - 1 - i] = list[len(list) - 1 - i], list[i]
    return list

print(reverse_list([21, 9, 6, -7]))
print(reverse_list([33, 6, 7, -10]))
print(reverse_list([]))
print(reverse_list([1]))
print(reverse_list([2,6]))