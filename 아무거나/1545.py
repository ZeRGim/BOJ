word = list(input())
n = len(word)
ans = [0]*n
word.sort()
if n == 1:
    print(word[0])
else:
    if n % 2 != 0:
        ans[(n+1)//2 - 1] = word[(n+1)//2 - 1]
    for i in range(n//2):
        ans[i], ans[-1-i] = word[i], word[-1-i]
    for i in range(n//2):
        if ans[i] == ans[-1-i]:
            for j in range(n + (-i-1), n-1):
                if ans[-i-1] != ans[n-(j+1)-1] and ans[j+1] != ans[-i-2]:
                    ans[-i-1], ans[j+1] = ans[j+1], ans[-1-i]
                    break
            else:
                print("-1")
                break
    else:
        for i in range(n-1):
            if ans[i] > ans[i+1]:
                if ans[i] != ans[-2-i] and ans[i+1] != ans[-1-i]:
                    ans[i], ans[i+1] = ans[i+1], ans[i]
        print("".join(ans))