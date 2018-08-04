n, m = map(int, input().split())

r = 2

for i in range(0, n//2):
    base = (1 + r * i) * ".|."
    print(base.center(m, '-'))

print("WELCOME".center(m, '-'))

for i in range(n//2-1, -1, -1):
    base = (1 + r * i) * ".|."
    print(base.center(m, '-'))
