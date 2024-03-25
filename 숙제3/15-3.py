def main():
    m,n = eval(input('두 정수 입력:'))
    print('{0}과 {1}의 gcd : {2}'.format(m,n,gcd(m,n)))

def gcd(m,n):
    if m%n == 0:
        return n
    return gcd(n,m%n)

main()