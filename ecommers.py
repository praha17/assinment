def cal_total_price(p,n,t):
    s=p*n
    tax=s*(t)/100
    total_amount_to_be_paid=s+tax
    print("The total amount to be paid: ",total_amount_to_be_paid)
cal_total_price(300,8,5)
