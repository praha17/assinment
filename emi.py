def emi(p,r,t):
    monthy_rate=r/(12*100)
    emi_calc=(p*monthy_rate)*(1+monthy_rate)**t/((1+monthy_rate)**t-1)
    print("Your EMI is: ",emi_calc)
emi(5000,10,24)