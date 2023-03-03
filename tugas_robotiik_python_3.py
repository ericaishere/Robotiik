#[SOAL NOMOR 3] Buat hierarki kelas untuk sistem perbankan. 
# Sistem harus memiliki kelas dasar untuk akun, dengan kelas turunan untuk rekening giro dan rekening tabungan. 
# Kelas rekening giro harus memiliki variabel instan untuk nomor rekening, saldo, dan riwayat transaksi. 
# Kelas rekening tabungan harus memiliki variabel instan untuk nomor rekening, saldo, dan suku bunga. 
# Kelas rekening giro dan tabungan harus memiliki metode untuk menarik dan menyetor uang, dan kelas rekening giro juga harus memiliki metode untuk menulis cek. 
# Hierarki kelas harus dibuat sehingga kode berikut dapat berjalan dan menghasilkan output berikut.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: ${amount:.2f}")
        else:
            print("Insufficient funds")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.transactions = []

    def write_check(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: ${amount:.2f}")
            self.transactions.append(f"Check: ${amount:.2f}")
        else:
            print("Error: Insufficient funds.")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        self.transactions.append(f"Interest: ${interest:.2f}")


checking = CheckingAccount("123456", 1000.00)
savings = SavingsAccount("654321", 5000.00, 0.02)

checking.write_check(100.00)
savings.calculate_interest()

print(checking.account_number, checking.balance, checking.transactions)
print(savings.account_number, savings.balance, savings.transactions)
