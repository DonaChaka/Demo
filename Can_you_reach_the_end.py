import sys

input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n = int(input())

    obs = {}
    
    for _ in range(n):
        x, y = input().split()
        x, y = int(x), int(y)

        if (x+y-2) in obs:
            obs[x+y-2] += 1
        else:
            obs[x+y-2] = 1

    for i in obs.keys():
        if i <= n-1:
            if obs[i] == i+1:
                print("NO")
                break
        if i > n-1:
            if obs[i] == (n-1) - (i-n):
                print("NO")
                break

    else:
        print("YES")
