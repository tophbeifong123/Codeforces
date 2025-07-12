n,m = map(int,input().split())

count = 1
for i in range(1,n+1):
    if i == 0 or i == n:
        print('#'*m)
    elif i % 2 == 0:
        if count % 2 != 0:
            print('.'*(m-1)+'#')
        else:
            print('#'+'.'*(m-1))
        count+=1
    else:
        print('#'*m)