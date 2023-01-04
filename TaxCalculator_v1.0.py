print("Tax Calculator v1.0 Made by Shash#9820")
print("================================================================================================================")
print("This Australian Tax Calculator accurately calculates tax using the 2022 - 20223 tax rates.")
print("Tax varies depending on if you are an Australian Resident, Foreign Resident, Child or Working Holiday Maker")
print("================================================================================================================")
        
print("What is your income in Australian Dollars?")
    
Income = int(input("$"))
Income2 = Income
Income3 = Income
UserIncome = Income
   
if Income <= 18200:
    print("TAX")
    print("Your tax is $0.00. There is no tax for people with an income of $18,200 or below in Australia")
elif Income >= 18201 and Income <= 45000:
    Tax = (Income - 18200)* 0.19
    print("TAX")
    print("Your Tax is $",Tax,"AUD")
elif Income >= 45001 and Income <= 120000:
    Tax = 5092 + (Income - 45000)* 0.325
    print("TAX")
    print("Your Tax is $",Tax,"AUD")
elif Income >= 120001 and Income <= 180000:
    Tax = 29467 + (Income - 120000)* 0.37
    print("TAX")
    print("Your Tax is $",Tax,"AUD")
elif Income >= 180001:
    Tax = 51667 + (Income - 180000)* 0.45
    print("TAX")
    print("Your Tax is $",Tax,"AUD")