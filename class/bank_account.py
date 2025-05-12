class Bank:
    def __init__(self,owner,balance=0.0):
        self.owner=owner
        self.balance=balance

    def deposit(self,d_amount):
        self.balance += d_amount
        print(f"ငွေပမာဏ {d_amount} ကျပ် ထပ်မံထည့်သွင်းပါသည်။\n")

    def withdraw(self,w_amount):
        if w_amount <= self.balance:
            self.balance -= w_amount
            print(f"ငွေပမာဏ {w_amount} ကျပ် ထုတ်ယူပါသည်။\n")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.balance

name = input("အမည်ထည့်သွင်းပါ = ")
initial_balance = float(input("စတင်ထည့်သွင်းမည့် ပမာဏ = "))

p1 = Bank(name,initial_balance)
print(f"လက်ရှိလက်ကျန်ငွေမှာ {p1.get_balance()} ကျပ်ဖြစ်ပါသည်။\n")

while True:
    question = input("ငွေထပ်မံထည့်သွင်းလိုပါက 1 ကိုနှိပ်ပါ။\n"
                         "ငွေထုတ်ယူလိုပါက 2 ကိုနှိပ်ပါ။\n"
                         "ငွေလက်ကျန် စစ်ဆေးလိုပါက 3 ကိုနှိပ်ပါ။\n"
                         "ပရိုဂရမ်မှ ထွက်လိုပါက 0 ကိုနှိပ်ပါ။\n"
                         "ရွေးချယ်ပါ။ :\n")
    if question == "1":
        deposit = float(input("ထပ်မံထည့်သွင်းမည့် ပမာဏ = "))
        p1.deposit(deposit)


    elif question == "2":
        withdraw = float(input("ထုတ်ယူမည့် ပမာဏ = "))
        p1.withdraw(withdraw)

    elif question == "3":
        print(f"လက်ရှိလက်ကျန်ငွေမှာ {p1.get_balance()} ကျပ်ဖြစ်ပါသည်။\n")

    elif question == "0":
        print("ပရိုဂရမ်မှထွက်ပါသည်။ ကျေးဇူးတင်ရှိပါသည်။")
        break

    else:
        print("1 (သို့) 2 (သို့) 3 (သို့) 0 ကိုသာရွေးချယ်ပါ။\n")

