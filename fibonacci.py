n = input()
l = []
l.append(0)
l.append(1)
i = 2
while(i<=n):
    x = l[i-1] + l[i-2]
    l.append(x)
print(l[l.len-1])

def fib():
     n = int(input())
     a = 0
     b = 1
     p = []
     for i in range(n):
         p.append(a)
         a,b = b,a+b
     print(p)
fib()
