def permutation(arr, m, result):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(len(arr)):
        if result and arr[i] < result[-1]:
            continue
        
        result.append(arr[i])
        permutation(arr, m, result)
        result.pop()

N, M = map(int, input().split())
num = list(range(1, N + 1))

permutation(num, M, [])