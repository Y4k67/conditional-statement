amount=float(input("please enter the price"))
sp=float(input("please enter the selling price"))
if sp>amount:
    x=sp-amount
    print("total profit",x)
else:
    print("no profit")