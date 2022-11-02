n = int(input())

arr = list(map(int,input().split()))
d = [0] * 100

# 다이나믹 프로그래밍 바텀업
d[0] = arr[0]
d[1] = max(arr[0],arr[1])
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2] + arr[i])

print(d[n-1])

# 점화식 ai = max(ai-1,ai-2+ki)
# #