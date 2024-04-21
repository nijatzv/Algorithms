
def axtar(listim, axtaris):
    for eded in range(len(listim)):
        if listim[eded] == axtaris:
            return eded
    return -1
     
      
try: 
    a = [1, 2, 3, 4, 5, 6, 7]
    b = 6     
    print(axtar(a, b))
except:
    print('TypeError')        