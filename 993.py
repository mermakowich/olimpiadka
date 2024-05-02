n = int(input())
ma = []

for i in range(n+1):
    ma.append(list())
print(ma)

for i in range (1, n+1):
    ma2 = list(map(int, input().split()))

    for j in range(i, n):
        if ma2[j] == 1:
            ma[i].append(j+1)
print(ma)
print(ma2)

for i in range(1, (n+1)):
    for j in range(len(ma[i])):
        print(i, ma[i][j])