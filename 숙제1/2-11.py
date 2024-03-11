value = eval(input("약정 금액:"))
rate = eval(input("연이율 % :"))
years = eval(input("약정기간 년:"))

month_rate = rate / 1200
deposit = value/(1+month_rate)**(years*12)
print("최초 예금: ",deposit)