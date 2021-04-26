import math
T = int(input())
result=[]
max_num = 0
def divisor_count(n):
    x = 0
    for i in range(n):
        x = len([i for i in range(1,n+1) if not n % i])
    return(x)

for T_itr in range(T):
    NK = input().split()

    N = int(NK[0])

    K = int(NK[1])
    max_num = 0
    for y in range(1,N+1):
        count_div = divisor_count(y)
        if(count_div == K and max_num < y):
            max_num = y
    result.append(max_num)
for i in result:
    if(i):
        print(i)
    else:
        print(-1)