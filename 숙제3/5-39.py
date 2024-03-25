def main():
    sales = 1 #1원 부터 시작해서 늘려나감
    Goal = 250000000
    commission = 0
    while commission <Goal:
        sales +=1
        print('sales',sales,'commission',commission)
        if sales>100000000:
            commission = 5000000*0.08 +5000000*0.1 +(sales-100000000)*0.12
        elif sales>5000000:
            commission = 5000000*0.08 + (sales-5000000)*0.1
        else:
            commission = sales*0.08
    print('연봉 3천만원이 되기위한 최소 매출액:',sales)

main()