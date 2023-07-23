def singleNumber(arr):
    
    result=0
    for i in arr:
        result=i^result
    return result

arr=list(map(int,input().split()))
print(singleNumber(arr))