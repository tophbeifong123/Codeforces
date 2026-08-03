for _ in range(int(input())):
    n = int(input())
    s = input()

    st = []

    for i in s:
        if st and st[-1] == i :
            st.pop()
        else:
            st.append(i)

    print('NO') if st else print('YES')