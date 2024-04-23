def to_days(date):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
    return year*12*28+month*28+day #일수로 변경해서 반환
def solution(today, terms, privacies):
    D = {}  #'A':6, 'B':12, 'C':3
    for s in terms:
        key = s[0] #'A'
        value = int(s[2:]) #6
        D[key] = value  #key:value
    Today = to_days(today) #현재날짜를 일수로

    answer = []

    for i, privacy in enumerate(privacies):
        if Today >= to_days(privacy[:10]) + D[privacy[11]] * 28:
            answer.append(i+1)

    return answer

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))

print(solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))