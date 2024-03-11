minutes = eval(input("분에 대한 숫자 입력:"))
total_days = minutes//(24*60)
years = total_days//365

print(minutes,"분은 약",years,"년",total_days%365,"일")