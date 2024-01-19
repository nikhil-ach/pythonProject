arr =[4,5,2,1]
def sort_list(arr):
    n = len(arr)
    while True:
        flag = False
        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True
        n = n-1
        if not flag or n == 1:
            break
    return arr

print(sort_list(arr))

