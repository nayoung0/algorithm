def gcd(a, b) :
    if b==0:
        return a
    else :
        return gcd(b,a%b)

def lcm(a, b) :
    g = gcd(a,b)
    return int(g*(a/g)*(b/g))

n,m = map(int,input().split())
print(gcd(n, m))
print(lcm(n, m))