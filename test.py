class Bank:
    def __init__(self,owner,balance=0.0):
        self.owner_name = owner
        self.owner_balance = balance

    def deposit(self,d_amount):
        self.owner_balance += d_amount
        print(f"ငွေပမာဏ {d_amount} ထည့်သွင်းပါသည်။")

    def withdraw(self,w_amount):
        if w_amount <= self.owner_balance:
            self.owner_balance -= w_amount
            print(f"ငွေပမာဏ {w_amount} ထုတ်ယူလိုက်ပါသည်။")
        else:
            print("လက်ကျန်ငွေမလုံလောက်ပါ။")

    def get_balance(self):
        return self.owner_balance

name = input("အမည် : ")
balance = float(input("ထည့်သွင်းမည့် ပမာဏ : "))

p1 = Bank(name,balance)
print(f"ပိုင်ရှင်အမည်မှာ {p1.owner_name}။ လက်ကျန်ငွေမှာ {p1.get_balance()} ကျပ်ဖြစ်ပါသည်။")

while True:
    user_choice = int(input("\nငွေထပ်မံထည့်သွင်းလိုပါက 1 ကိုနှိပ်ပါ။"
                            "\nငွေထုတ်လိုပါက 2 ကိုနှိပ်ပါ။"
                            "\nငွေလက်ကျန်စစ်ဆေးလိုပါက 3 ကိုနှိပ်ပါ။"
                            "\nProgram မှထွက်လိုပါက 0 ကိုနှိပ်ပါ။"
                            "\nတစ်ခုခုရွေးချယ်ပါ။ : "))

    if user_choice == 1:
        d_amt = float(input("\nထပ်မံထည့်သွင်းမည့် ပမာဏ : "))
        p1.deposit(d_amt)

    elif user_choice == 2:
        w_amt = float(input("\nထုတ်ယူမည့် ပမာဏ : "))
        p1.withdraw(w_amt)

    elif user_choice == 3:
        print(f"\nလက်ကျန်ငွေမှာ {p1.get_balance()} ကျပ် ဖြစ်ပါသည်။")

    elif user_choice == 0:
        print("\nProgram မှထွက်ပါသည်။ ကျေးဇူးတင်ပါသည်။")
        break

    else:
        print("1 သို့ 2 သို့ 3 သို့ 0 ကိုသာရွေးချယ်ပါ။")

