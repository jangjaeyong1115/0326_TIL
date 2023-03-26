N = int(input())

customer = list(map(int,input().split()))

cnt = 0
seat = []
for i in range(N):
    if customer[i] in seat:
        cnt += 1
    else:
        seat.append(customer[i])
print(cnt)