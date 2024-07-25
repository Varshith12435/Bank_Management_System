class Account:
    accNo=0
    name=""
    deposit=0
    type=""
    phoneno=0
    email=""
    
    def createAccount(self,j):
        self.accNo=Account.accNo+j
        self.name=input("\nEnter the account Holder name:")
        self.phoneno=int(input("Enter your phone number:"))
        self.email=input("Enter your email id:")
        self.type=input("Enter the type of account[Savings(S)/Current(C)]:")
        self.c=0
        if(self.type=='S'):
            while(self.c!=1):
                print("Minimum balance for savings account is 500")
                self.amount=float(input("Enter amount:"))
                if(self.amount>=500):
                    self.deposit+=self.amount 
                    self.c=1
                else:
                    print("The amount", self.amount, "is insufficent for minimum balance in savings account, please try again")
        elif(self.type=='C'):
            while(self.c!=1):
                print("Minimum balance for currrent account is 1000")
                self.amount=float(input("Enter Amount:"))
                if(self.amount>=1000):
                    self.deposit+=self.amount
                    self.c=1
                else:
                    print("The amount", self.amount, "is insufficent for minimum balance in current account, please try again")
        print("Your account is Successfully Created")
        print("Your Account Number is 21EG105B", self.accNo,sep="")
        
    def showAccount(self):
        print("Account Number:", "21EG105B", self.accNo, sep="")
        print("Account Holder name:", self.name)
        print("Account Holder Phone Number:", self.phoneno)
        print("Account Holder email id:", self.email)
        if(self.type=='S'):
            print("Account Type: Savings Account")
        else:
            print("Account Type: Current Account")
        print("Balance Amount", self.deposit)
        
    def modifyAccount(self):
        self.c=1
        print("Account Number:","21EG105B", self.accNo, sep="")
        self.name=input("Modify Account Holder Name:")
        self.phoneno=int(input("Modify Account Holder Phone Number:"))
        self.email=input("Modify Account Holder email id:")
        self.type=input("Modify Type of Account[Savings (S)/Current(C)]:")
        if(self.type=='S'):
            while(self.c!=0):
                if(self.deposit<500):
                    print("Your deposit is less than minimum balance(500) for Savings Account")
                    print("Your balance amount is:", self.deposit)
                    print("You need to deposit", 500-self.deposit, "to get your minimum balance for Savings Account")
                    self.amount=float(input("Enter amount:"))
                    if((self.deposit+self.amount)>=500):
                        self.deposit+=self.amount
                        self.c=0
                    else:
                        print("Your account have minimum balance(500) for savings Account")
                        self.c=0
        elif(self.type=='C'):
            self.c=1
            while(self.c!=0):
                if(self.deposit<1000):
                    print("Your deposit is less than minimum balance(1000) for Current Account")
                    print("Your balance amount is:", self.deposit)
                    print("You need to deposit", 1000-self.deposit, "to get your minimum balance for Current Account")
                    self.amount=float(input("Enter amount:"))
                    if((self.deposit+self.amount)>=1000):
                        self.deposit+=self.amount 
                        self.c=0
                    else:
                        print("Your account have minimum balance (1000) for Current Account")
                        self.c=0
                        print("Your Account is Successfully Modified")
                        
    def depositAmount(self):
        self.amount=float(input("Enter Amount to deposit:"))
        self.deposit+=self.amount
        print("Balance Amount", self.deposit)
        
    def withdrawAmount(self):
        self.amount=float(input("Enter Amount to Withdraw:"))
        if(self.type=='S'): 
            if((self.deposit-self.amount)>=500):
                self.deposit-=self.amount
            else:
                print("Your Account minimum balance is 500") 
                print("You can not withdraw", self.amount, "from your account and Account balance reduces to", self.deposit-self.amount, "from", self.deposit)
        else:
            if((self.deposit-self.amount)>=1000): 
                self.deposit-=self.amount
            else:
                print("Your Account minimum balance is 1000") 
                print("You can not withdraw", self.amount, "from your account and Account balance reduces to", self.deposit-self.amount, "from", self.deposit)
                print("Balance Amount", self.deposit)
                
    def loan(self):
        self.h=1
        self.loanamount=float(input("Enter amount to take loan:"))
        if(self.loanamount>=1000000):
            while(self.h!=0):
                print("5 Years is the limit for repaying the amount", self.loanamount, "Select the number of years between them")
                self.years=float(input("Enter number of years to repay loan amount:"))
                if(self.years<=5 and self.years>0):
                    self.simpleintrest=(self.loanamount*self.years*10)/100
                    self.totalamount=self.loanamount+self.simpleintrest
                    self.monthlypay=self.totalamount/12
                    self.h=0
                else:
                    print("Select the years to repay loan amount between the given limit")
        elif(self.loanamount>=10000):
            while(self.h!=0):
                print("2 Years is the limit for repaying the amount", self.loanamount, "Select the number of years between them")
                self.years=float(input("Enter number of years to repay loan amount:"))
                if(self.years<=2 and self.years>0):
                    self.simpleintrest=(self.loanamount*self.years*5)/100
                    self.totalamount=self.loanamount+self.simpleintrest
                    self.monthlypay=self.totalamount/12
                    self.h=0
                else:
                    print("Select the years to repay loan amount between the given limit")
        self.deposit+=self.loanamount
        print(self.loanamount, "Rs is deposited to your account")
        print("Total Simple Intreat for",self.years, "years is:", self.simpleintrest)
        print("Total amount should be paid with intrest", self.totalamount)
        print("Monthly Pay:",round(self.monthlypay,2),"Rs in every month for",self.years*12,"months")
        
j=0
L=[]
M=[0]
while(1):
    g=1
    print("\n\t\t\t\t\t\t\tWelcome to Bank")
    print("\nIf you don't have account. Enter "1" to create your own bank account.")
    print("If you already have an Account.")
    a=input("Enter your Account Number to login:")
    if (a=="1"):
        j = j + 1
        L.append(j)
        c = int(L[- 1])
        x=Account()
        x.createAccount(j)
        M.append(0)
        M[j - 1] = x
    elif("21EG105B" in a):
        d=a.split("21EG105B")
        e=int(d[1])
        if(e in L):
            g = 0
        while(g!=1):
            print("\n1.Show Account Details\n2.Modify Account Details\n3.Deposit\n4.Withdraw\n5.Loan\n6.Logout\n7.Exit") 
            f=int(input("Enter your choice:"))
            if(f==1):
                M[e-1].showAccount()
            elif(f==2):
                M[e-1].modifyAccount()
            elif(f==3):
                M[e-1].depositAmount()
            elif(f==4):
                M[e-1].withdrawAmount()
            elif(f==5):
                M[e-1].loan()
            elif(f==6):
                g=1
            elif(f==7):
                quit()
            else:
                print("Choose Vaild option")
        else:
            print("No Account is created With this Account Number", a, "Please check your Account Number and Try again")
    else:
        print("Enter your account number or "1" to Create Account")
