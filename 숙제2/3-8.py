name = input('사원 이름:')
hour = eval(input('주당 근무 시간'))
salary = eval(input('시간당 급여:'))
rate1 = eval(input('원천징수세율:'))
rate2 = eval(input('지방세율:'))
print('사원이름 : ',name)
print('주당 근무 시간 : ',hour)
print('시간당 임금 : ',salary)
print('총급여 : ',salary*hour)
print('공제:')
tex1 = salary*hour*rate1
print('\t원천징수세(',rate1*100,  '%):',tex1)
tex2 = salary*hour*rate2
print('\t지방세(',rate2*100,  '%):',tex2)
print('\t총공제:',tex1+tex2)
print('공제 후 급여:',salary*hour-tex1-tex2)