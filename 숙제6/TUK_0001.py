def main():
    number=eval(input())
    while True:
        if isPalindrome(number) and isPrime(number):
            print(number)
            break
        else:
            number+=1

def reverse(number): #숫자 반대로
    result=0
    while number:
        rem = number%10
        result = result*10 +rem
        number //=10
    return result

def isPalindrome(number): #대칭수
    if number == reverse(number):
        return True
    else:
        return False

def isPrime(number): #소수
    for i in range(2,int(number**0.5)+1): #i=1,2,3,4,...sqrt(number)
        if number % i ==0: #나누어떨어지면 소수x
            return False
    return True


main()