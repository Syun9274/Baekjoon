N = int(input())
c = 0

while N >= 0:
    if N % 5 == 0:
        print(c + N // 5)
        break

    N -= 3
    c += 1

else: print(-1)