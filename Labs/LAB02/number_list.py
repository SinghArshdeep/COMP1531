
def find_reverse(numbers):
    numbers.reverse()
    return numbers
    #TODO: find the reverse of the list
    pass

def find_max(numbers):
    return max(numbers)
    #TODO: find the maximum of the list
    pass

def find_min(numbers):
    return min(numbers)
    #TODO: find the minimum of the list
    pass

def find_sum(numbers):
    return sum(numbers)
    #TODO: find the sum of all the numbers in the list
    pass

def find_average(numbers):
    return sum(numbers)/len(numbers)
    #TODO: find the average of all the numbers in the list
    pass

def find_descending(numbers):
    return sorted(numbers, reverse = True)
    #TODO: numbers sorted in descending order
    pass

def second_smallest(numbers):
    numbers = find_descending(numbers)
    x = len(numbers)
    a = numbers[x-1]
    b = numbers[x-2]
    i = 2
    while a == b:
        i = i+1
        b = numbers[x-i]
    return b
    #TODO: find the second smallest
    pass

def kth_smallest(numbers, k):
    numbers = find_descending(numbers)
    x = len(numbers)
    
    a = numbers[x-1]
    if k == 1:
        return a
    b = numbers[x-2]
    i = 2
    m = 1
    
    while m != k:
        if a == b:
            i = i + 1
        else:
            m = m + 1
            a = b
        b = numbers[x-i]

    return b
    #TODO: find the kth smallest number in the list
    pass

if __name__ == '__main__':
    # If you are testing, place your print statements here
    
    pass
