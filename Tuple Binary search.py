
def binary_search(tuplem, search):
    
    left = 0
    right = len(tuplem) - 1

    while left <= right:
        mid = (left + right) // 2
        if tuplem[mid] == search:
            return mid
        elif tuplem[mid] < search:
            left = mid + 1
        else:
            right = mid - 1

    return -1
    
    
try: 
    a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    s = 8
    result = binary_search(a, s)   
    if result != -1:
        print(f"Element {s} found at index {result}.")
    else:
        print(f"Element {s} could not found.")
    
except:
    print('TypeError')