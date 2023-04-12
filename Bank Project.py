class Bank:
    def __init__(ref,name, acctNum, password,checking,savings,loans):
        ref.acctNum = acctNum
        ref.password = password
        ref.name = name
        ref.checking = checking
        ref.savings = savings
        ref.loans = loans
    def __str__(ref):
        return f'{ref.name}({"Checking $" + (str(ref.checking)),"Savings $" + (str(ref.savings)),"Loans $" + (str(ref.loans))})'
        
class Actions(Bank):
    def __init__(act, deposit, loan, withdraw):
        act.deposit = deposit
        act.loan = loan
        act.withdraw = withdraw







marge = Bank("Marge Simpson",311,"Homey123",0,0, 0)
homer = Bank("Homer Simpson", 411, "Maggie123", 0,0,0)
smithers = Bank("Waylon Smithers",511, "Mrburns123",0,0,0)

