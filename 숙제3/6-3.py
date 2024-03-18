def main():
    number = eval(input('정수 입력'))
    if isPalindrome(number):
        print(number,'는 Palindrome이다')
    else:
        print(number,'는 Palindrome이 아니다')

def isPalindrome(number):
    if number == reverse(number):
        return True
    else:
        return False

def reverse(number):
    result = 0
    while number:
        rem = number %10
        result = result*10+rem
        number//=10
    return result

main()