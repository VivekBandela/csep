def compoundInterest(P,r,T):
	if T==0:
		return principle
	else:
		ci=P*((1+r/100),T)
P=float(input("enter principle amount"))
T=folat(input("enter no.of years"))
r=float(input("enter rate of interest"))
ci=compoundInterest(P,r,T)
print("compound interest :{}".format(ci))
