from collections import deque
n = int(input())

# print (n)
if n == 1:
    print (1)
elif n == 2 or n == 3:
    print ("NO SOLUTION")
elif n == 4:
    print ('2 4 1 3')
else:
    res = deque()
    res.append(2)
    res.append(4)
    res.append(1)
    res.append(3)
    for i in range(5, n+1, 2):
        res.append(i)
        if i + 1 <= n:
            res.appendleft(i+1)

    for x in res:
        print (x, end=" ")

