def computepay(hours,rate):
 if hours > 40.0:
  p = rate * 40.0
  p = p+(1.5*rate*(hours-40))
 else:
  p = rate*hours
 return p
hours = float(raw_input("Enter worked hours: "))
rate = float(raw_input("Enter Pay rate per hour: "))
print("Pay",end=" ")
print (computepay(hours,rate))
