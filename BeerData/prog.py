import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

df = pd.read_excel(r'C:\Users\user\Python Programs\BeerData\pepsi-sales.xlsx',sheet_name="Data")
price12pk = df['PRICE 12PK']
price18pk = df['PRICE 18PK']
price30pk = df['PRICE 30PK']
cases12pk = df['CASES 12PK']
cases18pk = df['CASES 18PK']
cases30pk = df['CASES 30PK']
print(df.corr())

#Getting b1,b2 for price12pk vs week 
p12WeekCoeff = np.polyfit(list(range(1,53)),price12pk,1)
print("Price12 = %f Week + %f\n"%(p12WeekCoeff[0],p12WeekCoeff[1]))
plt.figure(1)
price12Week = np.polyval(p12WeekCoeff,range(1,53))
plt.plot(range(1,53),price12Week)
plt.scatter(list(range(1,53)),price12pk)


plt.figure(2)
p18WeekCoeff = np.polyfit(list(range(1,53)),price18pk,1)
print("Price18 = %f Week + %f\n"%(p18WeekCoeff[0],p18WeekCoeff[1]))
price18Week = np.polyval(p18WeekCoeff,range(1,53))
plt.plot(range(1,53),price18Week)
plt.scatter(list(range(1,53)),price18pk)


p30WeekCoeff = np.polyfit(list(range(1,53)),price30pk,1)
print("Price30 = %f Week + %f\n"%(p30WeekCoeff[0],p30WeekCoeff[1]))
plt.figure(3)
price30Week = np.polyval(p30WeekCoeff,range(1,53))
plt.plot(range(1,53),price30Week)
plt.scatter(list(range(1,53)),price30pk)


p12CasesCoeff = np.polyfit(price12pk,cases12pk,1)
print("Cases12 = %f Price12 + %f\n"%(p12CasesCoeff[0],p12CasesCoeff[1]))
plt.figure(4)
cases12Prices = np.polyval(p12CasesCoeff,price12pk)
plt.plot(price12pk,cases12Prices)
plt.scatter(price12pk,cases12pk)

p18CasesCoeff = np.polyfit(price18pk,cases18pk,1)
print("Cases12 = %f Price12 + %f\n"%(p18CasesCoeff[0],p18CasesCoeff[1]))
plt.figure(5)
cases18Prices = np.polyval(p18CasesCoeff,price18pk)
plt.plot(price18pk,cases18Prices)
plt.scatter(price18pk,cases18pk)

p30CasesCoeff = np.polyfit(price30pk,cases30pk,1)
print("Cases12 = %f Price12 + %f\n"%(p30CasesCoeff[0],p30CasesCoeff[1]))
plt.figure(6)
cases30Prices = np.polyval(p30CasesCoeff,price30pk)
plt.plot(price30pk,cases30Prices)
plt.scatter(price30pk,cases30pk)