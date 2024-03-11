number=eval(input("0과 1000사이 숫자 입력:"))
one = number %10
ten = (number // 10)%10
hundred = (number//100)

print("이 자릿수들의 합:",one+ten+hundred)