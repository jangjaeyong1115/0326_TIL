A,B = map(int, input().split())
if A > B:
  A,B = B,A
sum = 0

if A > 0:
  sum -= (A-1) * A // 2
  sum += B * (B+1) // 2
elif B > 0:
  sum -= A * (A-1) // 2
  sum += B * (B+1) // 2
else:
  sum -= A * (A-1) // 2
  sum += B * (B+1) // 2
  
print(sum)