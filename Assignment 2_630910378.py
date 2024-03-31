class BankAccount:

    def __init__(self, account_number, balance, name, account_type):
        self.__account_number = account_number
        self.__balance = balance
        self.__name = name
        self.__account_type = account_type

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("จำนวนเงินที่ฝากต้องมากกว่า 0")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("จำนวนเงินที่ถอนต้องมากกว่า 0")
        if amount > self.__balance:
            raise ValueError("ยอดเงินคงเหลือไม่เพียงพอ")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_name(self):
        return self.__name

    def get_account_type(self):
        return self.__account_type

    def calculate_interest(self):
        if self.__account_type == "SAVINGS":
            return self.__balance * 0.015
        elif self.__account_type == "CHECKING":
            return self.__balance * 0.005
        else:
            raise ValueError("ประเภทบัญชีไม่ถูกต้อง")

    def transfer_to(self, other_account, amount):
        if amount <= 0:
            raise ValueError("จำนวนเงินที่โอนต้องมากกว่า 0")
        if amount > self.__balance:
            raise ValueError("ยอดเงินคงเหลือไม่เพียงพอ")
        self.__balance -= amount
        other_account.deposit(amount)

    def __str__(self):
        return f"Account number: {self.__account_number}\n" \
               f"Name: {self.__name}\n" \
               f"Account type: {self.__account_type}\n" \
               f"Balance: {self.__balance}"

# สร้างออปเจ็ค BankAccount
account1 = BankAccount(630910378_1, 10000, "Suknipat Santamanas", "SAVINGS")

# ฝากเงิน
account1.deposit(5000)

# ถอนเงิน
account1.withdraw(2000)

# ตรวจสอบยอดเงินคงเหลือ
balance = account1.get_balance()

# คำนวณดอกเบี้ย
interest = account1.calculate_interest()

# โอนเงินไปยังบัญชีอื่น
account2 = BankAccount(630910378_2, 5000, "Suknipat Santamanas", "CHECKING")
account1.transfer_to(account2, 1000)

# พิมพ์ข้อมูล
print(account1)
print(account2)