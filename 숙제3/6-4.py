def main():
    number = eval(input('정수 입력'))
    print(reverse(number))

def reverse(number):
    result = 0
    while number:
        rem = number %10
        result = result*10+rem
        number//=10
    return result

main()